from aiohttp import web
from json.decoder import JSONDecodeError
from pydantic import ValidationError
from views import hash_view


async def healthcheck(request):
    return web.json_response({})


async def post_hash(request):
    try:
        response_data = await hash_view(request=request)
    except JSONDecodeError as e:
        return web.json_response({"validation_errors": str(e)}, status=400)
    except ValidationError as e:
        return web.json_response({"validation_errors": e.errors()}, status=400)
    return web.json_response(response_data.model_dump())


app = web.Application()


app.add_routes(
    [
        web.get("/healthcheck", healthcheck),
        web.post("/hash", post_hash),
    ]
)


if __name__ == "__main__":
    # celery.start()
    web.run_app(app, host="0.0.0.0", port=8000)
