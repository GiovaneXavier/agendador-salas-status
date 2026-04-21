from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.room_state import BookingCache
from app.schemas.booking import BookingWebhookPayload
from app.services import status_service
from app.services.websocket_manager import manager

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.post("/booking")
async def booking_webhook(payload: BookingWebhookPayload, db: AsyncSession = Depends(get_db)):
    if payload.event == "cancelled":
        booking = await db.scalar(
            select(BookingCache).where(BookingCache.booking_id == payload.booking_id)
        )
        if booking:
            await db.delete(booking)
    else:
        booking = await db.scalar(
            select(BookingCache).where(BookingCache.booking_id == payload.booking_id)
        )
        if not booking:
            booking = BookingCache(
                booking_id=payload.booking_id,
                room_id=payload.room_id,
                username=payload.username,
                start_time=payload.start_time,
                end_time=payload.end_time,
            )
            db.add(booking)
        else:
            booking.start_time = payload.start_time
            booking.end_time = payload.end_time
            booking.username = payload.username

    await db.commit()

    broadcast = await status_service.build_broadcast(db, payload.room_id)
    if broadcast:
        await manager.broadcast(broadcast.model_dump(mode="json"))

    return {"ok": True, "event": payload.event, "booking_id": payload.booking_id}
