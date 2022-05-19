import asyncio
import requests
import json
from httpx import AsyncClient


def get_url(i):
    return f"https://jsonplaceholder.typicode.com/posts/{i}"

async def request_and_print(i):
    url = get_url(i)
    print(f"sending {i}")
    res = await AsyncClient().get(url)
    print("\n", json.loads(res.content))


def request_and_print_sync(i):
    url = get_url(i)
    res = requests.get(url)
    print("\n", json.loads(res.content))

def sync_loop():
    for i in range(1,5):
        request_and_print(i)

async def async_loop(total):
    # batch = ((request_and_print, (i,)) for i in range(1,5))
    # tasks = [asyncio.create_task(request_and_print(*args)) for func, args in batch]
    tasks = [asyncio.create_task(request_and_print(i)) for i in range(1,total)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(async_loop(10))