#Python
from http.client import OK
from urllib import response
import uuid

#FastApi
from fastapi import HTTPException,UploadFile
import bson

#Models app Waro Colombia(Internal)
from app.models.models import NewRestaurantTable
from app.models.models import NewReserve

#Dump the loaded BSON to valid JSON
from bson import json_util
import json

#Function db
from app.config.db_class import select_db
from app.config.db_class import Validator


# =============================================================
# Manage Restaurant table's functions. Create,fetch and delete
# =============================================================

#Create a new table restaurant
def create_a_table(new_restaurant_table:NewRestaurantTable):
    category_bdd = select_db()
    _id = category_bdd[0].insert_one(dict(new_restaurant_table))
    _id=str(_id.inserted_id)
    return {"_id":_id}


# =============================================================
# Manage Reservation's functions. Create,fetch and delete
# =============================================================

#Create a new reservation
def create_new_reserve(new_reserve:NewReserve):
    category_bdd = select_db()
    _id = category_bdd[1].insert_one(dict(new_reserve))
    _id=str(_id.inserted_id)
    return {"_id":_id}