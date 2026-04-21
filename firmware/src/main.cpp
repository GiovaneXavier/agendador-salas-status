#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include "config.h"

static bool lastPresence = false;
static unsigned long lastSentMs = 0;
static unsigned long lastWifiCheckMs = 0;

// ── Wi-Fi ──────────────────────────────────────────────────────────────────

void connectWifi() {
    Serial.printf("[WiFi] Conectando a %s", WIFI_SSID);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    unsigned long start = millis();
    while (WiFi.status() != WL_CONNECTED && millis() - start < WIFI_RECONNECT_TIMEOUT_MS) {
        delay(500);
        Serial.print(".");
    }

    if (WiFi.status() == WL_CONNECTED) {
        Serial.printf("\n[WiFi] Conectado. IP: %s\n", WiFi.localIP().toString().c_str());
    } else {
        Serial.println("\n[WiFi] Falha na conexão. Tentará novamente em breve.");
    }
}

// ── HTTP ───────────────────────────────────────────────────────────────────

void sendPresence(bool presence) {
    if (WiFi.status() != WL_CONNECTED) return;

    String url = String("http://") + FASTAPI_HOST + ":" + FASTAPI_PORT
                 + "/sensor/" + ROOM_ID;

    JsonDocument doc;
    doc["presence"]  = presence;
    doc["room_name"] = ROOM_NAME;

    String body;
    serializeJson(doc, body);

    HTTPClient http;
    http.begin(url);
    http.addHeader("Content-Type", "application/json");

    int code = http.POST(body);

    digitalWrite(LED_STATUS_PIN, HIGH);
    delay(80);
    digitalWrite(LED_STATUS_PIN, LOW);

    if (code > 0) {
        Serial.printf("[HTTP] POST %s → %d | presence=%s\n",
                      url.c_str(), code, presence ? "true" : "false");
    } else {
        Serial.printf("[HTTP] Erro: %s\n", http.errorToString(code).c_str());
    }

    http.end();
    lastSentMs = millis();
}

// ── Setup / Loop ───────────────────────────────────────────────────────────

void setup() {
    Serial.begin(115200);

    pinMode(PIR_PIN, INPUT);
    pinMode(LED_STATUS_PIN, OUTPUT);
    digitalWrite(LED_STATUS_PIN, LOW);

    // Aguarda o HC-SR501 calibrar (recomendado: 30s; reduzido para 2s em dev)
    Serial.println("[PIR] Calibrando sensor...");
    delay(2000);

    connectWifi();

    // Envia estado inicial
    lastPresence = digitalRead(PIR_PIN) == HIGH;
    sendPresence(lastPresence);
}

void loop() {
    unsigned long now = millis();

    // Reconecta Wi-Fi se necessário
    if (now - lastWifiCheckMs >= WIFI_RECONNECT_TIMEOUT_MS) {
        lastWifiCheckMs = now;
        if (WiFi.status() != WL_CONNECTED) {
            Serial.println("[WiFi] Conexão perdida. Reconectando...");
            connectWifi();
        }
    }

    // Lê o sensor PIR
    bool presence = digitalRead(PIR_PIN) == HIGH;
    bool changed  = (presence != lastPresence);
    bool heartbeat = (now - lastSentMs >= HEARTBEAT_INTERVAL_MS);

    if (changed || heartbeat) {
        lastPresence = presence;
        sendPresence(presence);
    }

    delay(PIR_READ_INTERVAL_MS);
}
