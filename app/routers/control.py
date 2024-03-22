from fastapi import APIRouter

router = APIRouter()


@router.get("/motors/{id}/control")
async def get_motor_status(motor_id: int):
    motor_status = {}
    return motor_status
