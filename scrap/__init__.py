from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome()
driver.set_page_load_timeout(10)


def url_to_soup(url, safe=True):
    try:
        url = normalize_url(url)
        driver.get(url)

        return BeautifulSoup(driver.page_source, "html.parser")
    except Exception as e:
        if not safe:
            raise e


def normalize_url(url):
    if not url.startswith("http"):
        url = "https://" + url
    return url
