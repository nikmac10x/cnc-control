from fastapi import APIRouter, Depends, status
from typing import List

from app.schemas.motors import Motor, MotorCreate
from app.handlers.motors import MotorHandler


router = APIRouter()


@router.get("/motors",
            response_model=List[Motor],
            summary="Получение всех доступных моторов",
            description="Получение всех доступных моторов")
async def get_motors(handler: MotorHandler = Depends()):
    return handler.get_motors()


@router.get("/motors/{motor_id}",
            response_model=Motor,
            summary="Получить мотор по id",
            description="Получить мотор по id")
async def get_motor(motor_id: int, handler: MotorHandler = Depends()):
    return handler.get_motor(motor_id)


@router.post("/motors",
             #response_model=Motor,
             summary="Добавить новый мотор",
             description="Добавить новый мотор")
async def post_motor(scheme: MotorCreate, handler: MotorHandler = Depends()):
    return handler.save(scheme)


@router.delete("/motors/{motor_id}",
               status_code=status.HTTP_204_NO_CONTENT,
               summary="Удалить созданный мотор",
               description="Удалить созданный мотор")
async def delete_motor(motor_id: int, handler: MotorHandler = Depends()):
    handler.drop(motor_id)
