from dask.distributed import Client
from fastapi import FastAPI


app = FastAPI()

def inc(x: int) -> int:
    return x + 1

@app.get("/")
async def index():
    print("Index!!!")
    async with Client(asynchronous=True) as client:
        future = client.submit(inc, 10)
        result = await future
    return {"message": result}
