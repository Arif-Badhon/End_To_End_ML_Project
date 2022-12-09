from fastapi import FastAPI
from routes import *


app = FastAPI(
    title="End to End ML Project",
    version="0.0.1"
)

app.include_router(mlmodel)