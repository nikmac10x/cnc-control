from fastapi import APIRouter, Depends

from app.schemas.control import MotorCommandRequest
from app.handlers.control import ControlHandler


router = APIRouter()


@router.post("/motors/command",
             summary="Отправка команд частотнику",
             description="Отправка команд частотнику с заданным id")
async def send_command(scheme: MotorCommandRequest, handler: ControlHandler = Depends()):
    return handler.send_command(scheme.id, scheme.command, scheme.speed)
