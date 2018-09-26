"""
primary driver for celery
"""

from celery import Celery
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

import celery_config
# configuration
app = Celery('refresh', broker='redis://localhost:6379/0', include=['flaskr.blog'])
app.config_from_object(celery_config)







@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)

@app.task
def batch_query(posts):
    course_list_and_info = []

    for post in posts:
        course_title = post['title']
        course_contact = post['body']
        course_term_raw = course_contact.split(',')[0]
        course_list_and_info.append((course_title, course_contact))
        course_term = '000000'

        if '2018' in course_term_raw:
            course_term = '201809'
        elif '2019' in course_term_raw:
            course_term = '201901'

        url = "https://vsb.mcgill.ca/vsb/criteria.jsp?access=0&lang=en&tip=1&page=results&scratch=0&term={1}" \
              "&sort=none&filters=iiiiiiiii&bbs=&ds=&cams=Distance_Downtown_Macdonald_Off-Campus&locs=any&isrts=&" \
              "course_0_0={0}" \
              "&sa_0_0=&cs_0_0=--{1}_9182--&cpn_0_0=&csn_0_0=&ca_0_0=&dropdown_0_0=al&ig_0_0=" \
              "0&rq_0_0=".format(course_title, course_term)

        url1a = url
        browser = webdriver.PhantomJS()
        browser.get(url1a)
        delay = 3

        try:
            my_elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'seatText')))
            # print("Page loaded.")

        except TimeoutException:
            print("Warning taking too long to load. Possible issue with request.")

        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        open_seats_section = soup.find_all("span", "seatText")
        num_seats_available = 0

        if len(open_seats_section) > 0:
            num_seats_available = open_seats_section[0].text

        # print(num_seats_available)
        print('-----Sample Email Start-----')
        print('{0} in {1} has {2} open seats available now'.format(course_title, course_term, num_seats_available))
        print('-----Sample Email End-----')

@app.task
def func(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    func(["http://google.com", "https://facebook.com", "https://twitter.com", "https://alexa.com"])
