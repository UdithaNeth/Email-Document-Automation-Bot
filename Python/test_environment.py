# Test script to verify Python environment and configuration

import sys
import os
from pathlib import Path

print("=" * 60)
print("Email & Document Automation Bot - Environment Check")
print("=" * 60)

# Check Python version
print(f"\n✓ Python Version: {sys.version}")

# Check required modules
required_modules = ['imaplib', 'email', 'logging', 'pathlib', 'hashlib']
print("\nChecking required modules:")
for module in required_modules:
    try:
        __import__(module)
        print(f"  ✓ {module}")
    except ImportError:
        print(f"  ✗ {module} - MISSING!")

# Check configuration
print("\nChecking configuration:")
try:
    import config
    print(f"  ✓ config.py imported successfully")
    
    # Check email settings
    if config.EMAIL_USER == 'your_email@example.com':
        print("  ⚠ EMAIL_USER not configured (using default)")
    else:
        print(f"  ✓ EMAIL_USER: {config.EMAIL_USER}")
    
    if config.EMAIL_PASSWORD == 'your_password':
        print("  ⚠ EMAIL_PASSWORD not configured (using default)")
    else:
        print(f"  ✓ EMAIL_PASSWORD: {'*' * len(config.EMAIL_PASSWORD)}")
    
    print(f"  ✓ EMAIL_HOST: {config.EMAIL_HOST}")
    print(f"  ✓ EMAIL_PORT: {config.EMAIL_PORT}")
    
except Exception as e:
    print(f"  ✗ Error loading config: {e}")

# Check directories
print("\nChecking directories:")
base_dir = Path(__file__).parent.parent
dirs_to_check = [
    base_dir / 'logs',
    base_dir / 'Downloads',
    base_dir / 'Downloads' / 'Invoices',
    base_dir / 'Downloads' / 'Resumes',
    base_dir / 'Downloads' / 'Reports',
]

for dir_path in dirs_to_check:
    if dir_path.exists():
        print(f"  ✓ {dir_path.name}/")
    else:
        print(f"  ⚠ {dir_path.name}/ - Will be created on first run")

# Summary
print("\n" + "=" * 60)
print("Environment Check Complete")
print("=" * 60)
print("\nNext steps:")
print("1. Set EMAIL_USER and EMAIL_PASSWORD environment variables")
print("2. Run: python main.py")
print("3. Or launch the C# desktop UI")
print("\nFor detailed setup instructions, see SETUP.md")
print("=" * 60)
