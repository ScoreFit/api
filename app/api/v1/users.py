from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_users():
    return [{"username": "john"}, {"username": "doe"}]


from app.core.redis import test_connection


@router.get("/redis-test")
def redis_test():
    return {"redis_value": test_connection()}
