import uvicorn
import json
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()



@app.get("/items/")
async def read_item(request: Request):
    params = dict(request.query_params)
    print(type(params))
    print(params)
    return params








if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

