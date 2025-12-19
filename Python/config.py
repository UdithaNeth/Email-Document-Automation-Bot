"""
Configuration module for Email & Document Automation Bot
Contains email credentials, folder paths, and application settings
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email Configuration
# IMPORTANT: Use environment variables or a secure vault in production
EMAIL_HOST = os.getenv('EMAIL_HOST', 'imap.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '993'))
EMAIL_USER = os.getenv('EMAIL_USER', 'your_email@example.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_password')

# Email Filter Keywords
# Emails with these keywords in subject will be processed
FILTER_KEYWORDS = {
    'Invoice': 'Invoices',
    'Bill': 'Invoices',
    'Resume': 'Resumes',
    'CV': 'Resumes',
    'Report': 'Reports',
    'Analysis': 'Reports'
}

# Base directory for downloaded documents
BASE_DIR = Path(__file__).parent.parent
DOWNLOAD_BASE_DIR = BASE_DIR / 'Downloads'

# Folder structure for organizing documents
DOCUMENT_FOLDERS = {
    'Invoices': DOWNLOAD_BASE_DIR / 'Invoices',
    'Resumes': DOWNLOAD_BASE_DIR / 'Resumes',
    'Reports': DOWNLOAD_BASE_DIR / 'Reports',
    'Others': DOWNLOAD_BASE_DIR / 'Others'
}

# Log file configuration
LOG_DIR = BASE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'bot.log'

# Allowed file extensions for attachments
ALLOWED_EXTENSIONS = ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.txt', '.png', '.jpg', '.jpeg']

# Maximum attachment size in MB
MAX_ATTACHMENT_SIZE_MB = 25

# Create necessary directories
def initialize_directories():
    """Create all required directories if they don't exist"""
    LOG_DIR.mkdir(exist_ok=True)
    DOWNLOAD_BASE_DIR.mkdir(exist_ok=True)
    for folder_path in DOCUMENT_FOLDERS.values():
        folder_path.mkdir(exist_ok=True)

# Initialize on import
initialize_directories()
