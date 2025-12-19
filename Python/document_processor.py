"""
Document Processor Module
Handles document renaming and organization into appropriate folders
"""
import re
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class DocumentProcessor:
    """
    Processes and organizes documents based on type and metadata
    """
    
    def __init__(self, document_folders: Dict[str, Path], filter_keywords: Dict[str, str]):
        """
        Initialize document processor
        
        Args:
            document_folders: Dictionary mapping folder names to Path objects
            filter_keywords: Dictionary mapping keywords to document types
        """
        self.document_folders = document_folders
        self.filter_keywords = filter_keywords
        
    def determine_document_type(self, subject: str) -> str:
        """
        Determine document type based on email subject
        
        Args:
            subject: Email subject line
            
        Returns:
            Document type folder name
        """
        subject_lower = subject.lower()
        
        # Check each keyword to determine document type
        for keyword, doc_type in self.filter_keywords.items():
            if keyword.lower() in subject_lower:
                logger.debug(f"Matched keyword '{keyword}' -> type '{doc_type}'")
                return doc_type
        
        # Default to 'Others' if no match
        return 'Others'
    
    @staticmethod
    def sanitize_filename(text: str, max_length: int = 50) -> str:
        """
        Sanitize text for use in filenames
        
        Args:
            text: Raw text to sanitize
            max_length: Maximum length for the sanitized text
            
        Returns:
            Sanitized string safe for filenames
        """
        # Remove or replace invalid characters
        sanitized = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', text)
        
        # Remove extra whitespace
        sanitized = re.sub(r'\s+', '_', sanitized.strip())
        
        # Limit length
        if len(sanitized) > max_length:
            sanitized = sanitized[:max_length]
        
        return sanitized
    
    @staticmethod
    def extract_sender_name(from_field: str) -> str:
        """
        Extract sender name from email From field
        
        Args:
            from_field: Email From header value
            
        Returns:
            Sanitized sender name
        """
        # Try to extract name from "Name <email@example.com>" format
        match = re.search(r'^([^<]+)', from_field)
        if match:
            name = match.group(1).strip()
            # Remove quotes if present
            name = name.strip('"\'')
        else:
            # Use email address if name not found
            email_match = re.search(r'[\w\.-]+@[\w\.-]+', from_field)
            name = email_match.group(0).split('@')[0] if email_match else 'Unknown'
        
        return DocumentProcessor.sanitize_filename(name, max_length=30)
    
    def generate_new_filename(self, original_filename: str, doc_type: str, 
                             sender: str, email_date: str) -> str:
        """
        Generate a meaningful filename based on document metadata
        Format: <DocumentType>_<Date>_<Sender>.<ext>
        
        Args:
            original_filename: Original attachment filename
            doc_type: Type of document (Invoices, Resumes, etc.)
            sender: Sender's name or email
            email_date: Email date string
            
        Returns:
            New formatted filename
        """
        # Extract file extension
        file_path = Path(original_filename)
        extension = file_path.suffix
        
        # Parse and format date
        try:
            # Try to parse email date (can be in various formats)
            date_str = self._parse_email_date(email_date)
        except:
            # Fallback to current date if parsing fails
            date_str = datetime.now().strftime('%Y%m%d')
            logger.warning(f"Could not parse email date '{email_date}', using current date")
        
        # Sanitize sender name
        sender_clean = self.sanitize_filename(sender, max_length=20)
        
        # Create new filename
        new_filename = f"{doc_type}_{date_str}_{sender_clean}{extension}"
        
        logger.info(f"Generated filename: {original_filename} -> {new_filename}")
        return new_filename
    
    @staticmethod
    def _parse_email_date(email_date: str) -> str:
        """
        Parse email date string and format as YYYYMMDD
        
        Args:
            email_date: Date string from email header
            
        Returns:
            Formatted date string
        """
        try:
            # Email dates can be complex, try to extract basic date info
            # Example: "Thu, 19 Dec 2025 10:30:00 +0000"
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(email_date)
            return dt.strftime('%Y%m%d')
        except:
            # Fallback to current date
            return datetime.now().strftime('%Y%m%d')
    
    def organize_document(self, file_path: Path, doc_type: str, 
                         new_filename: str) -> Optional[Path]:
        """
        Move and rename document to appropriate folder
        
        Args:
            file_path: Current path of the file
            doc_type: Type of document
            new_filename: New name for the file
            
        Returns:
            New file path after organization, or None if failed
        """
        try:
            # Get target folder
            target_folder = self.document_folders.get(doc_type, self.document_folders['Others'])
            target_folder.mkdir(parents=True, exist_ok=True)
            
            # Create new file path
            new_path = target_folder / new_filename
            
            # Handle duplicate filenames
            counter = 1
            original_stem = new_path.stem
            original_suffix = new_path.suffix
            
            while new_path.exists():
                new_name = f"{original_stem}_{counter}{original_suffix}"
                new_path = target_folder / new_name
                counter += 1
            
            # Move and rename file
            file_path.rename(new_path)
            logger.info(f"Organized document: {file_path.name} -> {new_path}")
            
            return new_path
            
        except Exception as e:
            logger.error(f"Failed to organize document {file_path}: {e}")
            return None
    
    def process_attachment(self, file_path: Path, email_metadata: dict) -> Optional[Path]:
        """
        Complete processing: determine type, rename, and organize
        
        Args:
            file_path: Path to the attachment file
            email_metadata: Dictionary containing email metadata (subject, from, date)
            
        Returns:
            Final path of processed document, or None if failed
        """
        try:
            # Determine document type from email subject
            doc_type = self.determine_document_type(email_metadata['subject'])
            
            # Extract sender name
            sender = self.extract_sender_name(email_metadata['from'])
            
            # Generate new filename
            new_filename = self.generate_new_filename(
                file_path.name,
                doc_type,
                sender,
                email_metadata['date']
            )
            
            # Organize document
            final_path = self.organize_document(file_path, doc_type, new_filename)
            
            return final_path
            
        except Exception as e:
            logger.error(f"Failed to process attachment {file_path}: {e}")
            return None
