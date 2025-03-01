from fastapi import FastAPI, HTTPException
import httpx
from typing import List
from app.services.github_service import fetch_github_issues, write_to_csv
from app.config.config import Config
from loguru import logger
from asyncio import to_thread

# Initialize FastAPI app
app = FastAPI()


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the GitHub Issues Fetcher API! Use /fetch-github-issues to download data."}


# Fetch GitHub issues and save to CSV
@app.get("/fetch-github-issues")
async def fetch_and_save_issues(per_page: int = 30, max_pages: int = 5):
    try:
        # Add more detailed logging
        logger.info(f"Fetching issues with per_page={per_page} and max_pages={max_pages}")

        issues = await fetch_github_issues(per_page, max_pages)
        if issues:
            logger.info(f"Fetched {len(issues)} issues, now writing to CSV...")
            # Offload the blocking CSV writing to another thread
            await to_thread(write_to_csv, issues)
            logger.info(f"Data successfully saved to CSV with {len(issues)} issues")
            return {"message": "Data successfully saved to CSV", "file": Config.OUTPUT_FILE_PATH}
        else:
            logger.warning("No issues found.")
            raise HTTPException(status_code=404, detail="No issues found")
    except Exception as e:
        logger.error(f"Error in fetching data: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
