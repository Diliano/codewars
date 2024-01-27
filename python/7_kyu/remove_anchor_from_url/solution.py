def remove_url_anchor(url):
    # split url by the anchor (#) and then return the portion before the anchor
    # if no anchor is found, the entire URL is returned
    return url.split("#")[0]