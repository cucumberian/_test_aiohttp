import pytest
from aiohttp.pytest_plugin import aiohttp_client

from app import app


@pytest.fixture()
async def cli(aiohttp_client):
    return await aiohttp_client(app)


async def test_healthcheck(cli):
    resp = await cli.get("/healthcheck")
    assert resp.status == 200
    json_response = await resp.json()
    assert await json_response == {}
