from aiohttp import web

from .views import RecordHandler
from .usecases import UserRecordUsecase
from .db import records
from .utils import setup_cors
from . import settings


def setup(app: web.Application):
    #  need remove handler init from here
    record_handler = RecordHandler(
        record_usecase=UserRecordUsecase(records, app)
    )
    # app.router.add_get('/', record_handler.index)
    app.router.add_post('/api/v1/submit-record/', record_handler.submit_data)

    if settings.DEBUG:
        setup_cors(app)
