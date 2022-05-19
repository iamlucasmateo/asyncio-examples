import asyncio
from time import sleep

async def count(first):
    print(first)
    await asyncio.sleep(1)
    second = f"{first}_2"
    print(second)
    return first

batch = [(count, ("uno",)), (count, ("dos",)), (count, ("tres",))]

async def main():

    # this needs to be defined inside the async function
    # otherwise a never awaited error will show up
    tasks = [asyncio.create_task(func(*args)) for func, args in batch]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())