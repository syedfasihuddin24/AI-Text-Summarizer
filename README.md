# 🤖 AI Text Summarizer Web App

A simple, elegant web application that uses AI to summarize long texts into concise 3-4 line summaries using LSA (Latent Semantic Analysis).

![Status](https://img.shields.io/badge/status-working-brightgreen)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688)

## ✨ Features

- 🎨 Clean, modern UI with gradient design
- ⚡ Fast summarization (1-3 seconds)
- 📊 Real-time character counter
- 🔄 Loading indicator during processing
- ✅ Error handling and validation
- 📈 Summary statistics (character reduction %)
- 💡 Sample text loader for testing
- 🚀 No large model downloads required (lightweight)

## 🛠️ Tech Stack

- **Backend**: Python FastAPI
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI Library**: Sumy (LSA Algorithm)
- **NLP**: NLTK

## 📋 Prerequisites

- Python 3.8 or higher
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

### 2️⃣ Start the Backend

**Option A: Using the batch file (Windows)**
```bash
start_server.bat
```

**Option B: Manual command**
```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

You should see:
```
INFO:main:Summarizer initialized successfully!
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 3️⃣ Open the Frontend

Simply **double-click** `index.html` or open it in your browser.

## 📖 How to Use

1. **Enter Text**: Paste or type text (minimum 100 characters)
2. **Load Sample**: Click "Load Sample Text" for a pre-loaded example
3. **Summarize**: Click "✨ Summarize Text"
4. **View Results**: Summary appears below with statistics

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
API welcome message.

## 📁 Project Structure

```
.
├── main.py                 # FastAPI backend
├── index.html              # Frontend UI
├── requirements.txt        # Python dependencies
├── start_server.bat        # Quick start script (Windows)
├── INSTRUCTIONS.txt        # Detailed instructions
└── README.md               # This file
```

## ⚙️ Customization

### Change Summary Length
Edit `main.py` line ~86:
```python
sentence_count = min(5, max(3, len(text) // 200))
```

### Switch Algorithm
Replace LSA with TextRank in `main.py`:
```python
from sumy.summarizers.text_rank import TextRankSummarizer
summarizer = TextRankSummarizer()
```

### Change Port
Modify the uvicorn command and update `index.html` line 237:
```javascript
const API_URL = 'http://127.0.0.1:YOUR_PORT';
```

## ⚡ Performance

| Metric | Performance |
|--------|-------------|
| First Request | 1-3 seconds |
| Subsequent Requests | < 1 second |
| Model Size | None (no downloads) |
| Memory Usage | Very low |

## 🐛 Troubleshooting

### Backend won't start
- Ensure dependencies are installed: `pip install -r requirements.txt`
- Check if port 8000 is available
- Try: `python -m uvicorn main:app --host 127.0.0.1 --port 8001`

### "Failed to connect to API" error
- Verify backend is running on port 8000
- Check terminal for error messages
- Test API directly: visit http://127.0.0.1:8000 in browser

### NLTK errors
The app auto-downloads required NLTK data. If issues occur:
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
```

## 📝 Error Handling

The app handles:
- ❌ Empty text input
- ❌ Text too short (< 100 characters)
- ❌ Backend connection failures
- ❌ Server errors during processing

## 🎯 Use Cases

- 📰 Summarize news articles
- 📚 Condense research papers
- 📧 Shorten long emails
- 📄 Create abstracts from documents
- 💼 Quick content reviews

## 📜 License

Free to use for personal and educational purposes.

## 🤝 Support

For issues or questions:
1. Check browser console (F12 → Console)
2. Check backend terminal logs
3. Review `INSTRUCTIONS.txt` for detailed help

## 🎉 Enjoy summarizing!

---

**Made with ❤️ using FastAPI and Sumy**
