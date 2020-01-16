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

    # I have some difficulties with jinja2 template rendering.
    # So I decide to create rest api and add cors to local dev
    # Need to read more about best practices of server rendering
    # But for sure I understand why we could use
    # if request.method == 'get':
    #    ...
    app.router.add_post('/api/v1/submit-record/', record_handler.submit_data)

    if settings.DEBUG:
        setup_cors(app)
