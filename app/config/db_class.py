#FastAPI
from fastapi import HTTPException

#MondoDB Drivers
from pymongo import MongoClient

# env configuration
from app.config.config import settings

#Dump the loaded BSON to valid JSON
from bson import ObjectId

#FastApi
from fastapi import HTTPException,UploadFile

#certify SSL 
import certifi

# ============================================================
# Conection with de Database
# ============================================================

client = MongoClient(settings.URL_CLUSTER_MONGO_DB, tlsCAFile=certifi.where())

class Validator(object):
    def __init__(self) -> None:
        pass
    
    @classmethod
    def is_valid(cls, oid):
        if ObjectId.is_valid(oid):
            return True
        raise HTTPException(422,"Unprocessable Entity")

def select_db():
    __category = "Team9V1"
    restaurant = client.restaurant[__category]
    reservation = client.reservation[__category]
    return [restaurant, reservation]

def Validator_email(plain_email, email_bd):
    if plain_email != email_bd : 
        result = True
        return result
    raise HTTPException(409,"Unauthorized")




