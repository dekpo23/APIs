from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

app = FastAPI(title = "Simple FastApi App", version='1.0.0')

@app.get('/', description="This endpoint returns welcome message")
def root():
    return {"Message": "Welcome to my FastAPI Application"}

if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host = os.getenv("host"), port = int(os.getenv("port")))
    