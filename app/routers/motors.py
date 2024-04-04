from fastapi import APIRouter

router = APIRouter()

example_motor = {
    "id": 1,
    "location": "на первом конвеере за углом",
    "ip": "192.168.1.133",
    "port": 502,
    "status": "green",
}


@router.get("/motors")
async def get_motors():
    motors = [example_motor]
    return motors


@router.get("/motors/{motor_id}")
async def get_motor(motor_id: int):
    motor = example_motor
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
