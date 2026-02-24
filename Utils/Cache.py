import redis
import json
from Config import REDIS_URL

r = redis.Redis.from_url(REDIS_URL, decode_responses=True)

def get_cache(key):
    data = r.get(key)
    if data:
        return json.loads(data)
    return None

def set_cache(key, value, ttl=21600):
    r.setex(key, ttl, json.dumps(value))
