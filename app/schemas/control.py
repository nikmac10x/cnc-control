from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class MotorCommandCodes(str, Enum):
    """
    Коды команд
    """
    forward = "forward"
    stop = "stop"


class MotorCommandRequest(BaseModel):
    id: int
    command: MotorCommandCodes
    speed: Optional[int] = Field(le=100, ge=0, title="Скорость мотора",
                                 description="Скорость мотора в процентах от 0 до 100")


class MotorCommandResponse(BaseModel):
    requestId: str
