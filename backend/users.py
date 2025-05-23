from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from database import db
from auth import get_password_hash, verify_password, create_access_token
from datetime import timedelta

router = APIRouter()
users_collection = db["users"]

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate):
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    hashed_password = get_password_hash(user.password)
    users_collection.insert_one({"username": user.username, "hashed_password": hashed_password})
    return {"message": "User created successfully"}

@router.post("/token")
async def login(user: UserLogin):
    db_user = users_collection.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(hours=24))
    return {"access_token": access_token, "token_type": "bearer"}
