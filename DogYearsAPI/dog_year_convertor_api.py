import uvicorn
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return f'Hello! try using the url + /items/dog_year for example use url/items/dog_year=2'

@app.get("/items/")
async def read_item(dog_year: int):
    if dog_year == 1:
        return {'to_human_year': 15}
    elif dog_year == 2:
        return {'to_human_year': 24}
    else:
        foo = dog_year -2
        bar = foo * 4 + 24
        return {'to_human_year': bar}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
