# Getting Started - Visual Guide

## 🎯 What This Bot Does

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Unread    │         │   Filter &   │         │  Organized  │
│   Emails    │  ──→    │   Download   │  ──→    │  Documents  │
│             │         │  Attachments │         │             │
└─────────────┘         └──────────────┘         └─────────────┘
     IMAP                  Validation                Folders
```

## 📧 Example Workflow

### Input: Email Received
```
From: john.smith@company.com
Subject: Invoice for December Services
Attachment: document.pdf (245 KB)
Status: UNREAD
```

### Processing: Bot Actions
```
1. ✓ Connect to email server
2. ✓ Find unread emails
3. ✓ Match keyword "Invoice" in subject
4. ✓ Download attachment (245 KB)
5. ✓ Validate: PDF format, size OK
6. ✓ Check for duplicates (hash)
7. ✓ Rename: document.pdf → Invoices_20251219_JohnSmith.pdf
8. ✓ Move to: Downloads/Invoices/
9. ✓ Mark email as READ
```

### Output: Organized Files
```
Downloads/
└── Invoices/
    └── Invoices_20251219_JohnSmith.pdf  ✓ Saved!
```

## 🖥️ Desktop Application UI

```
┌────────────────────────────────────────────────────────────┐
│  Email & Document Automation Bot                    [_][□][X]│
├────────────────────────────────────────────────────────────┤
│                                                              │
│  [▶ Run Automation] [■ Stop] [📄 View Logs] [🗑 Clear]      │
│                                                              │
│  Status: Ready                                               │
│                                                              │
├────────────────────────────────────────────────────────────┤
│  Output Console:                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ === Email & Document Automation Bot ===              │  │
│  │ Configure your email credentials...                  │  │
│  │                                                       │  │
│  │ Click 'Run Automation' to start...                   │  │
│  │                                                       │  │
│  │                                                       │  │
│  │                                                       │  │
│  │                                                       │  │
│  │                                                       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
├────────────────────────────────────────────────────────────┤
│  Email & Document Automation Bot v1.0                       │
└────────────────────────────────────────────────────────────┘
```

## 📁 Project File Structure

```
📦 Email & Document Automation Bot
┣ 📂 Python                      ← Backend (Automation Logic)
┃ ┣ 📜 main.py                   ← Start here
┃ ┣ 📜 config.py                 ← Configuration
┃ ┣ 📜 email_reader.py           ← Email connection
┃ ┣ 📜 attachment_handler.py     ← File processing
┃ ┣ 📜 document_processor.py     ← Organization
┃ ┣ 📜 test_environment.py       ← Check setup
┃ ┣ 📜 requirements.txt          ← Dependencies
┃ ┗ 📜 .env.example              ← Config template
┃
┣ 📂 DotNet                      ← Frontend (Desktop UI)
┃ ┗ 📂 EmailAutomationBot
┃   ┣ 📜 Program.cs              ← Entry point
┃   ┣ 📜 MainForm.cs             ← UI logic
┃   ┣ 📜 AutomationEngine.cs     ← Process manager
┃   ┗ 📜 EmailAutomationBot.csproj
┃
┣ 📂 Downloads                   ← Generated folders
┃ ┣ 📂 Invoices
┃ ┣ 📂 Resumes
┃ ┣ 📂 Reports
┃ ┗ 📂 Others
┃
┣ 📂 logs                        ← Log files
┃ ┗ 📜 bot.log
┃
┣ 📜 README.md                   ← Main docs
┣ 📜 QUICKSTART.md               ← Fast setup
┣ 📜 SETUP.md                    ← Detailed guide
┣ 📜 ARCHITECTURE.md             ← Technical docs
┣ 📜 PROJECT_SUMMARY.md          ← Overview
┣ 📜 run_python.ps1              ← Quick test
┗ 📜 run_ui.ps1                  ← Quick UI run
```

## 🚀 3-Step Quick Start

### Step 1: Install Python Dependencies
```powershell
cd Python
pip install -r requirements.txt
```

### Step 2: Set Email Credentials
```powershell
# PowerShell
$env:EMAIL_HOST = "imap.gmail.com"
$env:EMAIL_USER = "your_email@gmail.com"
$env:EMAIL_PASSWORD = "your_app_password"
```

### Step 3: Run!

**Option A - Desktop UI (Recommended):**
```powershell
.\run_ui.ps1
# OR
cd DotNet\EmailAutomationBot
dotnet run
```

**Option B - Python Only:**
```powershell
.\run_python.ps1
# OR
cd Python
python main.py
```

## 🎨 Visual Example: File Naming

```
Before Processing:
┌──────────────────┐
│  Email Inbox     │
│                  │
│  📧 Subject:     │
│     "Invoice"    │
│                  │
│  📎 Attachment:  │
│     document.pdf │
└──────────────────┘

