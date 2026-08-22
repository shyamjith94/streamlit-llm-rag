from src.models import Users
from sqlalchemy.orm import Session
from argon2 import PasswordHasher

ph = PasswordHasher()

def _hash_password(password:str)->str:
    return ph.hash(password)

def _verify_password(password:str,hashed_password:str)->bool:
    return ph.verify(hashed_password, password)

def register_user(user:Users, db:Session):
    user.password = _hash_password(user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login_user(email:str, password:str, db:Session):
    user = db.query(Users).filter(Users.email == email).first()
    if user and _verify_password(password, user.password):
        return user
    return None