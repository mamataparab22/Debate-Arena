from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from integration.google_gemini_llm import query_gemini_llm
from integration.llm_connector import query_llm, query_llm_speech

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Debate Arena Backend!"}

@app.get("/llm/text")
def get_llm_text(prompt: str = "Hello, LLM fro!"):
    response = query_llm(prompt)
    return {"response": response}

@app.get("/llm/speech")
def get_llm_speech(prompt: str = "Hello, LLM with speech!"):
    text, speech_bytes = query_llm_speech(prompt)
    return Response(
        content=speech_bytes,
        media_type="audio/wav",
        headers={"X-LLM-Text": text},
    )

# Gemini LLM endpoint
@app.get("/llm/gemini")
def get_gemini_text(prompt: str = "Hello from Gemini!"):
    response = query_gemini_llm(prompt)
    return {"response": response}
