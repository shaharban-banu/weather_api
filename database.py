from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATBASE_URL='sqlite:///./weather.db'

engine=create_engine(DATBASE_URL)

SessionLocal=sessionmaker(bind=engine)

BASE=declarative_base()