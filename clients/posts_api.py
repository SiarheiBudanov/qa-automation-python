import requests


class PostsApi:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {"Accept": "application/json"}
        )

    def get_posts(self):
        return self.session.get(
            f"{self.BASE_URL}/posts",
            timeout=10,
        )

    def get_post(self, post_id):
        return self.session.get(
            f"{self.BASE_URL}/posts/{post_id}",
            timeout=10,
        )

    def create_post(self, payload):
        return self.session.post(
            f"{self.BASE_URL}/posts",
            json=payload,
            timeout=10,
        )

    def close(self):
        self.session.close()