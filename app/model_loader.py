from llama_cpp import Llama
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")
CONTEXT_SIZE = int(os.getenv("CONTEXT_SIZE", 2048))
NUM_THREADS = int(os.getenv("NUM_THREADS", 8))

# Load model once
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=CONTEXT_SIZE,
    n_threads=NUM_THREADS,
    verbose=False
)
