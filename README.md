# 🤖 Summify — AI Text Summarizer

A fast, beautifully designed web app that uses AI to summarize long texts into concise summaries using LSA (Latent Semantic Analysis).

![Status](https://img.shields.io/badge/status-working-brightgreen)
![Python](https://img.shields.io/badge/python-3.13%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688)

## ✨ Features

- 🎨 Modern UI with Raging Beige, Coral Pink, Sleuthe Yellow & Pink Leaf palette
- ⚡ Fast summarization (1-3 seconds)
- 📊 Real-time character counter
- 🔄 Animated loading bar during processing
- ✅ Error handling and validation
- 📈 Summary statistics (character reduction %)
- 💡 Sample text loader for testing
- 📋 One-click copy summary button
- 🚀 No large model downloads required (lightweight)

## 🛠️ Tech Stack

- **Backend**: Python FastAPI
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI Library**: Sumy (LSA Algorithm)
- **NLP**: NLTK

## 📋 Prerequisites

- Python 3.13 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge, Safari)

## 🚀 Quick Start

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- FastAPI & Uvicorn (web framework + server)
- Sumy (text summarization)
- NLTK (natural language processing)
- python-multipart (form handling)

### 2️⃣ Start the Backend

**Mac:**
```bash
./start_server.sh
```

Or manually:
```bash
/opt/anaconda3/bin/python3 -m uvicorn main:app --host 127.0.0.1 --port 8000
```

You should see:
INFO:main:Summarizer initialized successfully!
INFO:     Uvicorn running on http://127.0.0.1:8000

### 3️⃣ Open the App

Visit in your browser:
http://127.0.0.1:8000

## 📖 How to Use

1. **Enter Text**: Paste or type text (minimum 100 characters)
2. **Load Sample**: Click "Load sample" for a pre-loaded example
3. **Summarize**: Click "✦ Summarize"
4. **View Results**: Summary appears below with statistics
5. **Copy**: Click "COPY" to copy the summary

## 🔧 API Endpoints

### `POST /summarize`
Summarize text input.

**Request:**
```json
{
  "text": "Your long text here..."
}
```

**Response:**
```json
{
  "summary": "Concise summary...",
  "original_length": 1000,
  "summary_length": 200
}
```

### `GET /health`
Check API health status.

### `GET /`
Serves the frontend UI.

## 📁 Project Structure
.
├── main.py                 # FastAPI backend

├── index.html              # Frontend UI

├── requirements.txt        # Python dependencies

└── README.md               # This file

## ⚡ Performance

| Metric | Performance |
|--------|-------------|
| First Request | 1-3 seconds |
| Subsequent Requests | < 1 second |
| Model Size | None (no downloads) |
| Memory Usage | Very low |

## 🐛 Troubleshooting

### Backend won't start
- Install dependencies: `pip install -r requirements.txt`
- Check if port 8000 is in use
- Try: `/opt/anaconda3/bin/python3 -m uvicorn main:app --host 127.0.0.1 --port 8001`

### "Failed to connect to API" error
- Make sure backend is running
- Open `http://127.0.0.1:8000` directly in browser to verify

### NLTK errors
The app auto-downloads required NLTK data. If issues occur:
```bash
python3 -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

## 🎯 Use Cases

- 📰 Summarize news articles
- 📚 Condense research papers
- 📧 Shorten long emails
- 📄 Create abstracts from documents
- 💼 Quick content reviews

## 📜 License

Free to use for personal and educational purposes.

---

**Crafted with ❤️ by Syed Fasihuddin**
