import httpx

from config import API_URL



async def weather_now_service(lat: float, lon: float):

    url = f"{API_URL}/weather/by-coordinates"

    params = {
        'lat': lat,
        'lon': lon,
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)

            if response.status_code != 200:
                return "Error"
            data = response.json()

        except Exception as e:
            return f"Error {e}"

    return data








