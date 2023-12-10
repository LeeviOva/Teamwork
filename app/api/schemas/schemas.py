import marshmallow as ma
from marshmallow import Schema, fields

class BikeSchema(ma.Schema):
    id = fields.Int(dump_only = True)
    brand = fields.Str(required = True)
    status = fields.Str(dump_only = True)

class BikeQuerySchema(ma.Schema):
    name = ma.fields.String()