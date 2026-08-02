from pydantic import BaseModel


class WeatherNowResponse(BaseModel):
    city: str
    temperature: float
    feels_like: float
    description: str
    humidity: int
    wind_speed: float



