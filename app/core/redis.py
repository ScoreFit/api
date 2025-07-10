# app/core/redis.py
import redis
from dotenv import load_dotenv
import os

load_dotenv()

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)


def test_connection():
    try:
        r.set("test_key", "hello")
        return r.get("test_key")
    except Exception as e:
        return f"Redis error: {e}"
