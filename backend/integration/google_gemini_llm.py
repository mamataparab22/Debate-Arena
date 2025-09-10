
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # Load environment variables from a .env file

def query_gemini_llm(prompt: str) -> str:
    """
    Query Google Gemini LLM using the official API.
    Args:
        prompt (str): The prompt to send to Gemini.
    Returns:
        str: The response from Gemini.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,  # Pass prompt as a string
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        ),
    )
    # Extract the generated text
    return response.candidates[0].content.parts[0].text