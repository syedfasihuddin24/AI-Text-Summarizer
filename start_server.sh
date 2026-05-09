#!/bin/bash
echo "Starting AI Text Summarizer..."
echo "Server will run at: http://127.0.0.1:8000"
/opt/anaconda3/bin/python3 -m uvicorn main:app --host 127.0.0.1 --port 8000