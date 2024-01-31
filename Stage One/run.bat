echo off
echo Loading...
.\stage-one\Scripts\activate
uvicorn api:app --reload
streamlit run main.py