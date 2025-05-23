# from fastapi import APIRouter, HTTPException, Depends
# from models import UserCreate, UserLogin
# from database import db
# from utils import hash_password, verify_password, create_access_token

# router = APIRouter()
# users_collection = db["users"]

# @router.post("/register")
# def register(user: UserCreate):
#     if users_collection.find_one({"username": user.username}):
#         raise HTTPException(status_code=400, detail="Username already exists")
#     hashed = hash_password(user.password)
#     users_collection.insert_one({"username": user.username, "password": hashed})
#     token = create_access_token({"sub": user.username})
#     return {"access_token": token, "token_type": "bearer"}


# @router.post("/login")
# def login(user: UserLogin):
#     user_data = users_collection.find_one({"username": user.username})
#     if not user_data or not verify_password(user.password, user_data["password"]):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     token = create_access_token({"sub": user.username})
#     return {"access_token": token, "token_type": "bearer"}
