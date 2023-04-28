import feedparser
import requests
import ssl
import time
from functools import lru_cache, wraps
from datetime import datetime, timedelta


def timed_lru_cache(seconds: int, maxsize=128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime
            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


@timed_lru_cache(30)
def get_article_from_server(url):
    print('Fetching article from server... ')
    response = requests.get(url)
    return response.text


def monitor(url):
    max_len = 90
    while True:
        print('\nChecking feed...')
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:
            if 'python' in entry.title.lower():
                truncated_title = (entry.title[:max_len] + '...'
                                   if len(entry.title) > max_len
                                   else entry.title)
                print('Match found:',
                      truncated_title,
                      len(get_article_from_server(entry.link)))
        time.sleep(5)


if __name__ == '__main__':
    # if hasattr(ssl, '_create_unverified_context'):
    #     ssl._create_default_https_context = ssl._create_unverified_context
    # monitor('https://realpython.com/atom.xml')
    print({1, 2, 3,} | {4, 5, 6, 2})