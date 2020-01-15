
class UserRecordUsecase:

    def __init__(self, record_model, app):
        self.record_model = record_model
        self.app = app

    @property
    def db(self):
        return self.app['db']

    async def create(self, data):
        async with self.db.acquire() as conn:
            # I was trying to return id but I failed.
            # get sqlalchemy.exc.CompileError: RETURNING is not supported by this dialect's statement compiler
            # need to research more
            await conn.execute(self.record_model.insert().values(**data))
            await conn.execute('commit')
