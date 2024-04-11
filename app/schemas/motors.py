from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime


class Motor(BaseModel):
    model_config = ConfigDict(from_attributes=True,
                              arbitrary_types_allowed=True
                              )
    id: int
    location: str
    ip: str
    port: int
    status: Optional[str]
    statusDate: Optional[datetime]


class MotorCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True,
                              arbitrary_types_allowed=True
                              )
    location: str
    ip: str
    port: int


class MotorsRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True,
                              arbitrary_types_allowed=True)

    requestId: str


class MotorsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True,
                              arbitrary_types_allowed=True)

    requestId: str
    motors: List[Motor]


class MotorsCreateRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True,
                              arbitrary_types_allowed=True)

    requestId: str
    motor: MotorCreate
