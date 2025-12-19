# Quick Build and Run Script for C# Application
# Run this from PowerShell in the project root

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Email & Document Automation Bot" -ForegroundColor Cyan
Write-Host "C# Desktop UI - Build & Run" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to C# project directory
$projectPath = Join-Path $PSScriptRoot "DotNet\EmailAutomationBot"
Set-Location $projectPath

Write-Host "Building C# project..." -ForegroundColor Yellow
dotnet build

if ($LASTEXITCODE -eq 0) {
    Write-Host "Build successful!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Starting application..." -ForegroundColor Yellow
    dotnet run
} else {
    Write-Host "Build failed! Please check for errors." -ForegroundColor Red
    exit 1
}
