from fastapi import FastAPI
from pydantic import BaseModel
from app.model_loader import llm
from fastapi.middleware.cors import CORSMiddleware

# Allow frontend/browser use
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class Query(BaseModel):
    prompt: str
    max_tokens: int = 256

# Chat endpoint
@app.post("/chat")
def chat(query: Query):
    output = llm(
        prompt=query.prompt,
        max_tokens=query.max_tokens
    )
    return {
        "response": output["choices"][0]["text"].strip()
    }
