@echo off
echo Loading...
cd Stress Detection
start cmd /k uvicorn api:app --reload
start cmd /k streamlit run main.py
