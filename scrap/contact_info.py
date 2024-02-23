from .conditions import contact_info_href_conditions


def scrap_contact_info_by_href(soup, conditions=contact_info_href_conditions):
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
