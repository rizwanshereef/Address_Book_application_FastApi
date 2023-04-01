# Defines the model for the Application. Defines the DB details.
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float 

from database import engine,Base


class AddressesModel(Base):
    __tablename__ = "Addresses"

    sl_no = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    contact_number=Column(Integer,nullable=False)
    address = Column(String(255), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

Base.metadata.create_all(engine)
