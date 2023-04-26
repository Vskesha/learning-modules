import requests


cache = dict()


def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text


def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]


if __name__ == '__main__':
    print(get_article("https://realpython.com/sorting-algorithms-python/")[:150])
    print(get_article("https://realpython.com/sorting-algorithms-python/")[:100])