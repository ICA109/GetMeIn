import requests
from flaskr.celery_config import app


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)


def func(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    func(["http://google.com", "https://amazon.com", "https://facebook.com", "https://twitter.com", "https://alexa.com"])