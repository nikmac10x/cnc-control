from fastapi import FastAPI

from app.routers import motors, status, control

app = FastAPI()

router_parameters = dict(prefix="/api")
app.include_router(motors.router, tags=["motors"], **router_parameters)
app.include_router(status.router, tags=["status"], **router_parameters)
app.include_router(control.router, tags=["control"], **router_parameters)
