from marshmallow import Schema, fields
# import built-in validators
from marshmallow.validate import Length, Range


class UserSchema(Schema):
    # Required value shorter than 50 characters
    name = fields.Str(required=True, validate=Length(max=50))
    # Required value shorter than 50 characters
    surname = fields.Str(required=True, validate=Length(max=50))
    # Required value shorter than 12 characters
    identity_number = fields.Int(required=True, validate=Range(min=1))
    

class IDSchema(Schema):
    identity_number = fields.Int(required=True, validate=Range(min=1))