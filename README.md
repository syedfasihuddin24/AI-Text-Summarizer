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