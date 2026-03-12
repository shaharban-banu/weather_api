from sqlalchemy import Column,Integer,String,Float,DateTime
from database import BASE
from datetime import datetime

class Weather(BASE):
    __tablename__='weather'

    id=Column(Integer,primary_key=True,index=True)
    city=Column(String,unique=True)
    temperature=Column(Float)
    humidity=Column(Integer)
    description=Column(String)
    updated_at=Column(DateTime,default=datetime.utcnow)