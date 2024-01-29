import streamlit as st
import requests

st.title('Feelings Analyzer')
input_text = st.text_area('Write about your feelings..', '')
if st.button('Submit'):
    response = requests.get(f"http://localhost:8000/predict?text={input_text}")
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.write(f"Prediction: {prediction}")
    else:
        st.write("Error in prediction")
