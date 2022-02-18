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
    to_dog_years = human_dog_years * 2
    return to_dog_years








if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

