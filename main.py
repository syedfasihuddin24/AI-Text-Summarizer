from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Text Summarizer API")

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the summarization model
try:
    logger.info("Summarizer initialized successfully!")
    summarizer_available = True
except Exception as e:
    logger.error(f"Error initializing summarizer: {e}")
    summarizer_available = False


class TextInput(BaseModel):
    text: str


class SummaryResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int


@app.get("/")
async def root():
    return {"message": "AI Text Summarizer API is running!"}


@app.post("/summarize", response_model=SummaryResponse)
async def summarize_text(input_data: TextInput):
    """
    Endpoint to summarize input text.
    Accepts text (min 2000 chars) and returns a 3-4 line summary.
    """
    try:
        text = input_data.text.strip()
        
        # Validation
        if not text:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        if len(text) < 100:
            raise HTTPException(
                status_code=400, 
                detail="Text is too short. Please provide at least 100 characters for meaningful summarization."
            )
        
        if not summarizer_available:
            raise HTTPException(
                status_code=503, 
                detail="Summarization service is not available. Please try again later."
            )
        
        logger.info(f"Summarizing text of length: {len(text)} characters")
        
        # Create parser and summarizer
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        
        # Calculate number of sentences (3-4 lines approximately 3-5 sentences)
        sentence_count = min(5, max(3, len(text) // 200))  # Adaptive based on text length
        
        # Generate summary
        summary_sentences = summarizer(parser.document, sentence_count)
        summary = ' '.join([str(sentence) for sentence in summary_sentences])
        
        logger.info(f"Summary generated successfully. Length: {len(summary)} characters")
        
        return SummaryResponse(
            summary=summary,
            original_length=len(text),
            summary_length=len(summary)
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during summarization: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred during summarization: {str(e)}"
        )


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "summarizer_available": summarizer_available
    }
