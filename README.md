# Email & Document Automation Bot

An enterprise-grade RPA solution for automated email processing and document management. This bot connects to email accounts via IMAP, filters emails by subject keywords, downloads attachments, and organizes them into categorized folders with meaningful naming conventions.

## 🎯 Features

### Python Backend (Core Automation)
- **Email Processing**: Connects to email inbox using IMAP protocol
- **Smart Filtering**: Processes only UNREAD emails with specific keywords
- **Attachment Management**: Downloads and validates attachments
- **Duplicate Prevention**: SHA256 hash-based duplicate detection
- **Intelligent Naming**: Renames files using format: `<DocumentType>_<Date>_<Sender>.<ext>`
- **Auto-Organization**: Sorts documents into categorized folders
- **Robust Error Handling**: Comprehensive exception handling and logging
- **Configurable**: Environment variable-based configuration

### C# WinForms UI (Frontend)
- **Simple Interface**: Clean, minimal desktop application
- **Run/Stop Controls**: Start and stop automation with button clicks
- **Real-time Output**: Live display of Python script stdout/stderr
- **Log Viewer**: Quick access to detailed log files
- **Status Indicators**: Visual feedback on automation state

## 📁 Project Structure

```
Email-Document-Automation-Bot/
├── Python/                          # Backend automation scripts
│   ├── main.py                      # Main orchestration entry point
│   ├── config.py                    # Configuration and settings
│   ├── email_reader.py              # Email connection and fetching
│   ├── attachment_handler.py        # Attachment download and validation
│   ├── document_processor.py        # Document renaming and organization
│   └── requirements.txt             # Python dependencies
│
├── DotNet/                          # Frontend UI application
│   └── EmailAutomationBot/
│       ├── EmailAutomationBot.csproj    # C# project file
│       ├── Program.cs                    # Application entry point
│       ├── MainForm.cs                   # Main UI form logic
│       ├── MainForm.Designer.cs          # UI designer code
│       ├── MainForm.resx                 # Form resources
│       └── AutomationEngine.cs           # Python process manager
│
├── Downloads/                       # Generated folders for documents
│   ├── Invoices/
│   ├── Resumes/
│   ├── Reports/
│   └── Others/
│
└── logs/                           # Application logs
    └── bot.log                     # Detailed execution logs
```

## 🚀 Getting Started

### Prerequisites

**Python Backend:**
- Python 3.8 or higher
- pip package manager
- Email account with IMAP access enabled

**C# Frontend:**
- .NET 6.0 SDK or higher
- Windows OS (for WinForms)

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Email-Document-Automation-Bot.git
cd Email-Document-Automation-Bot
```

#### 2. Set Up Python Environment
```bash
cd Python
pip install -r requirements.txt
```

#### 3. Configure Email Credentials

**Option A: Environment Variables (Recommended)**
```bash
# Windows PowerShell
$env:EMAIL_HOST = "imap.gmail.com"
$env:EMAIL_PORT = "993"
$env:EMAIL_USER = "your_email@gmail.com"
$env:EMAIL_PASSWORD = "your_app_password"

# Windows Command Prompt
set EMAIL_HOST=imap.gmail.com
set EMAIL_PORT=993
set EMAIL_USER=your_email@gmail.com
set EMAIL_PASSWORD=your_app_password
```

**Option B: Edit config.py**
Modify the default values in `Python/config.py` (not recommended for production)

#### 4. Build C# Application
```bash
cd DotNet/EmailAutomationBot
dotnet build
dotnet run
```

## 📧 Email Configuration

### Gmail Setup
1. Enable IMAP in Gmail Settings
2. Generate an App Password (if 2FA is enabled)
3. Use the app password instead of your regular password

### Other Email Providers
Configure the IMAP settings accordingly:
- **Outlook/Office365**: `outlook.office365.com:993`
- **Yahoo**: `imap.mail.yahoo.com:993`
- **Custom**: Check your provider's IMAP settings

## 🎮 Usage

### Using the Desktop UI (Recommended)

1. **Launch Application**: Run `EmailAutomationBot.exe` or use `dotnet run`
2. **Click "Run Automation"**: Starts the Python backend
3. **Monitor Output**: View real-time processing in the output console
4. **Stop if Needed**: Click "Stop Automation" to terminate
5. **View Logs**: Click "View Logs" to open detailed log file

### Using Python Directly

```bash
cd Python
python main.py
```

**Exit Codes:**
- `0`: Success
- `1`: Error
- `2`: User interrupted

## 📋 Configuration Details

### Email Filter Keywords (config.py)
```python
FILTER_KEYWORDS = {
    'Invoice': 'Invoices',      # Keyword -> Folder mapping
    'Bill': 'Invoices',
    'Resume': 'Resumes',
    'CV': 'Resumes',
    'Report': 'Reports',
    'Analysis': 'Reports'
}
```

### Allowed File Extensions
```python
ALLOWED_EXTENSIONS = [
    '.pdf', '.docx', '.doc', 
    '.xlsx', '.xls', '.txt',
    '.png', '.jpg', '.jpeg'
]
```

### File Size Limit
```python
MAX_ATTACHMENT_SIZE_MB = 25  # Maximum attachment size
```

## 🔍 How It Works

### Automation Workflow

```
1. Connect to Email Server (IMAP)
   ↓
