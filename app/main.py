from fastapi import FastAPI
from pydantic import BaseModel

from .config import settings

app = FastAPI(title=settings.app_name)

class EchoRequest(BaseModel):
    message: str

@app.get("/health")
def health_check():
    return {"status": 200}

@app.post("/echo")
def echo(payload: EchoRequest):
    return {"received": payload.message}
