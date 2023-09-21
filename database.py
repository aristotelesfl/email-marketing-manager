from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "root"
password = "AR1st0tele5"
host = "localhost"
database = "level_marketing"

DATABASE_URL = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    