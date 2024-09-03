from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    return "Hello World"

@app.post('/world')
async def world():
    return "Hello World from post"
    
    
''' uvicorn main:app --reload
        |
    to run the file 
    uvicorn filename:app --reload(reload is used when we are in development)

'''