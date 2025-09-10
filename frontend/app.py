import streamlit as st
import requests

# Set page configuration, title, and welcome message once at the top
st.set_page_config(page_title="Debate Arena", page_icon="🗣️", layout="centered")
st.title("Debate Arena 🗣️")
st.write("Welcome to the Debate Arena Streamlit app!")

# Initialize session state variables if they don't exist
if "llm_response" not in st.session_state:
    st.session_state.llm_response = ""
if "llm_error" not in st.session_state:
    st.session_state.llm_error = ""

# Create a single form to handle user input and submission
with st.form(key="llm_form"):
    prompt = st.text_area(
        "Enter your debate topic or a prompt for the LLM:",
        "Should we invest more in space exploration?",
        height=100
    )
    submitted = st.form_submit_button("Start Debate")

    # If the form is submitted, make the API call
    if submitted:
        with st.spinner("Waiting for response..."):
            try:
                # Assuming a local API endpoint is running at this address
                url = "http://localhost:8000/llm/gemini"
                response = requests.get(url, params={"prompt": prompt})

                if response.status_code == 200:
                    st.session_state.llm_response = response.json().get("response", "No response received.")
                    st.session_state.llm_error = ""
                else:
                    st.session_state.llm_response = ""
                    st.session_state.llm_error = f"Error: {response.status_code} - {response.text}"
            except requests.exceptions.RequestException as e:
                st.session_state.llm_response = ""
                st.session_state.llm_error = f"Connection error: {e}"

# Display the LLM response or any errors
if st.session_state.llm_response:
    st.subheader("Debate Output")
    st.success(st.session_state.llm_response)
if st.session_state.llm_error:
    st.error(st.session_state.llm_error)
