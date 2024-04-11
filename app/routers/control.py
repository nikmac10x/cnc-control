from fastapi import APIRouter, HTTPException, status
from pymodbus.client.sync import ModbusTcpClient

from app.schemas.control import MotorCommandRequest


router = APIRouter()


def _control_by_modbus(host, port, command, speed=None):
    client = ModbusTcpClient(host, int(port))
    if not client.connect():
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Нет соединения с устройством")

    feeder_slave_id = 1
    res = None
    if speed is not None:
        speed = speed * 50
        print(f"Set speed is {speed}")
        res = client.write_registers(12288, [speed], unit=feeder_slave_id)
    if res and res.isError():
        print("Ошибка записи частоты")
        #client.close()
        #raise HTTPException(status_code=404)

    if command == "forward":
        res = client.write_registers(8192, [1], unit=feeder_slave_id)
    elif command == "stop":
        res = client.write_registers(8192, [5], unit=feeder_slave_id)

    if res and res.isError():
        print("Ошибка записи команды")
        #client.close()
        #raise HTTPException(status_code=404)

    client.close()


def _status_by_modbus(host, port):
    client = ModbusTcpClient(host, int(port))
    if not client.connect():
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Нет соединения с устройством")

    feeder_slave_id = 1
    res = None
    # чтение состояния и ошибок ЧП
    res = client.read_holding_registers(24576, 3, unit=feeder_slave_id)
    # чтение целевой и текущей частоты частоты
    res = client.read_holding_registers(4352, 2, unit=feeder_slave_id)

    client.close()


@router.post("/motors/command")
async def get_motor_status(scheme: MotorCommandRequest):
    motor = {}
    print("Control", motor["ip"], motor["port"])
    _control_by_modbus(motor["ip"], motor["port"], scheme.command, scheme.speed)

    return {
        "requestId": scheme.requestId
    }
