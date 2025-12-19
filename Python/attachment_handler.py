"""
Attachment Handler Module
Manages downloading and saving email attachments safely
"""
import os
import email
import hashlib
import logging
from pathlib import Path
from typing import List, Tuple, Optional

logger = logging.getLogger(__name__)


class AttachmentHandler:
    """
    Handles attachment extraction, validation, and storage
    """
    
    def __init__(self, download_base_dir: Path, allowed_extensions: List[str], max_size_mb: int = 25):
        """
        Initialize attachment handler
        
        Args:
            download_base_dir: Base directory for storing attachments
            allowed_extensions: List of permitted file extensions
            max_size_mb: Maximum allowed attachment size in megabytes
        """
        self.download_base_dir = download_base_dir
        self.allowed_extensions = [ext.lower() for ext in allowed_extensions]
        self.max_size_bytes = max_size_mb * 1024 * 1024
        self.processed_hashes = self._load_processed_hashes()
        
    def _load_processed_hashes(self) -> set:
        """
        Load previously processed attachment hashes to prevent duplicates
        
        Returns:
            Set of file hashes
        """
        hash_file = self.download_base_dir / '.processed_hashes.txt'
        hashes = set()
        
        if hash_file.exists():
            try:
                with open(hash_file, 'r') as f:
                    hashes = set(line.strip() for line in f if line.strip())
                logger.info(f"Loaded {len(hashes)} processed file hashes")
            except Exception as e:
                logger.warning(f"Failed to load processed hashes: {e}")
        
        return hashes
    
    def _save_processed_hash(self, file_hash: str):
        """
        Save a file hash to prevent duplicate processing
        
        Args:
            file_hash: SHA256 hash of the file
        """
        hash_file = self.download_base_dir / '.processed_hashes.txt'
        try:
            with open(hash_file, 'a') as f:
                f.write(f"{file_hash}\n")
            self.processed_hashes.add(file_hash)
        except Exception as e:
            logger.error(f"Failed to save processed hash: {e}")
    
    @staticmethod
    def _calculate_hash(data: bytes) -> str:
        """
        Calculate SHA256 hash of file data
        
        Args:
            data: File content as bytes
            
        Returns:
            Hexadecimal hash string
        """
        return hashlib.sha256(data).hexdigest()
    
    def _is_valid_extension(self, filename: str) -> bool:
        """
        Check if file extension is allowed
        
        Args:
            filename: Name of the file
            
        Returns:
            True if extension is allowed, False otherwise
        """
        ext = Path(filename).suffix.lower()
        return ext in self.allowed_extensions
    
    def _is_valid_size(self, data: bytes) -> bool:
        """
        Check if file size is within limits
        
        Args:
            data: File content as bytes
            
        Returns:
            True if size is acceptable, False otherwise
        """
        size_bytes = len(data)
        size_mb = size_bytes / (1024 * 1024)
        
        if size_bytes > self.max_size_bytes:
            logger.warning(f"File size {size_mb:.2f} MB exceeds limit of {self.max_size_bytes / (1024 * 1024)} MB")
            return False
        return True
    
    def extract_attachments(self, email_message: email.message.Message) -> List[Tuple[str, bytes]]:
        """
        Extract all attachments from an email message
        
        Args:
            email_message: Email message object
            
        Returns:
            List of tuples containing (filename, file_data)
        """
        attachments = []
        
        try:
            for part in email_message.walk():
                # Skip non-attachment parts
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                
                filename = part.get_filename()
                
                if filename:
                    # Decode filename if needed
                    if isinstance(filename, bytes):
                        filename = filename.decode()
                    
                    # Validate extension
                    if not self._is_valid_extension(filename):
                        logger.warning(f"Skipping file with disallowed extension: {filename}")
                        continue
                    
                    # Get file data
                    file_data = part.get_payload(decode=True)
                    
                    if file_data:
                        # Validate size
                        if not self._is_valid_size(file_data):
                            logger.warning(f"Skipping oversized file: {filename}")
                            continue
                        
                        # Check for duplicates using hash
                        file_hash = self._calculate_hash(file_data)
                        if file_hash in self.processed_hashes:
                            logger.info(f"Skipping duplicate file: {filename}")
                            continue
                        
                        attachments.append((filename, file_data))
                        logger.info(f"Extracted attachment: {filename} ({len(file_data) / 1024:.2f} KB)")
                        
                        # Mark as processed
                        self._save_processed_hash(file_hash)
        
        except Exception as e:
            logger.error(f"Error extracting attachments: {e}")
        
        return attachments
    
    def save_attachment(self, filename: str, file_data: bytes, destination_folder: Path) -> Optional[Path]:
        """
        Save attachment to specified folder
        
        Args:
            filename: Original filename
            file_data: File content as bytes
            destination_folder: Target folder for saving
            
        Returns:
            Path to saved file, or None if failed
        """
        try:
            # Ensure destination folder exists
            destination_folder.mkdir(parents=True, exist_ok=True)
            
            # Create full file path
            file_path = destination_folder / filename
            
            # Handle duplicate filenames
            counter = 1
            original_stem = file_path.stem
            original_suffix = file_path.suffix
            
            while file_path.exists():
                new_name = f"{original_stem}_{counter}{original_suffix}"
                file_path = destination_folder / new_name
                counter += 1
            
            # Write file
            with open(file_path, 'wb') as f:
                f.write(file_data)
            
            logger.info(f"Saved attachment to: {file_path}")
            return file_path
            
        except Exception as e:
            logger.error(f"Failed to save attachment {filename}: {e}")
            return None
