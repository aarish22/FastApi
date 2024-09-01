from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    return "Hello World"

@app.post('/world')
async def world():
    return "Hello World from post"
    