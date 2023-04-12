#creating Schema for validation.

from pydantic import BaseModel


class AddressIn(BaseModel):
    sl_no: int
    name: str
    contact_number: int
    address: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class AddressOut(AddressIn):
    sl_no: int

    class Config:
        orm_mode = True
