from pydantic import BaseModel, Field
from typing import Optional


class MotorCommandRequest(BaseModel):
    requestId: str
    id: int
    command: str
    speed: Optional[int] = Field(le=100, ge=0, title="Скорость мотора",
                                 description="Скорость мотора в процентах от 0 до 100")


class MotorCommandResponse(BaseModel):
    requestId: str
