import uvicorn

from fastapi import FastAPI

from app.config import settings
from app.api.v1.weather import router as weatherRouter

app = FastAPI(title="My Weather API")
app.include_router(weatherRouter, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)