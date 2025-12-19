# Quick Test Script for Python Automation
# Run this from PowerShell in the project root

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Email & Document Automation Bot" -ForegroundColor Cyan
Write-Host "Python Backend - Environment Check & Run" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to Python directory
$pythonPath = Join-Path $PSScriptRoot "Python"
Set-Location $pythonPath

Write-Host "Step 1: Running environment check..." -ForegroundColor Yellow
python test_environment.py

Write-Host ""
$response = Read-Host "Do you want to run the automation now? (y/n)"

if ($response -eq "y" -or $response -eq "Y") {
    Write-Host ""
    Write-Host "Starting automation..." -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    python main.py
    
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "Automation complete! Check logs folder for details." -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "Automation cancelled. Configure your credentials and try again." -ForegroundColor Yellow
}
