from fastapi import APIRouter
from app.core.redis import test_connection

router = APIRouter()


@router.get("/")
def get_users():
    return [{"username": "john"}, {"username": "doe"}]


@router.get("/redis-test")
def redis_test():
    return {"redis_value": test_connection()}
