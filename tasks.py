import asyncio

async def waiter() -> None:
    task1 = asyncio.create_task(cook("Pasta", 8))
    task2 = asyncio.create_task(cook("Salad", 3))
    task3 = asyncio.create_task(cook("Steak", 16))
    
    await task1
    await task2
    await task3
    
async def cook(order: str, time_to_prepare: int) -> None:
    print(f"Getting {order} order")
    await asyncio.sleep(time_to_prepare)
    print(order, "ready")
    

asyncio.run(waiter())