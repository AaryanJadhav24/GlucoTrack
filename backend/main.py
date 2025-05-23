# main.py (or app.py) - FastAPI main entry point

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import users, logs, predict
# from routes.logs import router as logs_router
# from routes.users import router as users_router
# from auth_routes import router as auth_router  # Remove or comment if auth_routes.py doesn't exist
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from routes import ai_insights

tags_metadata = [
    {"name": "Logs", "description": "Operations with logs."},
    {"name": "Auth", "description": "Authentication routes"},
]

app = FastAPI(openapi_tags=tags_metadata)

# Allow CORS from your React app origin
origins = [
    "http://localhost:3000",  # React frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_insights.router, prefix="/ai")
app.include_router(logs.router, prefix="/logs")
app.include_router(predict.router, prefix="/predict")

# app.include_router(users.router, prefix="/auth")
# app.include_router(auth_router, prefix="/auth")  # Comment out if auth_router not used
# app.include_router(users_router, prefix="/users")
# app.include_router(logs_router, prefix="/logs")  # Remove if logs.router and logs_router are the same

# Print all routes on startup for debugging
for route in app.routes:
    print(f"{route.path} -> {route.methods}")
    
    
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors()},
    )
