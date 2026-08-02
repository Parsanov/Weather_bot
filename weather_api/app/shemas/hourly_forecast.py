from datetime import datetime
from typing import List
from pydantic import BaseModel


class HourlyForecast(BaseModel):
    datetime: str
    temperature: float
    feels_like: float
    description: str
    humidity: float


class ForecastResponse(BaseModel):
    city: str
    forecast: List[HourlyForecast]