from bs4 import BeautifulSoup
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--blink-settings=imagesEnabled=false")
driver = webdriver.Chrome(options=options)


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
