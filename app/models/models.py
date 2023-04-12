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

class RestaurantTable(BaseModel): #Create new table 
    capacidad:int = Field( ...,example= 10)
    ubicacion:str = Field(...,min_length=2,max_length=64,example='3A')
    available:Optional[list] = None
    reserves:Optional[list] = None