from regex import (
    capture_all_in_one,
    email_pattern,
    facebook_page_pattern,
    instagram_page_pattern,
    linkedin_page_pattern,
    tiktok_page_pattern,
    youtube_page_pattern,
)

contact_info_conditions = {
    "email": lambda x: capture_all_in_one(x, email_pattern),
    "facebook": lambda x: capture_all_in_one(x, facebook_page_pattern),
    "instagram": lambda x: capture_all_in_one(x, instagram_page_pattern),
    "linkedin": lambda x: capture_all_in_one(x, linkedin_page_pattern),
    "tiktok": lambda x: capture_all_in_one(x, tiktok_page_pattern),
    "youtube": lambda x: capture_all_in_one(x, youtube_page_pattern),
}


def run_conditions(
    iterable, value_func, conditions=contact_info_conditions, to_skip=[]
):
    conditions = conditions.copy()
    for key in to_skip:
        conditions.pop(key, None)

    contact_info = {}

    for obj in iterable:
        for key, func in conditions.items():
            value = value_func(obj)
            result = func(value)
            if result:
                contact_info[key] = result
                conditions.pop(key, None)
                break
    return contact_info
