from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class RoomSensorState(Base):
    __tablename__ = "room_sensor_states"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    room_id: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    room_name: Mapped[str] = mapped_column(String, nullable=False)
    presence: Mapped[bool] = mapped_column(Boolean, default=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())


class SensorEventLog(Base):
    __tablename__ = "sensor_event_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    room_id: Mapped[str] = mapped_column(String, index=True, nullable=False)
    room_name: Mapped[str] = mapped_column(String, nullable=False)
    presence: Mapped[bool] = mapped_column(Boolean, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)  # LIVRE, RESERVADO, OCUPADO, USO_NAO_AGENDADO
    recorded_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), index=True)


class BookingCache(Base):
    __tablename__ = "booking_cache"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    booking_id: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    room_id: Mapped[str] = mapped_column(String, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
