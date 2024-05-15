import asyncio
from models import HashRequest
from models import HashResponse
from celery_app import calc_hash


async def hash_view(request) -> HashResponse:
    request_json = await request.json()
    hash_request = HashRequest.model_validate(request_json)
    hash_response = HashResponse()
    hash_response.hash_string = await async_calc_hash(
        string=hash_request.string
    )
    return hash_response


async def async_calc_hash(string: str) -> str:
    result = calc_hash.delay(string=string)
    ans = result.get()
    return ans
