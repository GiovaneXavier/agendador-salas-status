from pydantic import BaseModel


class SensorPayload(BaseModel):
    presence: bool
    room_name: str | None = None
