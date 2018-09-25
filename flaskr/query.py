from bs4 import BeautifulSoup
from selenium import webdriver


def check_for_updates(posts):
    course_list_and_info = []

    for post in posts:
        course_title = post['title']
        course_contact = post['body']
        course_list_and_info.append((course_title, course_contact))

    print(course_list_and_info)

    course_title = 'COMP-520'

    url = "https://vsb.mcgill.ca/vsb/criteria.jsp?access=0&lang=en&tip=1&page=results" \
          "&scratch=0&term=201901&sort=none&filters=iiiiiiiii&bbs=&ds=&cams=" \
          "Distance_Downtown_Macdonald_Off-Campus&locs=any&isrts=&course_0_0={0}&sa_0_0=" \
          "&cs_0_0=--201901_9182--&cpn_0_0=&csn_0_0=&ca_0_0=&dropdown_0_0=al&ig_0_0=0&rq_0_0=".format(course_title)

    url1a = url
    browser = webdriver.PhantomJS()
    browser.get(url1a)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    open_seats_section = soup.find_all("span", "seatText")
    num_seats_available = 0

    if len(open_seats_section) > 0:
        num_seats_available = open_seats_section[0].text

    print(num_seats_available)
