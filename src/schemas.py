from marshmallow import Schema, fields, validate, EXCLUDE

from .db import RECORD_NAME_MAX_LENGTH


class UserRecordSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(max=RECORD_NAME_MAX_LENGTH))
    age = fields.Integer(required=True)


user_record_schema = UserRecordSchema(unknown=EXCLUDE)
