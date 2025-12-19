"""
Email Reader Module
Handles email connection via IMAP and fetches unread emails
"""
import imaplib
import email
from email.header import decode_header
from email.message import Message
import logging
from typing import List, Tuple, Optional

logger = logging.getLogger(__name__)


class EmailReader:
    """
    Manages email connection and retrieval operations
    """
    
    def __init__(self, host: str, port: int, username: str, password: str):
        """
        Initialize email reader with connection parameters
        
        Args:
            host: IMAP server hostname
            port: IMAP server port
            username: Email account username
            password: Email account password
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None
        
    def connect(self) -> bool:
        """
        Establish connection to email server
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            logger.info(f"Connecting to {self.host}:{self.port}")
            self.connection = imaplib.IMAP4_SSL(self.host, self.port)
            self.connection.login(self.username, self.password)
            logger.info("Email connection established successfully")
            return True
        except imaplib.IMAP4.error as e:
            logger.error(f"IMAP authentication failed: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to connect to email server: {e}")
            return False
    
    def disconnect(self):
        """Close email connection safely"""
        try:
            if self.connection:
                self.connection.close()
                self.connection.logout()
                logger.info("Email connection closed")
        except Exception as e:
            logger.warning(f"Error during disconnect: {e}")
    
    def get_unread_emails(self, filter_keywords: List[str] = None) -> List[Tuple[str, object]]:
        """
        Fetch all unread emails, optionally filtered by subject keywords
        
        Args:
            filter_keywords: List of keywords to filter email subjects
            
        Returns:
            List of tuples containing (email_id, email_message_object)
        """
        unread_emails = []
        
        try:
            # Select inbox folder
            self.connection.select('INBOX')
            
            # Search for unread emails
            status, messages = self.connection.search(None, 'UNSEEN')
            
            if status != 'OK':
                logger.error("Failed to search for unread emails")
                return unread_emails
            
            email_ids = messages[0].split()
            logger.info(f"Found {len(email_ids)} unread emails")
            
            for email_id in email_ids:
                try:
                    # Fetch email data
                    status, msg_data = self.connection.fetch(email_id, '(RFC822)')
                    
                    if status != 'OK':
                        logger.warning(f"Failed to fetch email {email_id}")
                        continue
                    
                    # Parse email message
                    email_body = msg_data[0][1]
                    email_message = email.message_from_bytes(email_body)
                    
                    # Decode subject
                    subject = self._decode_subject(email_message.get('Subject', ''))
                    
                    # Filter by keywords if provided
                    if filter_keywords:
                        if not any(keyword.lower() in subject.lower() for keyword in filter_keywords):
                            logger.debug(f"Email {email_id} filtered out: '{subject}'")
                            continue
                    
                    logger.info(f"Processing email {email_id.decode()}: '{subject}'")
                    unread_emails.append((email_id.decode(), email_message))
                    
                except Exception as e:
                    logger.error(f"Error processing email {email_id}: {e}")
                    continue
            
            logger.info(f"Retrieved {len(unread_emails)} matching emails")
            
        except Exception as e:
            logger.error(f"Error fetching unread emails: {e}")
        
        return unread_emails
    
    def mark_as_read(self, email_id: str):
        """
        Mark an email as read
        
        Args:
            email_id: Email identifier to mark as read
        """
        try:
            self.connection.store(email_id, '+FLAGS', '\\Seen')
            logger.debug(f"Marked email {email_id} as read")
        except Exception as e:
            logger.warning(f"Failed to mark email {email_id} as read: {e}")
    
    @staticmethod
    def _decode_subject(subject: str) -> str:
        """
        Decode email subject handling various encodings
        
        Args:
            subject: Raw subject string
            
        Returns:
            Decoded subject string
        """
        if not subject:
            return "No Subject"
        
        decoded_parts = decode_header(subject)
        decoded_subject = ""
        
        for part, encoding in decoded_parts:
            if isinstance(part, bytes):
                try:
                    decoded_subject += part.decode(encoding or 'utf-8')
                except:
                    decoded_subject += part.decode('utf-8', errors='ignore')
            else:
                decoded_subject += part
        
        return decoded_subject
    
    @staticmethod
    def get_email_metadata(email_message: Message) -> dict:
        """
        Extract metadata from email message
        
        Args:
            email_message: Email message object
            
        Returns:
            Dictionary containing email metadata
        """
        metadata = {
            'subject': EmailReader._decode_subject(email_message.get('Subject', '')),
            'from': email_message.get('From', 'Unknown'),
            'date': email_message.get('Date', 'Unknown'),
            'to': email_message.get('To', 'Unknown')
        }
        return metadata
