class Bike:
    def __init__(self, id, brand, status ='available'):
        self.id = id
        self.brand = brand


import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


#vuokrattavat tuotteet
class ItemModel(Base):
    __tablename__ = 'item'

    id = Column(String, primary_key=True, default=generate_uuid)
    #order_id = Column(Integer, ForeignKey('order.id'))
    product = Column(String, nullable=False)
    size = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    def dict(self):
        return {
            'id': self.id,
            'product': self.product,
            'size': self.size,
            'quantity': self.quantity
        }

#asiakkaat
class ItemModel(Base):
    __tablename__ = 'item'

    id = Column(String, primary_key=True, default=generate_uuid)
    #order_id = Column(Integer, ForeignKey('order.id'))
    product = Column(String, nullable=False)
    size = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    def dict(self):
        return {
            'id': self.id,
            'product': self.product,
            'size': self.size,
            'quantity': self.quantity
        }


#vuokratut kohteet
class RentalModel(Base):
    __tablename__ = 'rental'

    id = Column(String, primary_key=True, default=generate_uuid)
    items = relationship('ItemModel', backref='rental')
    status = Column(String, nullable=False, default='created')
    created = Column(DateTime, default=datetime.utcnow)
    schedule_id = Column(String)
    delivery_id = Column(String)

    def dict(self):
        return {
            'id': self.id,
            'items': [item.dict() for item in self.items],
            'status': self.status,
            'created': self.created,
            'schedule_id': self.schedule_id,
            'delivery_id': self.delivery_id,
        }

class MaintenanceModel(Base):
    __tablename__ = 'maintenance'

    id = Column(String, primary_key=True, default=generate_uuid)
    # items = relationship('ItemModel', backref='rental')
    status = Column(String, nullable=False, default='created')
    created = Column(DateTime, default=datetime.utcnow)
    schedule_id = Column(String)
    delivery_id = Column(String)

    def dict(self):
        return {
            'id': self.id,
            #'items': [item.dict() for item in self.items],
            'status': self.status,
            'created': self.created,
            'schedule_id': self.schedule_id,
            'delivery_id': self.delivery_id,
        }

#vuokrattavat tuotteet
class ItemModel(Base):
    __tablename__ = 'item'

    id = Column(String, primary_key=True, default=generate_uuid)
    order_id = Column(Integer, ForeignKey('order.id'))
    product = Column(String, nullable=False)
    size = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    def dict(self):
        return {
            'id': self.id,
            'product': self.product,
            'size': self.size,
            'quantity': self.quantity
        }