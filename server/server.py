# backend/server.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import sys
from pathlib import Path

# import core/tokenizer
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))
from core.tokenizer import tokenize_text, DEFAULT_MODEL, estimate_cost

app = FastAPI(title="Tokenization API", version="1.0.0")

# allow ui / local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TokenizeRequest(BaseModel):
    text: str
    model: Optional[str] = DEFAULT_MODEL

@app.post("/tokenize")
def tokenize(req: TokenizeRequest):
    if not req.text:
        raise HTTPException(status_code=400, detail="Text is required")
    try:
        result = tokenize_text(req.text, model=req.model or DEFAULT_MODEL)
        result["estimated_cost_usd"] = estimate_cost(result["token_count"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
