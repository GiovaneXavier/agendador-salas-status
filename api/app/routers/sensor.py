from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import verify_token
from app.database import get_db
from app.models.room_state import RoomSensorState, SensorEventLog
from app.schemas.sensor import SensorPayload
from app.services import status_service
from app.services.websocket_manager import manager

router = APIRouter(prefix="/sensor", tags=["sensor"])


@router.post("/{room_id}", dependencies=[Depends(verify_token)])
async def receive_sensor_event(room_id: str, payload: SensorPayload, db: AsyncSession = Depends(get_db)):
    sensor = await db.scalar(select(RoomSensorState).where(RoomSensorState.room_id == room_id))

    if not sensor:
        sensor = RoomSensorState(
            room_id=room_id,
            room_name=payload.room_name or room_id,
            presence=payload.presence,
        )
        db.add(sensor)
    else:
        sensor.presence = payload.presence
        if payload.room_name:
            sensor.room_name = payload.room_name

    await db.commit()
    await db.refresh(sensor)

    broadcast = await status_service.build_broadcast(db, room_id)
    if broadcast:
        await manager.broadcast(broadcast.model_dump(mode="json"))
        db.add(SensorEventLog(
            room_id=room_id,
            room_name=sensor.room_name,
            presence=payload.presence,
            status=broadcast.status,
        ))
        await db.commit()

    return {"ok": True, "room_id": room_id, "presence": payload.presence}
