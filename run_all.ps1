# Run backend
Start-Process powershell -WorkingDirectory "$(Join-Path $PSScriptRoot 'backend')" -ArgumentList "-NoExit", "-Command", "python -m uvicorn main:app --host 0.0.0.0 --port 8000"

# Run frontend
Start-Process powershell -WorkingDirectory "$(Join-Path $PSScriptRoot 'frontend')" -ArgumentList "-NoExit", "-Command", "python -m streamlit run app.py"
