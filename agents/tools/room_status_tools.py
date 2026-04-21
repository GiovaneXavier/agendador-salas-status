import os
import httpx
from langchain_core.tools import tool

STATUS_API_URL = os.getenv("STATUS_API_URL", "http://localhost:9000")


@tool
def get_all_rooms_status() -> str:
    """Retorna o status atual (LIVRE/RESERVADO/OCUPADO/USO_NAO_AGENDADO) de todas as salas."""
    resp = httpx.get(f"{STATUS_API_URL}/rooms/status", timeout=10)
    resp.raise_for_status()
    rooms = resp.json()
    lines = [f"- {r['room_name']}: {r['label']} (presença={r['presence']})" for r in rooms]
    return "\n".join(lines) if lines else "Nenhuma sala encontrada."


@tool
def get_room_status(room_id: str) -> str:
    """Retorna o status atual de uma sala específica pelo room_id."""
    resp = httpx.get(f"{STATUS_API_URL}/rooms/status/{room_id}", timeout=10)
    if resp.status_code == 404:
        return f"Sala '{room_id}' não encontrada."
    resp.raise_for_status()
    r = resp.json()
    info = f"{r['room_name']}: {r['label']} (presença={r['presence']})"
    if r.get("active_booking"):
        b = r["active_booking"]
        info += f"\n  Reserva ativa: {b['username']} até {b['end_time']}"
    return info


@tool
def get_room_history(room_id: str, hours: int = 24) -> str:
    """Retorna o histórico de eventos do sensor de uma sala nas últimas N horas."""
    resp = httpx.get(f"{STATUS_API_URL}/audit/history/{room_id}", params={"hours": hours}, timeout=10)
    resp.raise_for_status()
    events = resp.json()
    if not events:
        return f"Sem eventos registrados para '{room_id}' nas últimas {hours}h."
    lines = [f"  [{e['recorded_at']}] {e['status']} (presença={e['presence']})" for e in events]
    return f"Histórico de '{room_id}' ({hours}h):\n" + "\n".join(lines)


@tool
def get_unscheduled_usage(hours: int = 24) -> str:
    """Retorna salas com uso não agendado detectado nas últimas N horas. Útil para auditoria."""
    resp = httpx.get(f"{STATUS_API_URL}/audit/unscheduled", params={"hours": hours}, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    rooms = data.get("rooms", [])
    if not rooms:
        return f"Nenhum uso não agendado detectado nas últimas {hours}h."
    lines = [f"- {r['room_id']}: {r['occurrences']} ocorrência(s)" for r in rooms]
    return f"Uso não agendado (últimas {hours}h):\n" + "\n".join(lines)


@tool
def get_sensor_anomalies(stuck_minutes: int = 60) -> str:
    """Detecta sensores com comportamento anômalo, como sensor travado em OCUPADO por muito tempo."""
    resp = httpx.get(f"{STATUS_API_URL}/audit/anomalies", params={"stuck_minutes": stuck_minutes}, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    anomalies = data.get("anomalies", [])
    if not anomalies:
        return "Nenhuma anomalia detectada nos sensores."
    lines = [f"- {a['room_name']}: {a['description']}" for a in anomalies]
    return "Anomalias detectadas:\n" + "\n".join(lines)
