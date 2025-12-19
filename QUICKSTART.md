# Quick Start Guide

## 1. Set Up Python Environment

```powershell
cd Python
pip install -r requirements.txt
```

## 2. Configure Email Credentials

### Option A: Environment Variables (Recommended)
```powershell
$env:EMAIL_HOST = "imap.gmail.com"
$env:EMAIL_USER = "your_email@gmail.com"
$env:EMAIL_PASSWORD = "your_app_password"
```

### Option B: Use .env file
```powershell
cp .env.example .env
# Edit .env with your credentials
```

## 3. Test Python Script

```powershell
cd Python
python main.py
```

Expected output:
- Connects to email server
- Fetches unread emails
- Downloads attachments
- Organizes into folders

## 4. Run Desktop UI

```powershell
cd ..\DotNet\EmailAutomationBot
dotnet build
dotnet run
```

## Gmail-Specific Setup

1. **Enable IMAP**:
   - Gmail Settings → Forwarding and POP/IMAP
   - Enable IMAP
   - Save Changes

2. **Generate App Password** (if 2FA enabled):
   - Google Account → Security
   - 2-Step Verification → App passwords
   - Select "Mail" and your device
   - Use generated 16-character password

3. **Less Secure Apps** (if no 2FA):
   - Not recommended, use App Password instead

## Testing

Send yourself a test email with:
- Subject: "Test Invoice Document"
- Attachment: Any PDF file

Run the bot and verify:
- ✅ Email is processed
- ✅ Attachment downloaded to `Downloads/Invoices/`
- ✅ File renamed: `Invoices_20251219_YourName.pdf`
- ✅ Email marked as read

## Common Issues

**"Authentication failed"**
- Double-check email and password
- Use app password if 2FA is enabled
- Verify IMAP is enabled

**"Module not found"**
- Run: `pip install -r requirements.txt`

**"Permission denied"**
- Check folder permissions
- Run as administrator if needed

## Next Steps

- Customize keywords in `config.py`
- Add more document types
- Schedule with Windows Task Scheduler
- Integrate with other systems
