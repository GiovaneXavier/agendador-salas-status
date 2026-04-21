# Agendador Salas — Room Status System

Sistema de sensoriamento em tempo real para 15 salas internas.
Complementa o sistema de agendamento existente exibindo o status real de cada sala.

## Estados possíveis

| Estado | Descrição |
|---|---|
| `LIVRE` | Sem presença e sem reserva ativa |
| `RESERVADO` | Reserva ativa, sem presença detectada |
| `OCUPADO` | Presença detectada (com ou sem reserva) |
| `USO_NAO_AGENDADO` | Presença detectada sem reserva correspondente |

## Stack

- **Backend:** Python 3.12 + FastAPI + WebSocket
- **Hardware sensor:** ESP32 + PIR
- **Display porta:** Tablet Android (Chromium kiosk)
- **Banco:** SQLite (PoC) → PostgreSQL (produção)

## Estrutura

```
api/       # FastAPI — Room Status Service
firmware/  # ESP32 — leitura PIR e envio HTTP
docs/      # Diagramas de arquitetura e pinout
```

## Git Flow

- `main` → produção
- `develop` → integração
- `feature/sprint-1` → Sprint 1: FastAPI core + Laravel webhooks
- `feature/sprint-2` → Sprint 2: React badge + dashboard
- `feature/sprint-3` → Sprint 3: ESP32 firmware + tablet kiosk
