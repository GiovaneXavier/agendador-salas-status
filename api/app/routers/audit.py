from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.room_state import SensorEventLog

router = APIRouter(prefix="/audit", tags=["audit"])


@router.get("/history/{room_id}")
async def room_history(
    room_id: str,
    hours: int = Query(default=24, ge=1, le=168),
    db: AsyncSession = Depends(get_db),
):
    since = datetime.now() - timedelta(hours=hours)
    events = (await db.scalars(
        select(SensorEventLog)
        .where(and_(SensorEventLog.room_id == room_id, SensorEventLog.recorded_at >= since))
        .order_by(SensorEventLog.recorded_at.asc())
    )).all()

    return [
        {
            "room_id": e.room_id,
            "room_name": e.room_name,
            "presence": e.presence,
            "status": e.status,
            "recorded_at": e.recorded_at.isoformat(),
        }
        for e in events
    ]


@router.get("/unscheduled")
async def unscheduled_usage(
    hours: int = Query(default=24, ge=1, le=168),
    db: AsyncSession = Depends(get_db),
):
    since = datetime.now() - timedelta(hours=hours)
    events = (await db.scalars(
        select(SensorEventLog)
        .where(and_(
            SensorEventLog.status == "USO_NAO_AGENDADO",
            SensorEventLog.recorded_at >= since,
        ))
        .order_by(SensorEventLog.recorded_at.asc())
    )).all()

    by_room: dict[str, list] = {}
    for e in events:
        by_room.setdefault(e.room_id, []).append({
            "status": e.status,
            "presence": e.presence,
            "recorded_at": e.recorded_at.isoformat(),
        })

    return {
        "period_hours": hours,
        "since": since.isoformat(),
        "rooms": [
            {"room_id": room_id, "room_name": events[0]["status"] and room_id, "occurrences": len(evs), "events": evs}
            for room_id, evs in by_room.items()
        ],
    }


@router.get("/anomalies")
async def sensor_anomalies(
    stuck_minutes: int = Query(default=60, ge=10),
    db: AsyncSession = Depends(get_db),
):
    since = datetime.now() - timedelta(minutes=stuck_minutes)
    events = (await db.scalars(
        select(SensorEventLog)
        .where(SensorEventLog.recorded_at >= since)
        .order_by(SensorEventLog.room_id, SensorEventLog.recorded_at.asc())
    )).all()

    anomalies = []
    by_room: dict[str, list] = {}
    for e in events:
        by_room.setdefault(e.room_id, []).append(e)

    for room_id, room_events in by_room.items():
        statuses = {e.status for e in room_events}
        if len(statuses) == 1 and "OCUPADO" in statuses:
            anomalies.append({
                "room_id": room_id,
                "room_name": room_events[0].room_name,
                "type": "sensor_stuck_occupied",
                "description": f"Sala reportando OCUPADO continuamente há mais de {stuck_minutes} minutos.",
                "since": room_events[0].recorded_at.isoformat(),
            })

    return {"anomalies": anomalies}
