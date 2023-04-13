# ============================================================
# TEAM9 FAST API, HOLA :v
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.restaurant.restaurant_router import restaurant_router_app
from app.reservations.reservation_router import reservation_router_app

import uvicorn

# Initialize the app
app = FastAPI()
app.include_router(restaurant_router_app)
app.include_router(reservation_router_app)

# ============================================================
# MIDDLEWARE TO CONECT
# ============================================================

origins = [ "http://0.0.0.0" ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )


if __name__ == '__main__':
    uvicorn.run(app)
