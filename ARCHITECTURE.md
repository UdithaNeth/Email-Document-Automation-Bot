# Architecture Documentation

## System Overview

The Email & Document Automation Bot is a two-tier RPA solution:
- **Backend**: Python automation engine (core processing)
- **Frontend**: C# WinForms UI (user interface and process management)

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    C# WinForms UI Layer                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Run Button   │  │ Stop Button  │  │ View Logs    │     │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘     │
│         │                  │                  │              │
│         └──────────────────┼──────────────────┘              │
│                            ▼                                 │
│                  ┌──────────────────┐                       │
│                  │ AutomationEngine │                       │
│                  │  Process Manager │                       │
│                  └────────┬─────────┘                       │
└───────────────────────────┼───────────────────────────────┘
                            │ Process.Start()
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  Python Automation Layer                     │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │                    main.py                          │    │
│  │              (Orchestration Logic)                  │    │
│  └───┬────────────────────┬───────────────────┬───────┘    │
│      │                    │                   │             │
│      ▼                    ▼                   ▼             │
│  ┌─────────────┐   ┌──────────────┐   ┌──────────────┐   │
│  │email_reader │   │  attachment  │   │  document    │   │
│  │    .py      │   │  _handler.py │   │ _processor.py│   │
│  └──────┬──────┘   └──────┬───────┘   └──────┬───────┘   │
│         │                  │                   │            │
│         │                  │                   │            │
│  ┌──────▼──────────────────▼───────────────────▼────────┐ │
│  │                    config.py                          │ │
│  │        (Configuration & Environment Variables)        │ │
│  └────────────────────────────────────────────────────── │ │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    External Systems                          │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   │
│  │ Email Server │   │ File System  │   │  Log Files   │   │
│  │    (IMAP)    │   │  (Storage)   │   │   (Audit)    │   │
│  └──────────────┘   └──────────────┘   └──────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. C# UI Layer

#### MainForm.cs
- **Responsibility**: User interface and interaction
- **Key Methods**:
  - `btnRunAutomation_Click()`: Initiates automation
  - `btnStopAutomation_Click()`: Terminates automation
  - `btnViewLogs_Click()`: Opens log file
  - Event handlers for output display

#### AutomationEngine.cs
- **Responsibility**: Python process lifecycle management
- **Key Methods**:
  - `StartAutomationAsync()`: Spawns Python process
  - `StopAutomation()`: Terminates Python process
  - `FindPythonExecutable()`: Locates Python installation
- **Features**:
  - Stdout/stderr capture
  - Real-time output streaming
  - Process monitoring
  - Graceful shutdown

### 2. Python Automation Layer

#### main.py
- **Responsibility**: Orchestration and workflow coordination
- **Key Functions**:
  - `setup_logging()`: Configure log handlers
  - `validate_configuration()`: Pre-flight checks
  - `process_emails()`: Main automation workflow
  - `main()`: Entry point with error handling

**Workflow Steps**:
1. Initialize components
2. Connect to email server
3. Fetch unread emails
4. Process attachments
5. Organize documents
6. Mark emails as read
7. Generate summary

#### email_reader.py
- **Responsibility**: Email connection and retrieval
- **Class**: `EmailReader`
- **Key Methods**:
  - `connect()`: IMAP connection establishment
  - `get_unread_emails()`: Fetch and filter emails
  - `mark_as_read()`: Update email status
  - `get_email_metadata()`: Extract email info
- **Features**:
  - IMAP4_SSL connection
  - Subject decoding
  - Keyword filtering

#### attachment_handler.py
- **Responsibility**: Attachment extraction and validation
- **Class**: `AttachmentHandler`
- **Key Methods**:
  - `extract_attachments()`: Parse email parts
  - `save_attachment()`: Write files to disk
  - `_calculate_hash()`: Generate SHA256 hash
  - `_is_valid_extension()`: Validate file type
  - `_is_valid_size()`: Check size limits
- **Features**:
  - Duplicate prevention (hash-based)
  - File type validation
  - Size limit enforcement
  - Automatic filename collision handling

#### document_processor.py
- **Responsibility**: Document organization and naming
- **Class**: `DocumentProcessor`
- **Key Methods**:
  - `determine_document_type()`: Classify by keyword
  - `generate_new_filename()`: Create meaningful names
  - `organize_document()`: Move to appropriate folder
  - `extract_sender_name()`: Parse email sender
- **Features**:
  - Intelligent categorization
  - Sanitized filenames
  - Date parsing
  - Folder organization

