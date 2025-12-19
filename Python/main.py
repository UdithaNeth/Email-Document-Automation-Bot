"""
Main Orchestration Module
Entry point for Email & Document Automation Bot
Coordinates email reading, attachment handling, and document processing
"""
import sys
import logging
from pathlib import Path

# Import configuration
import config

# Import modules
from email_reader import EmailReader
from attachment_handler import AttachmentHandler
from document_processor import DocumentProcessor


def setup_logging():
    """
    Configure logging for the application
    Logs to both file and console with appropriate formatting
    """
    # Create formatters
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )
    
    # File handler
    file_handler = logging.FileHandler(config.LOG_FILE, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)
    
    # Root logger configuration
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)


def validate_configuration():
    """
    Validate essential configuration parameters
    
    Returns:
        bool: True if configuration is valid, False otherwise
    """
    logger = logging.getLogger(__name__)
    
    # Check email credentials
    if config.EMAIL_USER == 'your_email@example.com' or config.EMAIL_PASSWORD == 'your_password':
        logger.error("Email credentials not configured. Please set EMAIL_USER and EMAIL_PASSWORD environment variables.")
        return False
    
    # Validate email host
    if not config.EMAIL_HOST:
        logger.error("Email host not configured.")
        return False
    
    logger.info("Configuration validated successfully")
    return True


def process_emails():
    """
    Main processing function
    Connects to email, fetches unread emails, downloads attachments, and organizes documents
    
    Returns:
        bool: True if execution successful, False otherwise
    """
    logger = logging.getLogger(__name__)
    logger.info("=" * 60)
    logger.info("Starting Email & Document Automation Bot")
    logger.info("=" * 60)
    
    # Initialize components
    email_reader = None
    total_processed = 0
    total_saved = 0
    
    try:
        # Step 1: Initialize Email Reader
        logger.info("Step 1: Initializing Email Reader")
        email_reader = EmailReader(
            host=config.EMAIL_HOST,
            port=config.EMAIL_PORT,
            username=config.EMAIL_USER,
            password=config.EMAIL_PASSWORD
        )
        
        # Step 2: Connect to email server
        logger.info("Step 2: Connecting to email server")
        if not email_reader.connect():
            logger.error("Failed to connect to email server")
            return False
        
        # Step 3: Fetch unread emails with filters
        logger.info("Step 3: Fetching unread emails")
        filter_keywords = list(config.FILTER_KEYWORDS.keys())
        unread_emails = email_reader.get_unread_emails(filter_keywords)
        
        if not unread_emails:
            logger.info("No matching unread emails found")
            return True
        
        # Step 4: Initialize Attachment Handler
        logger.info("Step 4: Initializing Attachment Handler")
        attachment_handler = AttachmentHandler(
            download_base_dir=config.DOWNLOAD_BASE_DIR,
            allowed_extensions=config.ALLOWED_EXTENSIONS,
            max_size_mb=config.MAX_ATTACHMENT_SIZE_MB
        )
        
        # Step 5: Initialize Document Processor
        logger.info("Step 5: Initializing Document Processor")
        document_processor = DocumentProcessor(
            document_folders=config.DOCUMENT_FOLDERS,
            filter_keywords=config.FILTER_KEYWORDS
        )
        
        # Step 6: Process each email
        logger.info(f"Step 6: Processing {len(unread_emails)} emails")
        
        for email_id, email_message in unread_emails:
            try:
                # Get email metadata
                metadata = EmailReader.get_email_metadata(email_message)
                logger.info(f"Processing email from: {metadata['from']}")
                logger.info(f"Subject: {metadata['subject']}")
                
                # Extract attachments
                attachments = attachment_handler.extract_attachments(email_message)
                
                if not attachments:
                    logger.info("No valid attachments found in this email")
                    email_reader.mark_as_read(email_id)
                    continue
                
                logger.info(f"Found {len(attachments)} attachment(s)")
                
                # Process each attachment
                for filename, file_data in attachments:
                    total_processed += 1
                    
                    # Determine document type
                    doc_type = document_processor.determine_document_type(metadata['subject'])
                    target_folder = config.DOCUMENT_FOLDERS.get(doc_type, config.DOCUMENT_FOLDERS['Others'])
                    
                    # Save attachment temporarily
                    temp_path = attachment_handler.save_attachment(
                        filename=filename,
                        file_data=file_data,
                        destination_folder=target_folder
                    )
                    
                    if temp_path:
                        # Process and organize document
                        final_path = document_processor.process_attachment(temp_path, metadata)
                        
                        if final_path:
                            total_saved += 1
                            logger.info(f"Successfully processed: {final_path.name}")
                        else:
                            logger.warning(f"Failed to organize: {filename}")
                    else:
                        logger.warning(f"Failed to save: {filename}")
                
                # Mark email as read after processing
                email_reader.mark_as_read(email_id)
                
            except Exception as e:
                logger.error(f"Error processing email {email_id}: {e}", exc_info=True)
                continue
        
        # Step 7: Summary
        logger.info("=" * 60)
        logger.info("Processing Complete")
        logger.info(f"Total attachments processed: {total_processed}")
        logger.info(f"Total documents saved: {total_saved}")
        logger.info("=" * 60)
        
        return True
        
    except Exception as e:
        logger.error(f"Critical error during execution: {e}", exc_info=True)
        return False
        
    finally:
        # Cleanup: Disconnect from email server
        if email_reader:
            email_reader.disconnect()
            logger.info("Disconnected from email server")


def main():
    """
    Main entry point
    Sets up logging, validates configuration, and runs the automation
    """
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Validate configuration
        if not validate_configuration():
            print("ERROR: Configuration validation failed")
            sys.exit(1)
        
        # Run email processing
        success = process_emails()
        
        if success:
            print("SUCCESS: Automation completed successfully")
            sys.exit(0)
        else:
            print("ERROR: Automation failed")
            sys.exit(1)
            
    except KeyboardInterrupt:
        logger.info("Automation interrupted by user")
        print("INFO: Automation stopped by user")
        sys.exit(2)
        
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        print(f"CRITICAL ERROR: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
