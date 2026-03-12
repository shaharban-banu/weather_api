from sqlalchemy.orm import Session
from models import Weather
from config import API_KEY
import httpx
from datetime import datetime,timedelta

CACHE_EXPIRY=timedelta(minutes=30)

async def get_weather(city:str,db:Session):
    cached=db.query(Weather).filter(Weather.city==city).first()

    if cached:
        if cached.updated_at and datetime.utcnow()-cached.updated_at<CACHE_EXPIRY:
            return {
                'source':'database_cache',
                'city':cached.city,
                'temperature':cached.temperature,
                'humidity':cached.humidity,
                'description':cached.description,
                'last_updated':cached.updated_at
            }
    
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    async with httpx.AsyncClient() as client:
        response=await client.get(url)

    data=response.json()
   
    if response.status_code != 200 or "main" not in data:
        return {
            "error": data.get("message", "Failed to fetch weather")
                }
    #Update existing cache or create new record
    if cached:
        cached.temperature = data['main']['temp']
        cached.humidity = data['main']['humidity']
        cached.description = data['weather'][0]['description']
        cached.updated_at = datetime.utcnow()
    else:
        weather=Weather(
            city=city,
            temperature=data['main']['temp'],
            humidity=data['main']['humidity'],
            description=data['weather'][0]['description'],
            updated_at=datetime.utcnow()
        )
        db.add(weather)
    db.commit()
    db.refresh(weather)


    return {
        'source':'external app',
            'city':city,
            'temperature':weather.temperature,
            'humidity':weather.humidity,
            'description':weather.description,
            "last_updated": cached.updated_at
    }