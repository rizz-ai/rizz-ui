import requests
import validators


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def is_valid_url(url_string: str) -> bool:
    try:
        validators.url(url_string)
        return True
    except:
        return False
