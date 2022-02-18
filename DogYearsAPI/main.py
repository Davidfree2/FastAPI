import uvicorn
import json
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()



@app.get("/convert_dog_years/")
async def read_item(request: Request):
    params = dict(request.query_params)
    print(type(params))
    print(params)
    human_dog_years = int(params['dogyear'])
    if human_dog_years == 1:
        return 15
    elif human_dog_years == 2:
        return 24
    else:
        foo = human_dog_years -2
        bar = foo * 4 + 24
        return bar








if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

