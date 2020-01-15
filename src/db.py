import sqlalchemy as sa
from aiomysql.sa import create_engine


RECORD_NAME_MAX_LENGTH = 200

meta = sa.MetaData()


records = sa.Table(
    'records', meta,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(RECORD_NAME_MAX_LENGTH), nullable=False),
    sa.Column('age', sa.SMALLINT, nullable=False),
)


class Record:

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }


async def create_db(app):
    return await create_engine(
        user='root', db='test_db',
        host='127.0.0.1', password='test_password'
    )
