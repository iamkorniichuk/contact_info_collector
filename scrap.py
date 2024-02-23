from regex import (
    split_by_punctuation,
    capture_all_in_one,
    url_until_params,
    facebook_page_pattern,
    instagram_page_pattern,
    linkedin_page_pattern,
    tiktok_page_pattern,
    youtube_page_pattern,
)

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


def check_email_href_condition(value):
    attribute = "mailto:"
    result = []
    if value.startswith(attribute):
        string = value[len(attribute) :]
        emails = split_by_punctuation(string, ",")
        for email in emails:
            result.append(capture_all_in_one(email, pattern=url_until_params))
    return result


def check_facebook_href_condition(value):
    return capture_all_in_one(value, facebook_page_pattern)


def check_instagram_href_condition(value):
    return capture_all_in_one(value, instagram_page_pattern)


def check_linkedin_href_condition(value):
    return capture_all_in_one(value, linkedin_page_pattern)


def check_tiktok_href_condition(value):
    return capture_all_in_one(value, tiktok_page_pattern)


def check_youtube_href_condition(value):
    return capture_all_in_one(value, youtube_page_pattern)


href_conditions = {
    "email": check_email_href_condition,
    "facebook": check_facebook_href_condition,
    "instagram": check_instagram_href_condition,
    "linkedin": check_linkedin_href_condition,
    "tiktok": check_tiktok_href_condition,
    "youtube": check_youtube_href_condition,
}


def scrap_contact_info_by_href(soup, conditions=href_conditions):
    conditions = conditions.copy()
    contact_info = {}

    for a in soup.find_all("a", href=True):
        for key, func in conditions.items():
            result = func(a["href"])
            if result:
                contact_info[key] = result
                conditions.pop(key, None)
                break
    return contact_info
