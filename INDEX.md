# 📚 Documentation Index

Welcome to the Email & Document Automation Bot! This index will guide you to the right documentation.

## 🎯 I Want To...

### Get Started Quickly
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Visual guide with diagrams and examples
- **[QUICKSTART.md](QUICKSTART.md)** - Minimal setup for experienced developers

### Install Step-by-Step
- **[SETUP.md](SETUP.md)** - Detailed installation and configuration guide
- Covers: Python setup, .NET setup, email configuration, testing

### Understand the System
- **[README.md](README.md)** - Complete project documentation
- Covers: Features, usage, configuration, troubleshooting
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Technical architecture and design
- Covers: Components, data flow, extensibility, patterns

### See What's Included
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project overview
- Covers: File structure, features implemented, status

## 📂 File Guide

### Documentation Files

| File | Purpose | When to Read |
|------|---------|--------------|
| **GETTING_STARTED.md** | Visual quick start guide | First time setup with examples |
| **QUICKSTART.md** | Minimal setup steps | You know what you're doing |
| **SETUP.md** | Detailed installation | Step-by-step configuration |
| **README.md** | Full documentation | Complete reference |
| **ARCHITECTURE.md** | Technical design | Understanding internals |
| **PROJECT_SUMMARY.md** | Project overview | What's implemented |
| **INDEX.md** | This file | Finding the right doc |

### Python Files

| File | Purpose |
|------|---------|
| `main.py` | Entry point - orchestrates entire workflow |
| `config.py` | Configuration settings and environment variables |
| `email_reader.py` | IMAP email connection and retrieval |
| `attachment_handler.py` | Download, validate, and save attachments |
| `document_processor.py` | Rename and organize documents |
| `test_environment.py` | Verify Python setup |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment variable template |

### C# Files

| File | Purpose |
|------|---------|
| `Program.cs` | Application entry point |
| `MainForm.cs` | UI logic and event handlers |
| `MainForm.Designer.cs` | UI designer-generated code |
| `AutomationEngine.cs` | Python process management |
| `EmailAutomationBot.csproj` | Project configuration |

### Helper Scripts

| File | Purpose |
|------|---------|
| `run_python.ps1` | Quick test Python backend |
| `run_ui.ps1` | Quick launch desktop UI |

## 🎓 Learning Path

### Beginner - First Time Setup
1. Read **GETTING_STARTED.md** (with visual guides)
2. Follow **SETUP.md** (step-by-step)
3. Run test with `run_python.ps1`
4. Launch UI with `run_ui.ps1`

### Intermediate - Configuration & Customization
1. Review **README.md** (features and options)
2. Edit `Python/config.py` (customize keywords)
3. Test with different document types
4. Schedule automation (Task Scheduler)

### Advanced - Extension & Development
1. Study **ARCHITECTURE.md** (design patterns)
2. Review Python modules (modular structure)
3. Extend `document_processor.py` (custom logic)
4. Add new features (cloud storage, OCR, etc.)

## 🔍 Common Questions

### Setup Questions
**Q: How do I install Python?**  
A: See **SETUP.md** → "Step 1: Install Python"

**Q: How do I configure Gmail?**  
A: See **SETUP.md** → "Step 4: Configure Email Credentials" → "For Gmail"

**Q: Dependencies not installing?**  
A: Run `pip install -r requirements.txt` from Python folder

### Usage Questions
**Q: How do I run the bot?**  
A: See **GETTING_STARTED.md** → "3-Step Quick Start"

**Q: How do I add new document types?**  
A: See **README.md** → "Extending the Bot" → "Adding New Document Types"

**Q: Where are my files saved?**  
A: `Downloads/` folder with subfolders (Invoices, Resumes, Reports)

### Technical Questions
**Q: How does the file renaming work?**  
A: See **ARCHITECTURE.md** → "document_processor.py" section

**Q: How are duplicates prevented?**  
A: See **ARCHITECTURE.md** → "attachment_handler.py" → SHA256 hash checking

**Q: Can I extend this bot?**  
A: Yes! See **ARCHITECTURE.md** → "Extensibility Points"

### Troubleshooting
**Q: "Authentication failed" error?**  
A: See **SETUP.md** → "Troubleshooting" section

**Q: Python script not found?**  
A: Verify folder structure matches **PROJECT_SUMMARY.md**

**Q: UI won't start?**  
A: Install .NET 6.0 SDK (see **SETUP.md** → "Step 2")

## 🎯 Quick Reference

### Configuration Locations
- **Email Settings**: `Python/config.py` or environment variables
- **Document Keywords**: `Python/config.py` → `FILTER_KEYWORDS`
- **File Types**: `Python/config.py` → `ALLOWED_EXTENSIONS`
- **Folder Paths**: `Python/config.py` → `DOCUMENT_FOLDERS`

### Important Paths
- **Logs**: `logs/bot.log`
- **Downloads**: `Downloads/` (with subfolders)
- **Python Backend**: `Python/`
- **C# Frontend**: `DotNet/EmailAutomationBot/`

### Key Commands
```powershell
# Test Python environment
cd Python
python test_environment.py

# Run Python automation
python main.py

# Build and run C# UI
cd DotNet\EmailAutomationBot
dotnet run

# Quick launch scripts
.\run_python.ps1
.\run_ui.ps1
```

## 📊 Documentation Map

```
Documentation Structure
│
├── Quick Start (Visual)
│   └── GETTING_STARTED.md ← Start here!
│
├── Installation
│   ├── QUICKSTART.md (minimal)
│   └── SETUP.md (detailed)
│
├── Reference
│   ├── README.md (complete)
│   └── PROJECT_SUMMARY.md (overview)
│
├── Technical
│   └── ARCHITECTURE.md (design)
│
└── Navigation
    └── INDEX.md (this file)
```

## 🎯 By Role

### End User
1. **GETTING_STARTED.md** - Understand what it does
2. **SETUP.md** - Install and configure
3. **README.md** - Reference for daily use

### Developer
1. **ARCHITECTURE.md** - Understand the design
2. **README.md** - Features and capabilities
3. Source code files - Implementation details

### System Administrator
1. **SETUP.md** - Installation requirements
2. **README.md** - Scheduling and maintenance
3. **ARCHITECTURE.md** - Deployment options

## ✅ Getting Started Checklist

- [ ] Read GETTING_STARTED.md
- [ ] Install Python 3.8+
- [ ] Install .NET 6.0 SDK
- [ ] Run `pip install -r requirements.txt`
- [ ] Configure email credentials
- [ ] Test with `python test_environment.py`
- [ ] Send test email
- [ ] Run automation
- [ ] Verify files organized correctly
- [ ] Check logs

## 🎉 Ready to Automate!

Choose your starting point:
- **New User?** → Start with [GETTING_STARTED.md](GETTING_STARTED.md)
- **Quick Setup?** → Jump to [QUICKSTART.md](QUICKSTART.md)
- **Need Details?** → Read [SETUP.md](SETUP.md)
- **Want Everything?** → See [README.md](README.md)

---

**Need help finding something? All docs are in the root folder!**
