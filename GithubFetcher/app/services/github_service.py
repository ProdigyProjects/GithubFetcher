import httpx
from app.config.config import Config
from app.utils.utils import save_to_csv
from fastapi import HTTPException
from tenacity import retry, wait_fixed, stop_after_attempt
from typing import List
from loguru import logger



@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
async def fetch_github_issues(per_page: int = 30, max_pages: int = 5):
    async with httpx.AsyncClient(follow_redirects=True) as client:
        issues = []
        for page in range(1, max_pages + 1):
            try:
                response = await client.get(Config.GITHUB_API_URL,
                                            params={"per_page": per_page, "page": page},
                                            headers={"Authorization": f"token {Config.GITHUB_TOKEN}"})

                # Log the status of the request
                logger.info(f"Fetching page {page}...")

                if response.status_code != 200:
                    logger.error(f"Failed to fetch page {page}, status code: {response.status_code}")
                    raise HTTPException(status_code=response.status_code, detail="Error fetching data")

                data = response.json()
                if not data:
                    logger.warning(f"No data returned on page {page}")
                    break
                issues.extend(data)

            except httpx.RequestError as e:
                logger.error(f"Request error on page {page}: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Request error: {str(e)}")
            except Exception as e:
                logger.error(f"General error on page {page}: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

        return issues


def write_to_csv(data: List[dict]):
    save_to_csv(data, Config.OUTPUT_FILE_PATH)
