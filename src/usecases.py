"""
    For sure we could create another layer of accessing data like dao
    to separate business logic from dbms related stuff. Like dbms engines and f.e. ORMs.
    but this project too simple for this.
"""


class UserRecordUseCase:

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
            # so for now just commit and return None
            await conn.execute(self.record_model.insert().values(**data))
            await conn.execute('commit')
