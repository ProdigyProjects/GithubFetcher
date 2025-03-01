import os
from dotenv import load_dotenv

# Load environment variables from .env file (optional if needed)
load_dotenv()

class Config:
    GITHUB_API_URL = "https://api.github.com/repos/tiangolo/fastapi/issues"  # Directly set the URL
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Still using .env for token if available
    OUTPUT_FILE_PATH = os.getenv("OUTPUT_FILE_PATH")  # Use the .env for the output file pat
