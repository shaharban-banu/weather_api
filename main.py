from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import models
from database import engine,SessionLocal
from weather_service import get_weather


models.BASE.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/weather/{city}')
async def weather(city:str,db:Session=Depends(get_db)):
    return await get_weather(city,db)