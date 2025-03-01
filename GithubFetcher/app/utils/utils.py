
import csv
from typing import List

def save_to_csv(data: List[dict], file_path: str):
    keys = ["id", "number", "title", "state", "created_at", "updated_at", "user_login"]
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        for item in data:
            writer.writerow({
                "id": item.get("id"),
                "number": item.get("number"),
                "title": item.get("title"),
                "state": item.get("state"),
                "created_at": item.get("created_at"),
                "updated_at": item.get("updated_at"),
                "user_login": item.get("user", {}).get("login")
            })
