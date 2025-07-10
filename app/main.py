from fastapi import FastAPI
from app.api.v1 import users

app = FastAPI()

# app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(users.router, prefix="/v1/users", tags=["Users"])


@app.get("/")
def root():
    return {"message": "Welcome to ScoreFit API"}
