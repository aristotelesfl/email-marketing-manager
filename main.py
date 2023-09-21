from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from core import UserCore
from models import User
from schemas import UserCreate, UserResponse, UserUpdate

app = FastAPI()

# Cria as tabelas no banco de dados
User.metadata.create_all(bind=engine)

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserCore.create_user(db, User(**user.dict()))

@app.get("/users/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return UserCore.get_users(db, skip, limit)

@app.get("/users/{user_id}", response_model=UserResponse)
def read_livro(user_id: int, db: Session = Depends(get_db)):
    user = UserCore.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@app.put("/users/{user_id}", response_model=UserResponse)
def update_livro(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    existing_user = UserCore.get_user(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    new_data = user.dict()
    return UserCore.update_user(db, user_id, new_data)

@app.delete("/users/{user_id}", response_model=UserResponse)
def delete_livro(user_id: int, db: Session = Depends(get_db)):
    existing_user = UserCore.get_user(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return UserCore.delete_user(db, user_id)