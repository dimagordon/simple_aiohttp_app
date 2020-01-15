from aiohttp import web

from .db import create_db
from . import settings, routes


async def on_startup(app):
    app['db'] = await create_db(app)


async def close_db(app):
    engine = app['db']
    engine.close()
    await engine.wait_closed()


def init_app(*args, **kwargs):

    app = web.Application()
    app['config'] = settings.config
    routes.setup(app)
    app.on_startup.append(on_startup)
    app.on_cleanup.append(close_db)

    web.run_app(app)
