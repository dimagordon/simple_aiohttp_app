from marshmallow import Schema, fields, validate, EXCLUDE

from .db import RECORD_NAME_MAX_LENGTH


class TrimmedString(fields.String):
    def _deserialize(self, value, *args, **kwargs):
        if hasattr(value, 'strip'):
            value = value.strip()
        return super()._deserialize(value, *args, **kwargs)


class UserRecordSchema(Schema):
    name = TrimmedString(required=True, validate=validate.Length(max=RECORD_NAME_MAX_LENGTH))
    age = fields.Integer(required=True)


user_record_schema = UserRecordSchema(unknown=EXCLUDE)
