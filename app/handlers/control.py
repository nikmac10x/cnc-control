from fastapi import Depends, HTTPException
from app.repos.motors import MotorRepository
from app.utils import modbus


class ControlHandler:
    def __init__(self, motor_repo: MotorRepository = Depends()):
        self.motor_repo = motor_repo

    def send_command(self, id, command, speed=None):
        motor = self.motor_repo.get(id)
        if not motor:
            raise HTTPException(status_code=404, detail=f"Мотора с id = {id} не найдено")
        res, descError = modbus.send_command(motor["ip"], motor["port"], command, speed)
        if not res:
            return {
                "motor": motor,
                "isError": True,
                "descError": descError
            }

        return {
            "motor": motor,
            "isError": False,
            "descError": ""
        }
