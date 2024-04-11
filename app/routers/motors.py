from fastapi import APIRouter, Depends
from typing import List

from app.schemas.motors import MotorsRequest, MotorsResponse, MotorsCreateRequest, Motor
from app.handlers.motors import MotorHandler


router = APIRouter()


@router.get("/motors",
            response_model=MotorsResponse)
async def get_motors(requestId: str, handler: MotorHandler = Depends()):
    motors = handler.get_motors()
    return {"requestId": requestId, "motors": motors}


@router.get("/motors/{motor_id}")
async def get_motor(motor_id: int, requestId: str, handler: MotorHandler = Depends()):
    return {"requestId": requestId, "motor": handler.get_motor(motor_id)}


@router.post("/motors")
async def post_motor(requestId: str, scheme: MotorsCreateRequest, handler: MotorHandler = Depends()):
    return {"requestId": requestId, "motor": handler.save(scheme.motor)}


@router.delete("/motors/{motor_id}")
async def delete_motor(motor_id: int, requestId: str, handler: MotorHandler = Depends()):
    handler.drop(motor_id)
    return {"requestId": requestId}
