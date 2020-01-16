import asyncio
from http import HTTPStatus
from json.decoder import JSONDecodeError

from aiohttp import web
from marshmallow import ValidationError

from .schemas import user_record_schema
from .utils import logger, prepare_validation_log_message


class RecordHandler:

    def __init__(self, record_usecase):
        self.usecase = record_usecase

    async def submit_data(self, request):
        try:
            request_data = await request.json()
        except JSONDecodeError:
            return web.json_response(status=HTTPStatus.BAD_REQUEST)

        try:
            data = user_record_schema.load(request_data)
        except ValidationError as e:
            logger.warning(prepare_validation_log_message(request_data, e))
            return web.json_response(data=e.messages, status=HTTPStatus.BAD_REQUEST)

        # ensure that data will be saved even if client close connection.
        await asyncio.shield(self.usecase.create(data))
        # but it will be more clear if add sleep inside shield
        await asyncio.sleep(10)
        return web.json_response(status=HTTPStatus.CREATED)
