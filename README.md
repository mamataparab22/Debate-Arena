
# Debate Arena

Debate Arena is a full-stack application for interacting with Large Language Models (LLMs) via a FastAPI backend and a Streamlit frontend. It supports integration with Google Gemini (Generative AI) and can be easily extended to other LLMs.

## Features
- FastAPI backend with endpoints for text, speech, and Gemini LLM responses
- Streamlit frontend for user-friendly interaction
- Secure API key management using `.env` and `python-dotenv`
- Easy setup and extensibility

## Folder Structure
```
Debate-Arena/
│
├── README.md                # Project overview
├── backend/                 # Backend logic and API
│   ├── main.py              # Main backend application
│   ├── README.md            # Backend documentation
│   └── integration/
│       ├── llm_connector.py # LLM integration logic
│       ├── google_gemini_llm.py # Gemini LLM integration
│       └── README.md        # Integration documentation
├── frontend/                # Frontend application
│   ├── app.py               # Main frontend application (Streamlit)
│   └── README.md            # Frontend documentation
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API keys)
├── .gitignore               # Files to ignore in git
├── run_all.ps1              # PowerShell script to run backend and frontend together
```

## Setup & Usage

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_actual_api_key
```

### 3. Run Backend & Frontend
Use the PowerShell script to start both:
```powershell
./run_all.ps1
```
Or run manually:
```powershell
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000
cd ../frontend
streamlit run app.py
```

### 4. Interact with the App
- Open the Streamlit frontend in your browser (URL shown in terminal)
- Enter a prompt and get LLM responses powered by Gemini

## Extending
- Add new LLM integrations in `backend/integration/`
- Update frontend UI in `frontend/app.py`

## Security
- API keys are loaded from `.env` and never hardcoded
- `.env` is git-ignored by default

## License
MIT
