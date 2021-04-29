import os.path


def get_urls(filename):
    if not os.path.isfile(filename):
        return None

    try:
        with open(filename, 'r') as file:
            urls = file.readlines()
    except:
        print("exception occurred in getURLs().")
        return None

    return [url.strip() for url in urls]
