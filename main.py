# main.py
from typing import List, Optional
from fastapi import FastAPI,Depends, HTTPException
from sqlalchemy.orm import Session, sessionmaker
from geopy.distance import geodesic as GD  
from models import AddressesModel
from schema import AddressIn, AddressOut
from database import SessionLocal
import logging

# Initializing loggers
FORMAT = "%(levelname)s:%(asctime)s:%(message)s"
logging.basicConfig(filename='./log/log_file.log',format=FORMAT, datefmt='%d-%b-%y %H:%M:%S',level=logging.DEBUG)

logging.info('Starting FastApi application')

# Initiating FastApi application
app = FastAPI()

# function to connect to the Database
def get_db():
    logging.info('Connecting to DB')
    db = SessionLocal()
    try:
        yield db
    finally:
        logging.info('Closing Connection')
        db.close()

#default page
@app.get("/")
async def root():
    logging.info('Inside root')
    return {"message": "This is a CRUD api to manage user addresses"}

#Post request to add address to the DB
@app.post('/addresses', response_model=AddressIn)
def create_address(address: AddressIn, db: Session = Depends(get_db)):
    logging.info('Inside POST request /addresses')
    db_address = AddressesModel(name=address.name, contact_number=address.contact_number, address=address.address,
                         latitude=address.latitude, longitude=address.longitude)
# Adding address from the request to DB
    logging.info('Adding address from POST request')
    try:
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        logging.info('Added Address')
    except Exception as e:
        error=e
        raise HTTPException(status_code=404, detail=str(e))
        logging.error(error)
    return db_address

#PUT request to update the exising address
@app.put('/addresses/{address_id}', response_model=AddressIn)
def update_address(address_id: int, address: AddressIn, db: Session = Depends(get_db)):
    logging.info('Inside PUT request /addresses{address_id}')
# Fetching address based on the put request
    db_address = db.query(AddressesModel).filter(AddressesModel.sl_no == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail='Address not found')
        logging.info()
#Updating the address based on the put request
    try:
        db_address.name = address.name
        db_address.contact_number=address.contact_number
        db_address.address = address.address
        db_address.latitude = address.latitude
        db_address.longitude = address.longitude
        db.commit()
        db.refresh(db_address)
    except Exception as e:
        error=e
        raise HTTPException(status_code=404, detail=str(e))
        logging.error(error)
    return db_address

#Delete request to delete address based on ID
@app.delete('/addresses/{address_id}')
def delete_address(address_id: int, db: Session = Depends(get_db)):
# Fetching the address from DB based on the address id from the delete request
    db_address = db.query(AddressesModel).filter(AddressesModel.sl_no == address_id).first()
    if not db_address:
        logging.error('Address not found')
        raise HTTPException(status_code=404, detail='Address not found')
    logging.info('Deleting address:%s',address_id)    
 # Deleting entry from DB
    try:
        db.delete(db_address)
        db.commit()
    except Exception as e:
            error=e
            raise HTTPException(status_code=404, detail=str(e))
            logging.error(error)
    logging.info('Address deleted, exiting DELETE Request')
    return {'message': 'Address deleted'}

# Get request to fetch all the Address from DB
@app.get('/addresses', response_model=List[AddressIn])
def get_addresses(db: Session = Depends(get_db)):
    logging.info('Inside GET request /addresses')
# Fetching all the addresses from DB 
    try:
        addresses = db.query(AddressesModel).all()
        logging.info('Fetched addresses')
    except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))
            logging.error(error)
    logging.info('Exiting GET request /addresses')
    return addresses

#Get request to find nearby address
@app.get("/addresses/nearby",response_model=List[AddressIn])
def read_nearby_addresses(latitude: float, longitude: float, distance: float, db: Session = Depends(get_db)):
    logging.info('Insided GET request /addresses/nearby')
    user_location = (latitude, longitude)
    logging.debug('Location parsed %s:',user_location)
    nearby_addresses = []
 #Fetching all addresses from DB
    try:
        addresses=db.query(AddressesModel).all()
    except Exception as e:
            error=e
            raise HTTPException(status_code=404, detail=str(e))
            logging.error(error)
    logging.info('Comparing with location in DB')
# Calculating distance between locations in DB vs locations from Request and selecting the nearest location based on distance
    for row in addresses:
            logging.debug('Calculated distance:%s',GD(user_location,(row.latitude,row.longitude)).km)
            if GD(user_location,(row.latitude,row.longitude)).km <= distance:
                near_address = row
                nearby_addresses.append(near_address)
                logging.info('Found Location matches within the range')
            if not nearby_addresses:
                raise HTTPException(status_code=404, detail='No nearby address')
                logging.error('No nearby address')
    logging.info('Exiting GET request /addresses/nearby')
    return nearby_addresses