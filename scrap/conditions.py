from regex import (
    split_by_punctuation,
    capture_all_in_one,
    email_pattern,
    facebook_page_pattern,
    instagram_page_pattern,
    linkedin_page_pattern,
    tiktok_page_pattern,
    youtube_page_pattern,
)


def check_email_href_condition(value):
    attribute = "mailto:"
    result = []
    if value.startswith(attribute):
        string = value[len(attribute) :]
        emails = split_by_punctuation(string, ",")
        for email in emails:
            result.append(capture_all_in_one(email, pattern=email_pattern))
    return result


contact_info_href_conditions = {
    "email": check_email_href_condition,
    "facebook": lambda x: capture_all_in_one(x, facebook_page_pattern),
    "instagram": lambda x: capture_all_in_one(x, instagram_page_pattern),
    "linkedin": lambda x: capture_all_in_one(x, linkedin_page_pattern),
    "tiktok": lambda x: capture_all_in_one(x, tiktok_page_pattern),
    "youtube": lambda x: capture_all_in_one(x, youtube_page_pattern),
}

contact_info_facebook_conditions = {
    "email": lambda x: capture_all_in_one(x, email_pattern),
}
