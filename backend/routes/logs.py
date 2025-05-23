from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from database import db
from datetime import datetime
from fastapi.responses import JSONResponse
from bson import ObjectId

router = APIRouter()
logs_collection = db["logs"]

class LogEntry(BaseModel):
    date: str
    glucose: Optional[float] = None
    meals: Optional[str] = None
    activity: Optional[str] = None
    sleep_hours: Optional[float] = None

class LogEntryUpdate(BaseModel):
    date: Optional[str] = None
    glucose: Optional[float] = None
    meals: Optional[str] = None
    activity: Optional[str] = None
    sleep_hours: Optional[float] = None

def validate_date(date_str: str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Invalid date format, should be YYYY-MM-DD"
        )

@router.post("/", status_code=201)
def add_log(log: LogEntry):
    validate_date(log.date)
    existing_log = logs_collection.find_one({"date": log.date})
    if existing_log:
        raise HTTPException(status_code=400, detail="Log for this date already exists")

    log_dict = log.dict()
    result = logs_collection.insert_one(log_dict)
    print("Recieved log:", log)
    print("✅ Inserted log ID:", result.inserted_id)
    return {"message": "Log added successfully"}

@router.get("/")
def get_logs():
    logs_cursor = logs_collection.find()
    logs = []
    for log in logs_cursor:
        log["_id"] = str(log["_id"])
        logs.append(log)
    return {"logs": logs}

@router.put("/{log_id}", tags=["Logs"])
def update_log(log_id: str, log_update: LogEntryUpdate):
    if log_update.date:
        validate_date(log_update.date)
    update_data = {k: v for k, v in log_update.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update provided")

    result = logs_collection.update_one(
        {"_id": ObjectId(log_id)}, {"$set": update_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Log not found")

    updated_log = logs_collection.find_one({"_id": ObjectId(log_id)})
    updated_log["_id"] = str(updated_log["_id"])
    return updated_log

@router.delete("/{log_id}", tags=["Logs"], status_code=status.HTTP_204_NO_CONTENT)
def delete_log(log_id: str):
    result = logs_collection.delete_one({"_id": ObjectId(log_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Log not found")
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)
