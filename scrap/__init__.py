from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def url_to_soup(url, safe=True):
    try:
        if not url.startswith("http"):
            url = "https://" + url
        content = requests.get(
            url, timeout=2, verify=False, allow_redirects=True
        ).content
        return BeautifulSoup(content, "lxml")
    except Exception as e:
        if not safe:
            raise e
