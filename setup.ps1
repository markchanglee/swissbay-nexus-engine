python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if (!(Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "Created .env from .env.example. Add your OPENAI_API_KEY."
}

Write-Host "Setup complete."
Write-Host "Run: python nexus.py build Customer_Object"
