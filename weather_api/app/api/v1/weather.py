import httpx
from app.config import settings
from fastapi import APIRouter, HTTPException
from app.shemas.hourly_forecast import ForecastResponse

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("/by-coordinates")
async def get_by_coordinates(lat: float, lon: float):

    params = {
        "lat": lat,
        "lon": lon,
        "appid": settings.API_KEY,
        "units": "metric",
        "lang": "uk",
    }


    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(settings.API_URL_TODAY, params=params, timeout=5)

            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Error OpenWeather: {response.text}",
                )
            data = response.json()

            return {
                "city": data["name"] or "No city",
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
            }

        except Exception as e:
            raise HTTPException(
                status_code=503,
                detail=f"Error OpenWeather: {e}",
            )



@router.get("/by-all-day", response_model=ForecastResponse)
async def get_by_one_day(lat: float, lon: float):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": settings.API_KEY,
        "units": "metric",
        "lang": "uk",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(settings.API_URL_TOMORROW, params=params, timeout=5)

            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Error OpenWeather: {response.text}",
                )

            data = response.json()


            clean_forecast = []
            for item in data.get("list", [])[:8]:
                clean_forecast.append(
                    {
                        "datetime": item["dt_txt"],
                        "temperature": item["main"]["temp"],
                        "feels_like": item["main"]["feels_like"],
                        "description": item["weather"][0]["description"],
                        "humidity": item["main"]["humidity"],
                    }
                )

            return {
                "city": data.get("city", {}).get("name") or "No city",
                "forecast": clean_forecast,
            }

        except Exception as e:
            raise HTTPException(
                status_code=503,
                detail=f"Error OpenWeather: {e}",
            )

