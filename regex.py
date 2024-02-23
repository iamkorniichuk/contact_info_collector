import re


def split_by_punctuation(string, punctuation=r",.;@#?!&$"):
    pattern = r"[{punctuation}]+\ *".format(punctuation=punctuation)
    return re.split(pattern, string)


email_pattern = r"([A-Za-z0-9]+[._])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
facebook_page_pattern = (
    r"(mbasic\.facebook|m\.facebook|facebook|fb)\.(com|me)\/(?:[^\s\/?]+)?(?:\?|\/|$)"
)
instagram_page_pattern = r"(instagram\.com\/)(?:[^\s\/?]+)?(?:\?|\/|$)"
linkedin_page_pattern = r"(linkedin\.com\/company\/)(?:[^\s\/?]+)?(?:\?|\/|$)"
tiktok_page_pattern = r"(tiktok\.com\/@)(?:[^\s\/?]+)?(?:\?|\/|$)"
youtube_page_pattern = r"(youtube\.com\/channel\/)(?:[^\s\/?]+)?(?:\?|\/|$)"


def capture_all_in_one(string, pattern):
    pattern = r"({pattern})".format(pattern=pattern)
    results = re.findall(pattern, string)
    if results:
        return results[0][0]
