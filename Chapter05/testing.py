import asyncio
import time

async def mytask() :
    print("Yuhu")


async def implement() :
    task=[]
    for i in range(5) :
        asyncio.ensure_future(mytask())
    await asyncio.gather(*task,return_exceptions=True)


loop = asyncio.get_event_loop()
loop.run_until_complete(implement())
print("Complete")
loop.close()