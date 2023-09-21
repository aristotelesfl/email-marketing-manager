from sqlalchemy.orm import Session
from models import User


class UserCore:

    def create_user(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def clone_user_list(db: Session, user: User):
        pass

    def get_users(db: Session, skip: int = 0, limit: int = 10):
        return db.query(User).offset(skip).limit(limit).all()

    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def update_user(db: Session, user_id: int, new_data: dict):
        user = db.query(User).filter(User.id == user_id).first()
        for key, value in new_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user

    def delete_user(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        db.delete(user)
        db.commit()
        return user