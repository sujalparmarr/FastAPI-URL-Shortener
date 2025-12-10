import streamlit as st
import requests

API_URL = "http://localhost:8000/shorten"

st.set_page_config(page_title="URL Shortener", page_icon="🔗")

st.title("🔗 Simple URL Shortener (FastAPI + Streamlit)")

st.write("Enter a long URL and get a short version instantly!")

long_url = st.text_input("Enter URL to shorten:")

if st.button("Shorten URL"):
    if long_url:
        with st.spinner("Generating short URL..."):
            response = requests.post(API_URL, json={"long_url": long_url})
            
            if response.status_code == 200:
                data = response.json()
                
                st.success("Short URL Generated!")
                st.write("### 🔗 Short URL:")
                st.markdown(f"[{data['short_url']}]({data['short_url']})")
            else:
                st.error("Failed to shorten URL. Check if the API is running.")
    else:
        st.warning("Please enter a valid URL.")

