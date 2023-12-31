from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {"Hi! From fastapi :)"}

if __name__ == '__main__':
    uvicorn.run(app,port=8000)