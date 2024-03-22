from fastapi import APIRouter

router = APIRouter()


@router.get("/motors")
async def get_motors():
    motors = []
    return motors

@router.get("/motors/{motor_id}")
async def get_motor(motor_id: int):
    motor = {}
    return motor


@router.post("/motors")
async def post_motor(scheme):
    motor = {}
    return motor


@router.put("/motors/{motor_id}")
async def put_motor(motor_id: int, scheme):
    motor = {}
    return motor


@router.delete("/motors/{motor_id}")
async def delete_motor(motor_id: int):
    return
