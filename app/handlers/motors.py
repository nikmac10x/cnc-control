from fastapi import Depends, HTTPException
from app.repos.motors import MotorRepository


class MotorHandler:
    def __init__(self, repo: MotorRepository = Depends()):
        self.repo = repo

    def get_motors(self):
        return self.repo.get_list()

    def get_motor(self, id):
        res = self.repo.get(id)
        if not res:
            raise HTTPException(status_code=404)
        return res

    def save(self, scheme):
        return self.repo.save(scheme)

    def drop(self, id):
        return self.repo.drop(id)

