import os

DEFAULT_HOST = os.environ.get("DEFAULT_HOST", "localhost")
DEFAULT_HOST_PORT = os.environ.get("DEFAULT_HOST_PORT", 8000)
FRONTEND_HOST = os.environ.get("FRONTEND_HOST", "localhost")
FRONTEND_HOST_PORT = os.environ.get("FRONTEND_HOST_PORT", 4000)

DB_NAME = os.environ.get("DB_NAME", "pokemon")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_HOST = os.environ.get("DB_HOST", "pokemon-postgres")
DB_PORT = os.environ.get("DB_PORT", 5432)

REDIS_HOST = os.environ.get("REDIS_HOST", "pokemon-redis")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
CACHE_LOCATION = os.environ.get(
    "CACHE_LOCATION", f"redis://{REDIS_HOST}:{REDIS_PORT}/1"
)
