from fastapi import Request
from aiocache import caches
from src.main.settings import REDIS_HOST, REDIS_PORT
from fastapi_plugins import RedisSettings

# Dependency
def get_db(request: Request) -> Request:
    """ Assign db session for request """
    return request.state.db


# You can use either classes or strings for referencing classes
class AppSettings(RedisSettings):
    api_name: str = str(__name__)
