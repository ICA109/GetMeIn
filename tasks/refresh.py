"""
primary driver for celery
"""

from celery import Celery
import requests

app = Celery('refresh', broker='redis://localhost:6379/0', include=['flaskr.blog'])


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)


@app.task
def func(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    func(["http://google.com", "https://facebook.com", "https://twitter.com", "https://alexa.com"])
