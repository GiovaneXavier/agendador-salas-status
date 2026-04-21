from datetime import datetime

from pydantic import BaseModel

from app.core.status import RoomStatus


class RoomStatusResponse(BaseModel):
    room_id: str
    room_name: str
    status: RoomStatus
    color: str
    label: str
    presence: bool
    active_booking: "ActiveBookingInfo | None"
    updated_at: datetime


class ActiveBookingInfo(BaseModel):
    booking_id: str
    username: str
    start_time: datetime
    end_time: datetime


class RoomStatusBroadcast(BaseModel):
    type: str = "room_status_update"
    room_id: str
    status: RoomStatus
    color: str
    label: str
    presence: bool
    active_booking: "ActiveBookingInfo | None"
