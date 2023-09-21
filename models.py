from sqlalchemy import Column, Integer, String
from database import Base

class Emails(Base):
    __tablename__ = "emails"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: str = Column(String(15), nullable=False)
    last_name: str = Column(String(15), nullable=False)
    email: str = Column(String(15), nullable=False, unique=True)