2. Search for UNREAD emails
   ↓
3. Filter by subject keywords
   ↓
4. Extract attachments from matching emails
   ↓
5. Validate file type and size
   ↓
6. Check for duplicates (SHA256 hash)
   ↓
7. Save attachments temporarily
   ↓
8. Rename files: DocumentType_Date_Sender.ext
   ↓
9. Move to appropriate folder
   ↓
10. Mark email as READ
   ↓
11. Log results and generate report
```

### Example File Naming

**Original:** `document.pdf`  
**Renamed:** `Invoices_20251219_JohnSmith.pdf`

**Components:**
- `Invoices`: Document type (from subject keyword)
- `20251219`: Email date (YYYYMMDD format)
- `JohnSmith`: Sender name (sanitized)
- `.pdf`: Original extension

## 🛡️ Security Best Practices

1. **Never Hardcode Credentials**: Use environment variables or secure vaults
2. **App Passwords**: Use app-specific passwords, not your main password
3. **File Validation**: Only allowed extensions are processed
4. **Size Limits**: Protects against large file downloads
5. **Logging**: No sensitive data logged (passwords masked)

## 🔧 Troubleshooting

### Common Issues

**Problem**: "Failed to connect to email server"
- **Solution**: Verify IMAP settings and credentials
- Check firewall/antivirus blocking port 993
- Ensure IMAP is enabled in email account settings

**Problem**: "Python script not found"
- **Solution**: Ensure folder structure is correct
- Check that Python files are in `Python/` directory relative to C# app

**Problem**: "No module named 'imaplib'"
- **Solution**: Run `pip install -r requirements.txt`

**Problem**: Duplicate files not being prevented
- **Solution**: Check `.processed_hashes.txt` file exists in Downloads folder

## 📊 Logging

Logs are written to `logs/bot.log` with the following levels:
- **INFO**: General execution flow
- **WARNING**: Non-critical issues
- **ERROR**: Failures that don't stop execution
- **CRITICAL**: Fatal errors

### Log Format
```
2025-12-19 10:30:45 - email_reader - INFO - Connected to email server
2025-12-19 10:30:46 - email_reader - INFO - Found 5 unread emails
2025-12-19 10:30:47 - attachment_handler - INFO - Extracted attachment: invoice.pdf (234.5 KB)
```

## 🧪 Testing

### Manual Testing Checklist
- [ ] Send test email with keyword in subject
- [ ] Verify attachment is downloaded
- [ ] Check file is renamed correctly
- [ ] Confirm file is in correct folder
- [ ] Verify email marked as read
- [ ] Test duplicate prevention
- [ ] Test error handling (invalid credentials)

## 🚀 Extending the Bot

### Adding New Document Types

1. Edit `config.py`:
```python
FILTER_KEYWORDS = {
    'Invoice': 'Invoices',
    'Contract': 'Contracts',  # Add new type
}

DOCUMENT_FOLDERS = {
    'Invoices': DOWNLOAD_BASE_DIR / 'Invoices',
    'Contracts': DOWNLOAD_BASE_DIR / 'Contracts',  # Add folder
}
```

2. Folders will be created automatically on first run

### Custom File Processing

Extend `document_processor.py`:
```python
def custom_processing(self, file_path):
    # Add OCR, data extraction, etc.
    pass
```

## 📝 License

This project is provided as-is for educational and enterprise use.

## 🤝 Contributing

Contributions welcome! Please follow these guidelines:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## 📞 Support

For issues and questions:
- GitHub Issues: Report bugs and feature requests
- Documentation: Check this README and inline code comments

## 🎓 Best Practices Implemented

- ✅ Modular architecture (separation of concerns)
- ✅ Comprehensive error handling
- ✅ Detailed logging
- ✅ Configuration externalization
- ✅ Duplicate prevention
- ✅ File validation
- ✅ Clean code with comments
- ✅ Type hints (Python)
- ✅ Resource cleanup (connections, processes)
- ✅ User-friendly UI
- ✅ Cross-platform considerations

## 🔄 Version History

**v1.0.0** (2025-12-19)
- Initial release
- Python backend with IMAP email processing
- C# WinForms desktop UI
- Automatic document organization
- Duplicate prevention
- Comprehensive logging

---

**Built with ❤️ for Enterprise Automation**
