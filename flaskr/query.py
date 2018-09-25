import time
import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


def check_for_updates(posts):
    course_list_and_info = []

    for post in posts:
        course_title = post['title']
        course_contact = post['body']
        course_list_and_info.append((course_title, course_contact))

    print(course_list_and_info)

    url = "https://vsb.mcgill.ca/vsb/criteria.jsp?access=0&lang=en&tip=1&page=results&scratch=0&term=201901&sort=none&filters=iiiiiiiii&bbs=&ds=&cams=Distance_Downtown_Macdonald_Off-Campus&locs=any&isrts=&course_0_0=COMP-520&sa_0_0=&cs_0_0=--201901_9182--&cpn_0_0=&csn_0_0=&ca_0_0=&dropdown_0_0=al&ig_0_0=0&rq_0_0="
    page = requests.get(url)
    # url2 = "https://horizon.mcgill.ca/pban1/bwckschd.p_disp_detail_sched?term_in=201901&crn_in=16181&search_mode_in="
    # page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    # time.sleep(3)

    '''
    page_content = page.content
    soup = BeautifulSoup(page_content, 'html.parser')
    class_space = soup.find_all("span", "seatText")
    print(soup.prettify())
    print(class_space)
    '''
    from bs4 import BeautifulSoup
    from selenium import webdriver

    url1a = url
    browser = webdriver.PhantomJS()
    browser.get(url1a)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    a = soup.find_all("span", "seatText")
    print(a)



    try:
        url2 = "https://horizon.mcgill.ca/pban1/bwckschd.p_disp_detail_sched?term_in=201901&crn_in=16181&search_mode_in="
        with urllib.request.urlopen(url2) as response:
            # time.sleep(3)
            su = BeautifulSoup(response.read(), 'lxml')
            cs = su.find_all("td", "dddefault")
            # print(cs)

    except urllib.request.HTTPError as e:
        if e.code == 404:
            print(f"{url} is not found")
        elif e.code == 503:
            print(f'{url} base webservices are not available')
            ## can add authentication here
        else:
            print('http error', e)

