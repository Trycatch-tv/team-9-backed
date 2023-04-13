#Python
from http.client import OK
from urllib import response
import uuid

#FastApi
from fastapi import HTTPException,UploadFile
import bson

#Models app Waro Colombia(Internal)
from app.models.models import RestaurantTable

#Dump the loaded BSON to valid JSON
from bson import json_util
import json

#Function db
from app.config.db_class import select_db
from app.config.db_class import Validator


# =============================================================
# Manage Restaurant table's functions. Create,fetch and delete
# =============================================================

#Create a Parthner
def create_a_table(restaurant_table:RestaurantTable):
    category_bdd = select_db()
    category_bdd[0].insert_one(dict(restaurant_table)) #add to garage products
    return restaurant_table


# =============================================================
# Manage Reservation's functions. Create,fetch and delete
# =============================================================