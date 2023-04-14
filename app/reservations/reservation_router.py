#Python
import uuid, json

#FastAPI
from fastapi import FastAPI, APIRouter, status, HTTPException
from fastapi import Path

#DataBase encoders
from app.config.db import create_new_reserve

#Models app Team 9 (Internal)
from app.models.models import NewReserve

# ============================================================
# Definitions Router:

reservation_router_app = APIRouter(
    prefix="/reservation",
    tags=["Manage Reservation's"]
)

# ============================================================

# ============================================================
# Path operations, reservation user
# ============================================================

#Create a new reservation
@reservation_router_app.post(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Create a new reservation"  
        )
def post_a_table_restaurant(new_reserve:NewReserve):
    response = create_new_reserve(new_reserve.dict()) 
    if response:
        return response
    raise HTTPException(404,"Error")


@reservation_router_app.get(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Get all reservations"  
        )
def get_all_tables_restaurant():
    return {"get":"Get all rerservations"}

@reservation_router_app.put(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Update reservation"  
        )
def update_a_table_restaurant():
    return {"edit":"update reservation"}

@reservation_router_app.delete(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Delete reservations"  
        )
def delete_a_table_restaurant():
    return {"delete":"delete a reservation"}