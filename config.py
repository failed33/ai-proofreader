"""
Configuration settings for the AI Proofreader script.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# --- OpenAI API Configuration ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # Default to gpt-4o-mini
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.0"))  # For deterministic output

# --- Token Management ---
# Max tokens for a single API request (prompt + expected completion)
MAX_TOKENS_PER_API_REQUEST = int(os.getenv("MAX_TOKENS_PER_API_REQUEST", "4000"))

# --- File Paths ---
INPUT_DOCX_PATH = os.getenv("INPUT_DOCX_PATH", "my_draft.docx")
OUTPUT_DOCX_PATH = os.getenv("OUTPUT_DOCX_PATH", "proofread_output.docx")

# --- Retry Mechanism ---
MAX_RETRY_TIME_SECONDS = int(os.getenv("MAX_RETRY_TIME_SECONDS", "60"))

# --- Prompting ---
SYSTEM_PROMPT = """You are an expert copy-editor. You meticulously review text for grammatical errors, spelling mistakes, punctuation issues, clarity, conciseness, and overall readability. Return JSON only."""

USER_PROMPT_TEMPLATE = """Please proofread the following text.
Return a JSON object with the following three keys:

"original": The verbatim input text you received.

"corrected": The corrected version of the text. If no corrections are needed, this should be identical to the original.

"feedback": A bulleted list (strings) of major issues fixed or suggestions for improvement. If no issues, provide an empty list or a single item like "No major issues found."

Original Text:

{paragraph_text}"""

# Validation
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY environment variable not set. "
        "Please set it in your .env file or environment variables."
    ) 