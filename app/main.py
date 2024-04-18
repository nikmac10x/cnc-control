import datetime

from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.routers import motors, control


scheduler = AsyncIOScheduler()
app = FastAPI()

router_parameters = dict(prefix="/api")
app.include_router(motors.router, tags=["motors"], **router_parameters)
app.include_router(control.router, tags=["control"], **router_parameters)

"""
Периодический опрос частотников
"""
@scheduler.scheduled_job('interval', seconds=1)
async def example_heartbeat():
    now = datetime.datetime.now()
    print(f'Time: {now}')


#@app.on_event('startup')
#async def startup_jobs():
#    scheduler.start()
