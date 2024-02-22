import re


def split_by_punctuation(string, punctuation=r",.;@#?!&$"):
    pattern = r"[{punctuation}]+\ *".format(punctuation=punctuation)
    return re.split(pattern, string)


def capture_until_url_params(string):
    pattern = r"^(.*?)(?:\?|$)"
    results = re.findall(pattern, string)
    if results:
        return results[0]
