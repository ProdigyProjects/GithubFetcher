
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.services.github_service.fetch_github_issues")
def test_fetch_github_issues(mock_fetch):
    mock_fetch.return_value = [
        {"id": 12345, "title": "Test Issue", "state": "open", "user_login": "user1"}
    ]
    response = client.get("/fetch-github-issues")
    assert response.status_code == 200
    assert "Data successfully saved to CSV" in response.json()["message"]
