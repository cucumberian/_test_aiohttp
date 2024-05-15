import click
from aiohttp import web
from app import app as web_app


@click.command()
@click.option("--port", default=8000, help="Port to run the web app on")
@click.option("--host", default="0.0.0.0", help="Host to run the web app on")
def run(host, port):
    web.run_app(web_app, host=host, port=port)


if __name__ == "__main__":
    run()
