# GitHub Issues Fetcher API

This is a FastAPI backend application that fetches GitHub issues from a repository and saves them to a CSV file. The application demonstrates best practices for building production-grade APIs.

---

## Features

### Current Production-Grade Features
1. **Pagination Support**:
   - Fetches data across multiple pages using the GitHub API’s pagination features.
   - Supports `per_page` and `max_pages` parameters to control the number of issues fetched.

2. **Asynchronous Programming**:
   - Uses `async` and `await` to handle HTTP requests and file I/O efficiently.

3. **Environment Variable Management**:
   - Uses `python-dotenv` to load sensitive configuration (e.g., GitHub token) from a `.env` file.

4. **Error Handling**:
   - Handles failed API requests, missing data, and other exceptions gracefully.

5. **Structured Logging**:
   - Uses `loguru` for structured and detailed logging.

6. **CSV Output**:
   - Saves fetched issues to a CSV file for further analysis or processing.

7. **Unit Testing**:
   - Includes unit tests for the `/fetch-github-issues` endpoint using `unittest.mock`.

---

### Future Improvements
1. **Rate Limiting**:
   - Add rate limiting to prevent abuse of the API (e.g., using `slowapi`).

2. **Authentication**:
   - Secure the API with API key authentication or OAuth.

3. **Enhanced Logging**:
   - Configure log rotation and structured logging for better debugging and monitoring.

4. **CORS Configuration**:
   - Add CORS middleware to allow cross-origin requests from trusted frontend applications.

5. **Health Check Endpoint**:
   - Add a `/health` endpoint to monitor the status of the application.

6. **Containerization**:
   - Use Docker to containerize the application for easy deployment and scaling.

7. **Comprehensive Testing**:
   - Add integration tests and edge case scenarios.

---

## Getting Started

### Prerequisites
- Python 3.9 or higher
- A GitHub token (create one [here](https://github.com/settings/tokens))

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
<br>

### Start the FastAPI Server
To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```
### Testing
Run the unit tests:
```bash
pytest
```






   
