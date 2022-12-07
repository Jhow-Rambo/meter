import base64
from fastapi import FastAPI, File, UploadFile, Request
import json
from routes.PaddleOCR import paddle

app = FastAPI()

app.include_router(paddle.router)

@app.get("/")
def home():
  return 'Hello World'

