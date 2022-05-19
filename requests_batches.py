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

async def main(total):
    max_tasks_per_batch = 10
    batches = []
    tasks = []
    # prepare inputs
    for i in range(1, total):
        tasks.append((request_and_print, (i, )))
        if len(tasks) == max_tasks_per_batch:
            batches.append(tasks)
            tasks = []

    # run in batches
    for batch in batches:
        running_batch = [asyncio.create_task(func(*args)) for func, args in batch]
        await asyncio.gather(*running_batch)


if __name__ == "__main__":
    asyncio.run(main(30))