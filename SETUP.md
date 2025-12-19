# Setup Instructions

## Complete Installation Guide

### Step 1: Install Python

1. Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Verify installation:
   ```powershell
   python --version
   ```

### Step 2: Install .NET SDK

1. Download .NET 6.0 SDK from [dotnet.microsoft.com](https://dotnet.microsoft.com/download)
2. Run the installer
3. Verify installation:
   ```powershell
   dotnet --version
   ```

### Step 3: Install Python Dependencies

```powershell
cd "E:\Projects\Email & Document Automation Bot\Python"
pip install -r requirements.txt
```

### Step 4: Configure Email Credentials

#### For Gmail:

1. **Enable IMAP**:
   - Open Gmail → Settings (gear icon) → See all settings
   - Go to "Forwarding and POP/IMAP" tab
   - Enable IMAP
   - Click "Save Changes"

2. **Generate App Password** (if 2-Step Verification is enabled):
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Under "Signing in to Google", select "App passwords"
   - Select "Mail" and your device type
   - Click "Generate"
   - Copy the 16-character password

3. **Set Environment Variables**:
   ```powershell
   # In PowerShell
   $env:EMAIL_HOST = "imap.gmail.com"
   $env:EMAIL_PORT = "993"
   $env:EMAIL_USER = "your_email@gmail.com"
   $env:EMAIL_PASSWORD = "your_16_char_app_password"
   ```

#### For Outlook/Office 365:

```powershell
$env:EMAIL_HOST = "outlook.office365.com"
$env:EMAIL_PORT = "993"
$env:EMAIL_USER = "your_email@outlook.com"
$env:EMAIL_PASSWORD = "your_password"
```

### Step 5: Test Python Script

```powershell
cd "E:\Projects\Email & Document Automation Bot\Python"
python main.py
```

**Expected Output**:
```
INFO - Connecting to imap.gmail.com:993
INFO - Email connection established successfully
INFO - Found X unread emails
INFO - Processing complete
SUCCESS: Automation completed successfully
```

### Step 6: Build and Run C# Application

```powershell
cd "E:\Projects\Email & Document Automation Bot\DotNet\EmailAutomationBot"
dotnet build
dotnet run
```

The WinForms application window should open.

## Testing the Complete System

### Test Scenario 1: Invoice Processing

1. **Send test email**:
   - To: Your configured email
   - Subject: "Invoice for December 2025"
   - Attachment: sample.pdf

2. **Run automation**:
   - Open the WinForms app
   - Click "Run Automation"
   - Watch output console

3. **Verify results**:
   - Check `Downloads/Invoices/` folder
   - File should be renamed: `Invoices_20251219_SenderName.pdf`
   - Email should be marked as read
   - Check `logs/bot.log` for details

### Test Scenario 2: Resume Processing

1. **Send test email**:
   - Subject: "Resume - John Smith"
   - Attachment: resume.docx

2. **Run automation**

3. **Verify**:
   - File in `Downloads/Resumes/`
   - Renamed: `Resumes_20251219_SenderName.docx`

## Permanent Environment Variable Setup

To avoid setting environment variables every time:

### Windows (Permanent):

1. Search for "Environment Variables" in Windows
2. Click "Edit system environment variables"
3. Click "Environment Variables" button
4. Under "User variables", click "New"
5. Add each variable:
   - Variable name: `EMAIL_HOST`
   - Variable value: `imap.gmail.com`
   - Repeat for EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

### Using .env file (Alternative):

1. Create `.env` file in Python directory:
   ```powershell
   cd "E:\Projects\Email & Document Automation Bot\Python"
   Copy-Item .env.example .env
   ```

2. Edit `.env` with your credentials:
   ```
   EMAIL_HOST=imap.gmail.com
   EMAIL_PORT=993
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

3. Update `config.py` to load .env:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

## Scheduling Automation (Optional)

### Windows Task Scheduler:

1. Open Task Scheduler
2. Create Basic Task
3. Name: "Email Document Automation"
4. Trigger: Daily at specific time
5. Action: Start a program
   - Program: `python`
   - Arguments: `"E:\Projects\Email & Document Automation Bot\Python\main.py"`
   - Start in: `E:\Projects\Email & Document Automation Bot\Python`
6. Finish and test

## Troubleshooting

### Issue: "Python not found"
**Solution**: Add Python to PATH or use full path:
```powershell
C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe
```

### Issue: "Module not found"
**Solution**: Install dependencies:
```powershell
pip install -r requirements.txt
```

### Issue: "Authentication failed"
**Solutions**:
- Verify email and password are correct
- Check IMAP is enabled
- Use app password (not regular password) if 2FA enabled
- Check firewall/antivirus isn't blocking port 993

### Issue: "Permission denied" when creating folders
**Solution**: Run as administrator or check folder permissions

### Issue: C# app can't find Python script
**Solution**: Check folder structure matches:
```
Email & Document Automation Bot/
├── Python/
│   └── main.py
└── DotNet/
    └── EmailAutomationBot/
```

## Customization

### Change Document Categories:

Edit `Python/config.py`:
```python
FILTER_KEYWORDS = {
    'Invoice': 'Invoices',
    'Contract': 'Contracts',    # Add new
    'Agreement': 'Contracts',    # Add new
    'Resume': 'Resumes',
    'Report': 'Reports',
}

DOCUMENT_FOLDERS = {
    'Invoices': DOWNLOAD_BASE_DIR / 'Invoices',
    'Contracts': DOWNLOAD_BASE_DIR / 'Contracts',    # Add new
    'Resumes': DOWNLOAD_BASE_DIR / 'Resumes',
    'Reports': DOWNLOAD_BASE_DIR / 'Reports',
    'Others': DOWNLOAD_BASE_DIR / 'Others'
}
```

### Change File Size Limit:

Edit `Python/config.py`:
```python
MAX_ATTACHMENT_SIZE_MB = 50  # Increase to 50 MB
```

### Add More File Types:

Edit `Python/config.py`:
```python
ALLOWED_EXTENSIONS = [
    '.pdf', '.docx', '.doc', 
    '.xlsx', '.xls', '.txt',
    '.png', '.jpg', '.jpeg',
    '.zip', '.csv', '.pptx'  # Add more
]
```

## Next Steps

1. ✅ Complete setup
2. ✅ Test with sample emails
3. ✅ Customize keywords and folders
4. ✅ Schedule automation (optional)
5. ✅ Monitor logs for issues
6. ✅ Extend functionality as needed

## Support

For issues or questions:
- Check `logs/bot.log` for detailed error messages
- Review ARCHITECTURE.md for technical details
- Refer to README.md for comprehensive documentation

---

**Setup complete! You're ready to automate email document processing.**
