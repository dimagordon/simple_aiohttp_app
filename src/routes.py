from aiohttp import web

from .views import RecordHandler
from .usecases import UserRecordUseCase
from .db import records
from .utils import setup_cors
from . import settings


def setup(app: web.Application):
    record_handler = RecordHandler(
        record_usecase=UserRecordUseCase(records, app)
    )

    # mb need to move /api/v1/ to subapp
    app.router.add_post('/api/v1/submit-record/', record_handler.submit_data)

    if settings.DEBUG:
        setup_cors(app)
