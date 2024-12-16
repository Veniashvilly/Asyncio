import asyncio
import time

async def find_sum(x, y):
    await asyncio.sleep(2)
    return x + y

async def find_multiplication(x, y):
    await asyncio.sleep(2)
    return x * y

async def main():
    start = time.time()
    sum = asyncio.create_task(find_sum(3, 4))
    multiplication = asyncio.create_task(find_multiplication(3, 4))
    await asyncio.gather(sum, multiplication)
    end = time.time()
    print(f"Время работы - {end - start}")

asyncio.run(main())

