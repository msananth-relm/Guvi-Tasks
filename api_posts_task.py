import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    try:
        response = requests.get(API_URL, timeout=10)
        print(f"Status Code: {response.status_code}")

        response.raise_for_status()

        posts = response.json()

        for post in posts[:5]:
            print(f"Post ID: {post['id']}")
            print(f"User ID: {post['userId']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
            print("-" * 50)

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    fetch_posts()