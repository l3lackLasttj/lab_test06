from fastapi import FastAPI
from routes.courses_route import courses_api_router

app = FastAPI()

app.include_router(courses_api_router)
