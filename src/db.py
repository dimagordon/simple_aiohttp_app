import sqlalchemy as sa
from aiomysql.sa import create_engine


RECORD_NAME_MAX_LENGTH = 200
RECORD_CITY_MAX_LENGTH = 200

meta = sa.MetaData()


records = sa.Table(
    'records', meta,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(RECORD_NAME_MAX_LENGTH), nullable=False),
    sa.Column('age', sa.SMALLINT, nullable=False),
    sa.Column('city', sa.String(RECORD_CITY_MAX_LENGTH), nullable=False),
)


class RecordModel:

    def __init__(self, id, name, age, city):
        self.id = id
        self.name = name
        self.age = age
        self.city = city

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }


async def create_db(app):
    db_config = app['config']['mysql']
    return await create_engine(
        user=db_config['user'], db=db_config['database'],
        host=db_config['host'], password=db_config['password']
    )
