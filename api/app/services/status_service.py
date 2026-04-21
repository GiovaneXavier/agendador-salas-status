from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.status import STATUS_COLOR, STATUS_LABEL, calculate_status, is_booking_active
from app.models.room_state import BookingCache, RoomSensorState
from app.schemas.room import ActiveBookingInfo, RoomStatusBroadcast, RoomStatusResponse


async def get_room_status(db: AsyncSession, room_id: str) -> RoomStatusResponse | None:
    sensor = await db.scalar(select(RoomSensorState).where(RoomSensorState.room_id == room_id))
    if not sensor:
        return None

    active_booking = await _get_active_booking(db, room_id)
    status = calculate_status(sensor.presence, active_booking is not None)

    return RoomStatusResponse(
        room_id=room_id,
        room_name=sensor.room_name,
        status=status,
        color=STATUS_COLOR[status],
        label=STATUS_LABEL[status],
        presence=sensor.presence,
        active_booking=active_booking,
        updated_at=sensor.updated_at or datetime.now(),
    )


async def get_all_rooms_status(db: AsyncSession) -> list[RoomStatusResponse]:
    sensors = (await db.scalars(select(RoomSensorState))).all()
    result = []
    for sensor in sensors:
        active_booking = await _get_active_booking(db, sensor.room_id)
        status = calculate_status(sensor.presence, active_booking is not None)
        result.append(RoomStatusResponse(
            room_id=sensor.room_id,
            room_name=sensor.room_name,
            status=status,
            color=STATUS_COLOR[status],
            label=STATUS_LABEL[status],
            presence=sensor.presence,
            active_booking=active_booking,
            updated_at=sensor.updated_at or datetime.now(),
        ))
    return result


async def build_broadcast(db: AsyncSession, room_id: str) -> RoomStatusBroadcast | None:
    room_status = await get_room_status(db, room_id)
    if not room_status:
        return None
    return RoomStatusBroadcast(
        room_id=room_status.room_id,
        status=room_status.status,
        color=room_status.color,
        label=room_status.label,
        presence=room_status.presence,
        active_booking=room_status.active_booking,
    )


async def _get_active_booking(db: AsyncSession, room_id: str) -> ActiveBookingInfo | None:
    bookings = (await db.scalars(
        select(BookingCache).where(BookingCache.room_id == room_id)
    )).all()

    for booking in bookings:
        if is_booking_active(booking.start_time, booking.end_time):
            return ActiveBookingInfo(
                booking_id=booking.booking_id,
                username=booking.username,
                start_time=booking.start_time,
                end_time=booking.end_time,
            )
    return None
