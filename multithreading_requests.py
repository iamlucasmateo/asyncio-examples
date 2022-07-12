from concurrent.futures import ThreadPoolExecutor
import requests

from timer import timer

URL = "https://httpbin.org/uuid"

def fetch(url):
        return requests.get(url).json()["uuid"]
@timer
def run():
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(fetch, [URL]*100)
        executor.shutdown(wait=True)
        return results


if __name__ == "__main__":
    results = run()
    # results is a generator