#### config.py
- **Responsibility**: Centralized configuration
- **Configuration Sections**:
  - Email settings (host, port, credentials)
  - Filter keywords
  - Document folders
  - File validation rules
  - Logging configuration
- **Features**:
  - Environment variable support
  - Auto-directory creation
  - Path management

## Data Flow

### Email Processing Flow

```
1. User clicks "Run" → C# UI
2. UI spawns Python process → AutomationEngine
3. Python reads config → config.py
4. Connect to email → EmailReader
5. Fetch unread emails → IMAP Server
6. Filter by keywords → EmailReader
7. For each email:
   a. Extract attachments → AttachmentHandler
   b. Validate file (type, size, hash)
   c. Save temporarily
   d. Determine doc type → DocumentProcessor
   e. Generate new filename
   f. Move to target folder
   g. Mark email as read
8. Log results → logs/bot.log
9. Return status → C# UI
```

## Security Architecture

### Credential Management
- Environment variables (primary method)
- No hardcoded credentials
- Secure storage recommendations

### File Validation
- Extension whitelist
- Size limit enforcement
- Hash-based duplicate detection

### Error Handling
- Try-catch at every level
- Graceful degradation
- Comprehensive logging

## Extensibility Points

### Adding Document Types
1. Update `FILTER_KEYWORDS` in `config.py`
2. Add folder to `DOCUMENT_FOLDERS`
3. No code changes required

### Custom Processing
1. Extend `DocumentProcessor` class
2. Override `process_attachment()` method
3. Add custom logic (OCR, data extraction, etc.)

### Alternative Email Protocols
1. Implement new reader class
2. Follow `EmailReader` interface
3. Update `main.py` initialization

### Additional UI Features
1. Extend `MainForm.cs`
2. Add new buttons/controls
3. Wire to `AutomationEngine` methods

## Performance Considerations

### Optimization Strategies
- **Batch Processing**: Process multiple emails in sequence
- **Connection Reuse**: Single IMAP connection per session
- **Lazy Loading**: Load attachments only when needed
- **Hash Caching**: In-memory hash set for duplicate checks

### Scalability Limits
- **Email Volume**: Designed for hundreds of emails per run
- **Attachment Size**: 25MB default limit (configurable)
- **Concurrent Processing**: Single-threaded (by design)

### Resource Usage
- **Memory**: Grows with attachment count
- **Disk**: Depends on attachment sizes
- **Network**: IMAP bandwidth requirements

## Monitoring & Observability

### Logging Strategy
- **File Logging**: `logs/bot.log` (persistent)
- **Console Logging**: Real-time feedback
- **Log Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Rotation**: Manual (extend for production)

### Metrics to Track
- Emails processed per run
- Attachments downloaded
- Processing time
- Error rates
- Duplicate detections

## Deployment Options

### Standalone Desktop
- User runs manually via UI
- Suitable for ad-hoc processing

### Scheduled Automation
- Windows Task Scheduler
- Run Python script directly
- Logs capture results

### Service Mode (Future)
- Windows Service wrapper
- Continuous monitoring
- Auto-retry on failure

## Technology Stack

### Backend
- **Language**: Python 3.8+
- **Libraries**: 
  - `imaplib` (IMAP client)
  - `email` (message parsing)
  - `pathlib` (file operations)
  - `logging` (audit trail)
  - `hashlib` (duplicate detection)

### Frontend
- **Framework**: .NET 6.0 WinForms
- **Language**: C# 10
- **UI Pattern**: Event-driven
- **Process Management**: System.Diagnostics

## Design Patterns Used

1. **Module Pattern**: Separation of concerns across files
2. **Facade Pattern**: `main.py` provides simple interface
3. **Strategy Pattern**: Configurable document classification
4. **Observer Pattern**: Event-based UI updates
5. **Singleton Pattern**: Single configuration instance

## Future Enhancements

### Planned Features
- [ ] Multi-threading for parallel processing
- [ ] Database for tracking processed emails
- [ ] Web UI (ASP.NET Core)
- [ ] Cloud storage integration (Azure Blob, AWS S3)
- [ ] OCR for PDF text extraction
- [ ] Machine learning for smart classification
- [ ] Email sending capabilities
- [ ] Webhook notifications
- [ ] Docker containerization

### Code Improvements
- [ ] Unit tests (pytest, NUnit)
- [ ] Integration tests
- [ ] CI/CD pipeline
- [ ] Code coverage reports
- [ ] Performance profiling
