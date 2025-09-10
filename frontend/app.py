
import streamlit as st
import requests

st.title("Debate Arena UI")
st.write("Welcome to the Debate Arena Streamlit app!")

prompt = st.text_input("Enter your prompt for LLM:", "Hello, LLM!")

if st.button("Get LLM Text Response"):
	try:
		# Change the URL if backend is running elsewhere
		url = "http://localhost:8000/llm/text"
		response = requests.get(url, params={"prompt": prompt})
		if response.status_code == 200:
			st.success(f"LLM Response: {response.json().get('response')}")
		else:
			st.error(f"Error: {response.text}")
	except Exception as e:
		st.error(f"Connection error: {e}")
