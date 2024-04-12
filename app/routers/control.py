from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas.control import MotorCommandRequest
from app.handlers.motors import MotorHandler
from app.utils import modbus


router = APIRouter()


@router.post("/motors/command")
async def send_command(requestId: str, scheme: MotorCommandRequest, handler: MotorHandler = Depends()):
    motor = handler.get_motor(scheme.id)
    if not motor:
        raise HTTPException(status_code=404, detail=f"Мотора с id={scheme.id} не найдено")

    res, descError = modbus.send_command(motor["ip"], motor["port"], scheme.command, scheme.speed)
    if not res:
        return {
            "requestId": requestId,
            "motor": motor,
            "descError": descError
        }

    return {
        "requestId": requestId,
        "motor": motor
    }
