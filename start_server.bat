@echo off
echo Starting AI Text Summarizer Backend Server...
echo.
echo The server will be available at: http://127.0.0.1:8000
echo.
echo To stop the server, press CTRL+C
echo.
python -m uvicorn main:app --host 127.0.0.1 --port 8000
pause
