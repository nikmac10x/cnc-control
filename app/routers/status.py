import datetime

from fastapi import APIRouter


router = APIRouter()


@router.get("/motors/{id}/status")
async def get_motor_status(motor_id: int):


    motor_status = {
      "requestId": "string",
      "response": {
          "id": motor_id,
          "location": "на первом конвеере за углом",
          "status": "green",
          "statusDate": datetime.datetime.now(),
          "statusDescription": "мотор не найден",
          "statusRaw": "string",
          "extension": {
            "additionalProp1": {}
          }
      }
    }
    return motor_status


@router.get("/motors/all/status")
async def get_all_motors_status():
    motors_status = {
      "requestId": "string",
      "response": [
        {
          "id": 1,
          "location": "на первом конвеере за углом",
          "status": "green",
          "statusDate": "2024-03-22T18:02:27.879Z",
          "statusDescription": "мотор не найден",
          "statusRaw": "string",
          "extension": {
            "additionalProp1": {}
          }
        }
      ]
    }
    return motors_status
