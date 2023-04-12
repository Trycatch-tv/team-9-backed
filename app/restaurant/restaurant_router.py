#Python
import uuid, json

#FastAPI
from fastapi import FastAPI, APIRouter, status, HTTPException
from fastapi import Path

#DataBase encoders
from app.config.db import create_a_table

#Models app Waro Colombia(Internal)
from app.models.models import RestaurantTable

# ============================================================
# Definitions Router:

restaurant_router_app = APIRouter(
    prefix="/restaurant",
    tags=["Manage Restaurant table's"]
)

# ============================================================

# ============================================================
# Path operations, Parthner
# ============================================================

@restaurant_router_app.get(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Get all tables restaurant"  
        )
def get_all_tables_restaurant():
    return {"get":"Get all tables restaurant"}

@restaurant_router_app.post(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Create table restaurant"  
        )
def post_a_table_restaurant(restaurant_table:RestaurantTable):
    response = create_a_table(restaurant_table.dict()) 
    if response:
        return response
    raise HTTPException(404,"Error")

@restaurant_router_app.put(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Update table restaurant"  
        )
def update_a_table_restaurant():
    return {"edit":"edit tables"}

@restaurant_router_app.delete(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Delete table restaurant"  
        )
def delete_a_table_restaurant():
    return {"delete":"delete a table"}