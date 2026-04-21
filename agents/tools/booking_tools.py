import os
from datetime import date
import httpx
from langchain_core.tools import tool

BOOKING_API_URL = os.getenv("BOOKING_API_URL", "http://localhost:8000/api")


@tool
def get_all_rooms() -> str:
    """Lista todas as salas cadastradas no sistema de agendamento."""
    resp = httpx.get(f"{BOOKING_API_URL}/rooms", timeout=10)
    resp.raise_for_status()
    rooms = resp.json()
    lines = [f"- {r['name']} (id={r['id']}, capacidade={r.get('capacity', '?')})" for r in rooms]
    return "\n".join(lines) if lines else "Nenhuma sala encontrada."


@tool
def get_bookings(room_id: str, date_str: str = "") -> str:
    """
    Retorna as reservas de uma sala em uma data específica.
    date_str deve estar no formato YYYY-MM-DD. Se omitido, usa hoje.
    """
    target_date = date_str or date.today().isoformat()
    resp = httpx.get(
        f"{BOOKING_API_URL}/bookings",
        params={"room_id": room_id, "date": target_date},
        timeout=10,
    )
    resp.raise_for_status()
    bookings = resp.json()
    if not bookings:
        return f"Sem reservas para sala '{room_id}' em {target_date}."
    lines = [
        f"  {b['start_time']}–{b['end_time']} | {b.get('username', '?')}"
        for b in bookings
    ]
    return f"Reservas de '{room_id}' em {target_date}:\n" + "\n".join(lines)
