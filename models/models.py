import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

# pyörät
class Bike(Base):
    __tablename__ = 'bike'

    id = Column(String, primary_key=True, default=generate_uuid)
    brand = Column(String, nullable=False)
    size = Column(String, nullable=False)
    user = Column(String, nullable=False) #male/female
    bike_status = Column(String, nullable=False, default='available')

    def dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'size': self.size,
            'user': self.user,
            'bike_status': self.bike_status
        }


#asiakkaat
class Customer(Base):
    __tablename__ = 'customer'

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(String, nullable=False)

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }


#vuokraus
class Rental(Base):
    __tablename__ = 'rental'

    id = Column(String, primary_key=True, default=generate_uuid)
    bike_id = Column(String, ForeignKey('bike.id'))
    customer_id = Column(String, ForeignKey('customer.id'))
    status = Column(String, nullable=False, default='created')
    created = Column(DateTime, default=datetime.utcnow)
    delivery_id = Column(String)

    def dict(self):
        return {
            'id': self.id,
            'bike_id': self.bike_id,
            'customer_id': self.customer_id,
            'status': self.status,
            'created': self.created,
            'delivery_id': self.delivery_id,
        }

#huolto
class Maintenance(Base):
    __tablename__ = 'maintenance'

    id = Column(String, primary_key=True, default=generate_uuid)
    bike_id = Column(String, ForeignKey('bike.id'))
    status = Column(String, nullable=False, default='created')
    created = Column(DateTime, default=datetime.utcnow)
    

    def dict(self):
        return {
            'id': self.id,
            'bike_id': self.bike_id,
            'status': self.status,
            'created': self.created,
        }

    





