
from contextlib import asynccontextmanager, contextmanager
from fastapi import FastAPI
from dotenv import load_dotenv



# fastapi model init
# file main.py

load_dotenv()

app = FastAPI()


@app.get("/ping")
def ping_app():
    return "pong"


