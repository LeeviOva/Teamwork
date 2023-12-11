import marshmallow as ma
from marshmallow import Schema, fields, validate

from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

# from pydantic import BaseModel, Extra, conint, conlist, validator


class Size(Enum):
    child = 'child'
    junior = 'junior'
    adult_small = 'small'
    adult_medium = 'medium'
    adult_large = 'large'


class User(Enum):
    male = 'male'
    female = 'female'

# vuokrauksen ja huollon tilavaihtoehdot
class Status(Enum):
    created = 'created' # vuokraus/huoltotilaus
    reserved = 'reserved' # vuokraus
    paid = 'paid' # vuokraus
    delivered = 'delivered' # vuokraus
    cancelled = 'cancelled' # vuokraus
    returned = 'returned' # vuokraus
    delayed = 'delayed' # vuokraus
    pending = 'pending' # huolto
    in_progress = 'in_progress' # huolto
    ready = 'ready' # huolto

class BikeStatus(Enum):
    available = 'available'
    reserved = 'reserved'
    under_maintenance = 'under_maintenance'
    removed = 'removed'

# class BikeSchema(ma.Schema):
#     id = fields.Int(dump_only = True)
#     brand = fields.Str(required = True)
#     status = fields.Str(dump_only = True)

class BikeQuerySchema(ma.Schema):
    name = ma.fields.String()

class BikeSchema(ma.Schema):
    id = fields.UUID(required=True)
    brand = fields.String(required=True)
    size = fields.String(
        required=True,
        validate=validate.OneOf(["child", "junior","small", "medium", "large"]),
    )
    user = fields.String(
        required=True,
        validate=validate.OneOf(["male", "female"]),
    )

    bike_status = fields.String(
        required=True,
        validate=validate.OneOf(["available", "reserved", "under_maintenance", "removed"]),
    )
    
class BikeQuerySchema(ma.Schema):
    name = ma.fields.String()