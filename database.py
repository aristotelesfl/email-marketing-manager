from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "root"
password = "@r1st0tele5"
host = "127.0.0.1"
connection = "level_marketing"

DATABASE_URL = f'mysql+mysqlconnector://{user}:{password}@{host}/{connection}'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()