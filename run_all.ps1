# Run backend
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python ..\backend\main.py"

# Run frontend
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python ..\frontend\app.py"
