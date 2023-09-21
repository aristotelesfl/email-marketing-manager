from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    last_name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    last_name: str
    email: str

class UserUpdate(BaseModel):
    name: str
    last_name: str
    email: str