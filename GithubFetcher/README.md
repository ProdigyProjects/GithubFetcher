
# GitHub Issues Fetcher

This is a FastAPI project that fetches issues from a GitHub repository and saves them to a CSV file.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file with your GitHub API URL and token.

3. Run the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

## Endpoints

- `/` - Welcome message
- `/fetch-github-issues` - Fetches GitHub issues and saves them to CSV.
    