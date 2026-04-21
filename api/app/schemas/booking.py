from datetime import datetime

from pydantic import BaseModel


class BookingWebhookPayload(BaseModel):
    event: str  # "created" | "extended" | "cancelled"
    booking_id: str
    room_id: str
    username: str
    start_time: datetime
    end_time: datetime
