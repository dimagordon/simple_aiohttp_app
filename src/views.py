import asyncio
from http import HTTPStatus
from json.decoder import JSONDecodeError

from aiohttp import web
from marshmallow import ValidationError


from .schemas import user_record_schema


class RecordHandler:

    def __init__(self, record_usecase):
        self.usecase = record_usecase

    async def submit_data(self, request):
        # mb this 2 types of exception need to move to middleware
        try:
            data = user_record_schema.load(await request.json())
        except JSONDecodeError:
            return web.json_response(status=HTTPStatus.BAD_REQUEST)
        except ValidationError as e:
            return web.json_response(data=e.messages, status=HTTPStatus.BAD_REQUEST)

        # ensure that data will be saved even if client close connection.
        await asyncio.shield(self.usecase.create(data))
        await asyncio.sleep(10)
        return web.json_response(status=HTTPStatus.CREATED)