After Processing:
┌────────────────────────────────────────┐
│  Downloads/Invoices/                   │
│                                        │
│  📄 Invoices_20251219_JohnSmith.pdf   │
│     │         │         │              │
│     │         │         └─ Sender      │
│     │         └─────────── Date        │
│     └───────────────────── Type        │
└────────────────────────────────────────┘
```

## 📋 Email Setup Guide (Gmail)

### 1. Enable IMAP
```
Gmail Settings → See all settings → Forwarding and POP/IMAP
[✓] Enable IMAP
[Save Changes]
```

### 2. Generate App Password (if 2FA enabled)
```
Google Account → Security → 2-Step Verification → App passwords
Select: Mail + Your device
[Generate] → Copy 16-character password
```

### 3. Use in Configuration
```powershell
$env:EMAIL_USER = "your_email@gmail.com"
$env:EMAIL_PASSWORD = "abcd efgh ijkl mnop"  # 16-char app password
```

## 🔍 What Gets Processed?

```
┌─────────────────────────────────────────────┐
│  Emails with Keywords in Subject:           │
├─────────────────────────────────────────────┤
│  ✓ "Invoice"     → Invoices/               │
│  ✓ "Bill"        → Invoices/               │
│  ✓ "Resume"      → Resumes/                │
│  ✓ "CV"          → Resumes/                │
│  ✓ "Report"      → Reports/                │
│  ✓ "Analysis"    → Reports/                │
│  ✗ Others        → Ignored (not processed)  │
└─────────────────────────────────────────────┘
```

## 🛡️ File Validation

```
┌───────────────────────────────────────────┐
│  Allowed File Types:                      │
│  ✓ .pdf, .docx, .doc                     │
│  ✓ .xlsx, .xls                           │
│  ✓ .txt                                  │
│  ✓ .png, .jpg, .jpeg                     │
│  ✗ .exe, .zip, .bat (rejected)           │
│                                           │
│  Max Size: 25 MB                          │
│  Duplicate Check: SHA256 hash             │
└───────────────────────────────────────────┘
```

## 📊 Sample Output

### Console Log:
```
═══════════════════════════════════════════════════
Starting Email & Document Automation Bot
═══════════════════════════════════════════════════

Step 1: Initializing Email Reader
Step 2: Connecting to email server
INFO - Connected to imap.gmail.com:993
INFO - Email connection established successfully

Step 3: Fetching unread emails
INFO - Found 2 unread emails

Step 4: Initializing Attachment Handler
Step 5: Initializing Document Processor
Step 6: Processing 2 emails

Processing email from: john.smith@company.com
Subject: Invoice for December Services
INFO - Found 1 attachment(s)
INFO - Extracted attachment: invoice.pdf (234.5 KB)
INFO - Generated filename: Invoices_20251219_JohnSmith.pdf
✓ Successfully processed: Invoices_20251219_JohnSmith.pdf

═══════════════════════════════════════════════════
Processing Complete
Total attachments processed: 2
Total documents saved: 2
═══════════════════════════════════════════════════

SUCCESS: Automation completed successfully
```

## 🎯 Testing Checklist

Send yourself test emails and verify:

```
□ Email with "Invoice" in subject
  → File saved in Downloads/Invoices/
  
□ Email with "Resume" in subject
  → File saved in Downloads/Resumes/
  
□ Email with "Report" in subject
  → File saved in Downloads/Reports/
  
□ Files renamed correctly
  → Format: Type_Date_Sender.ext
  
□ Emails marked as READ
  → Check your inbox
  
□ Logs generated
  → Check logs/bot.log
  
□ Duplicate prevention works
  → Send same file twice
```

## 🎓 Need Help?

| Question | Answer |
|----------|--------|
| How to configure? | See `SETUP.md` |
| Architecture details? | See `ARCHITECTURE.md` |
| Quick setup? | See `QUICKSTART.md` |
| Full documentation? | See `README.md` |
| Can't connect? | Check email credentials & IMAP enabled |
| Module not found? | Run `pip install -r requirements.txt` |
| UI won't start? | Install .NET 6.0 SDK |

## 🚀 You're Ready!

```
┌────────────────────────────────────┐
│  Setup Complete! ✓                 │
│                                    │
│  Next: Run the automation          │
│                                    │
│  → Desktop UI: .\run_ui.ps1       │
│  → Python: .\run_python.ps1       │
│                                    │
│  Happy Automating! 🎉             │
└────────────────────────────────────┘
```

---

**Pro Tip**: Start with a test email to verify everything works before processing your actual inbox!
