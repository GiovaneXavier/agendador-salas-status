# Arquitetura do Sistema

## Topologia

```
[ESP32 + PIR]  →  Wi-Fi  →  FastAPI (Python)
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
     [Tablet porta]      [React Totem]         [TV Recepção]
     (kiosk Android,     (badge status         (rota /dashboard
      WebSocket)          no RoomRow)           no mesmo React)

     [Laravel Agendador]  →  webhook domain events  →  FastAPI
```

## Comunicação

- **ESP32 → FastAPI:** `POST /sensor/{room_id}` via HTTP sobre Wi-Fi
- **FastAPI → Displays:** WebSocket `/ws` broadcast em tempo real
- **Laravel → FastAPI:** HTTP POST webhook disparado nos domain events (BookingCreated, BookingExtended, BookingCancelled)

## Lógica dos 4 estados

```
presença=false, reserva=false  →  LIVRE
presença=false, reserva=true   →  RESERVADO
presença=true,  reserva=any    →  OCUPADO
presença=true,  reserva=false  →  USO_NAO_AGENDADO
```

## Hardware por sala

- ESP32 DevKit + sensor PIR HC-SR501
- Tablet Android (Chromium em kiosk mode)
- Rede Wi-Fi dedicada ao sistema
