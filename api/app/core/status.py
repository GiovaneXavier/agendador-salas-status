from datetime import datetime
from enum import Enum


class RoomStatus(str, Enum):
    LIVRE = "LIVRE"
    RESERVADO = "RESERVADO"
    OCUPADO = "OCUPADO"
    USO_NAO_AGENDADO = "USO_NAO_AGENDADO"


STATUS_COLOR = {
    RoomStatus.LIVRE: "#22c55e",           # verde
    RoomStatus.RESERVADO: "#f59e0b",       # amarelo
    RoomStatus.OCUPADO: "#ef4444",         # vermelho
    RoomStatus.USO_NAO_AGENDADO: "#a855f7", # roxo
}

STATUS_LABEL = {
    RoomStatus.LIVRE: "Livre",
    RoomStatus.RESERVADO: "Reservado",
    RoomStatus.OCUPADO: "Ocupado",
    RoomStatus.USO_NAO_AGENDADO: "Uso não agendado",
}


def calculate_status(presence: bool, has_active_booking: bool) -> RoomStatus:
    if presence and not has_active_booking:
        return RoomStatus.USO_NAO_AGENDADO
    if presence:
        return RoomStatus.OCUPADO
    if has_active_booking:
        return RoomStatus.RESERVADO
    return RoomStatus.LIVRE


def is_booking_active(start_time: datetime, end_time: datetime) -> bool:
    now = datetime.now()
    return start_time <= now <= end_time
