#!/bin/bash
echo "Loading..."
cd Stress Detection
# Run uvicorn in the background and save its process ID
uvicorn api:app --reload &
uvicorn_pid=$!
# Run streamlit in the background and save its process ID
streamlit run main.py &
streamlit_pid=$!
# Wait for both processes to finish
wait $uvicorn_pid $streamlit_pid
