import uvicorn
import json
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/{dog_year}')
def read_item(dog_year):
    thingy = json.loads(dog_year)
    print(thingy)
    print(type(thingy))
#E    if type(thingy) == int:
#E        print(type(thingy))
#E        print('int')
#E    else:
#E        print(type(thingy))
#E        print('string')








if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

