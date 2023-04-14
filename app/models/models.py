#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#Datetime
import datetime

# ============================================================
# Define models, Restarant TEAM 9
# ============================================================

class NewReserve(BaseModel): #Create new reserve
    date_reserve:str = Field( ...,min_length=2,max_length=64,example= "2023-04-12")
    id_table:str = Field(...,min_length=2,max_length=64,example='6438bf0e12a189b6a5c34f4a')
    number_people_reserve:int = Field( ...,example= 10)
    name_reserve_titular:str = Field(...,min_length=2,max_length=100,example='Anderson Arévalo')
    phone_reserve_titular:int = Field(...,example=3142058934)
    email_reserve_titular:EmailStr = Field( ...,example= "hola@warocol.com")
    active_reserve:bool = Field(...,example=False)
    time_reserve:str = Field(...,min_length=2,max_length=64,example='12345678')

class NewRestaurantTable(BaseModel):
    location_table:str = Field(...,min_length=2,max_length=64,example= "3A")
    capacity_table:int = Field( ...,example= 10)
    active_table:bool = Field(...,example=False)
