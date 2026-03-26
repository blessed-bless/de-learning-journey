# setup.ps1 - Safe version (no Unicode)
Write-Host "Data Engineering Environment Setup" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green

# 1. Check Python
Write-Host "`n[1] Checking Python..." -ForegroundColor Yellow
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Python not found! Install Python 3.10+" -ForegroundColor Red
    exit 1
}

# 2. Create venv
Write-Host "`n[2] Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "WARNING: Venv already exists, skipping" -ForegroundColor Yellow
} else {
    python -m venv venv
    Write-Host "SUCCESS: Venv created" -ForegroundColor Green
}

# 3. Activate venv
Write-Host "`n[3] Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# 4. Install dependencies
Write-Host "`n[4] Installing dependencies..." -ForegroundColor Yellow
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
    Write-Host "SUCCESS: Dependencies installed" -ForegroundColor Green
} else {
    Write-Host "WARNING: requirements.txt not found" -ForegroundColor Yellow
}

# 5. Check environment
Write-Host "`n[5] Running environment check..." -ForegroundColor Yellow
python main.py

Write-Host "`n=== Setup Complete! ===" -ForegroundColor Green