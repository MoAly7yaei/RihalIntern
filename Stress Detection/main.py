import os
import streamlit as st
import requests

st.title('Stress Detector')
input_text = st.text_area('Write about your feelings..', '')
if st.button('Send'):
    api_url = f"http://{os.environ['API_HOST']}:{os.environ['API_PORT']}/predict?text={input_text}"
    response = requests.get(api_url)
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.write(f"Result: {prediction}")
    else:
        st.write("Error in prediction")
