import asyncio
import datetime

from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.routers import motors, control
from app.repos.motors import MotorRepository


"""
Настройка HTTP API
"""
app = FastAPI()

router_parameters = dict(prefix="/api")
app.include_router(motors.router, tags=["motors"], **router_parameters)
app.include_router(control.router, tags=["control"], **router_parameters)

"""
Периодический опрос частотников
"""
scheduler = AsyncIOScheduler()


@scheduler.scheduled_job('interval', seconds=10)
async def poll_motors():
    repo = MotorRepository()
    motor_list = repo.get_list()

    no_conn = True
    for motor in motor_list:
        no_conn = True

        # опросить мотор
        now = datetime.datetime.now()
        print(f'Poll {motor["id"]}: {now}')

        # обновить статус в бд
        if no_conn:
            motor['status'] = 'failure'
        else:
            motor['status'] = 'success'
        motor['statusDate'] = now
        repo.update_status(motor['id'], motor['status'])


@app.on_event('startup')
async def startup_jobs():
    scheduler.start()
