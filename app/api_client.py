import requests
from app.config import BASE_URL

class APIClient:
    def get_posts(self):
        return requests.get(f"{BASE_URL}/posts")

    def create_post(self, data):
        return requests.post(f"{BASE_URL}/posts", json=data)
