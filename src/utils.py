import aiohttp_cors
import logging


logger = logging.getLogger()


def setup_cors(app):
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*")})

    for route in list(app.router.routes()):
        cors.add(route)


def prepare_validation_log_message(initial_data, error):
    return {
        'initial_data': initial_data,
        'errors': error.messages
    }
