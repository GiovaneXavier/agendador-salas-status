#pragma once

// ── Wi-Fi ──────────────────────────────────────────────────────────────────
#define WIFI_SSID     "NOME_DA_REDE"
#define WIFI_PASSWORD "SENHA_DA_REDE"

// ── Identificação da sala ──────────────────────────────────────────────────
// Deve bater com o room_id no sistema de agendamento (ex: UUID do Laravel)
#define ROOM_ID   "sala-carvalho"
#define ROOM_NAME "Sala Carvalho"

// ── FastAPI Room Status Service ────────────────────────────────────────────
#define FASTAPI_HOST "192.168.1.100"   // IP do servidor FastAPI na rede local
#define FASTAPI_PORT 9000

// ── Hardware ───────────────────────────────────────────────────────────────
#define PIR_PIN        14    // GPIO conectado ao OUT do HC-SR501
#define LED_STATUS_PIN 2     // LED onboard (azul) — pisca ao enviar dados

// ── Intervalos (ms) ────────────────────────────────────────────────────────
#define PIR_READ_INTERVAL_MS     500    // leitura do sensor a cada 500ms
#define HEARTBEAT_INTERVAL_MS    30000  // envia estado mesmo sem mudança a cada 30s
#define WIFI_RECONNECT_TIMEOUT_MS 10000 // tenta reconectar Wi-Fi a cada 10s
