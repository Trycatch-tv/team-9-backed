#Python
import uuid, json

#FastAPI
from fastapi import FastAPI, APIRouter, status, HTTPException
from fastapi import Path

# ============================================================
# Definitions Router:

reservation_router_app = APIRouter(
    prefix="/reservation",
    tags=["Manage Reservation's"]
)

# ============================================================

# ============================================================
# Path operations, Parthner
# ============================================================

@reservation_router_app.get(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Get all reservations"  
        )
def get_all_tables_restaurant():
    return {"get":"Get all rerservations"}

@reservation_router_app.post(
        "/",
        status_code=status.HTTP_200_OK,
        summary="Create a new reservation"  
        )
def post_a_table_restaurant():
    return {"post":"create new reservation"}

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