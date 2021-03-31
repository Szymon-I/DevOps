from typing import Dict
from aioredis import Redis
import pickle
from typing import Any, Callable


async def get_cached_or_db(
    cache: Redis,
    cache_key: str,
    query_function: Callable,
) -> Any:
    """ Get data from cache, otherwise get from db and set cache """
    cached_data = await cache.get(cache_key)
    if not cached_data:
        data = query_function()
        await cache.set(cache_key, pickle.dumps(data))
        return data
    return pickle.loads(cached_data)
