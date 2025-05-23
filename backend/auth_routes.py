# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel, EmailStr
# from database import db
# from passlib.hash import bcrypt

# router = APIRouter()
# users_collection = db["users"]

# class SignupUser(BaseModel):
#     username: str
#     email: EmailStr
#     password: str

# @router.post("/signup", tags=["Auth"])
# def signup(user: SignupUser):
#     if users_collection.find_one({"email": user.email}):
#         raise HTTPException(status_code=400, detail="Email already registered.")
    
#     hashed_password = bcrypt.hash(user.password)
#     users_collection.insert_one({
#         "username": user.username,
#         "email": user.email,
#         "password": hashed_password
#     })
#     return {"message": "User signed up successfully"}
