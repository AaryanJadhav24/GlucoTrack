from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# client = MongoClient(os.getenv("MONGODB_URI"))
# uri = "mongodb+srv://aaryanjadhav2824:Aaryan24@aaryanscluster.aejvgsi.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://aaryanjadhav2824:Aaryan24@aaryanscluster.aejvgsi.mongodb.net/?retryWrites=true&w=majority")
try:
    client.admin.command("ping")
    print("✅ MongoDB connection successful")
except Exception as e:
    print("❌ MongoDB connection failed:", e)

db = client["gluco_db"]
logs_collection = db["logs"]
