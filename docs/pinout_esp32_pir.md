# Pinout — ESP32 + HC-SR501

## Conexão física

```
HC-SR501          ESP32 DevKit
─────────         ────────────
VCC       →       5V (VIN)
GND       →       GND
OUT       →       GPIO 14
```

## Diagrama

```
        ┌─────────────┐
        │  HC-SR501   │
        │             │
   5V ──┤ VCC         │
  GND ──┤ GND         │
 GPIO14─┤ OUT         │
        └─────────────┘
             ↕ detecção
          (campo ~7m, 120°)
```

## Configuração do HC-SR501

| Trimpot | Função | Recomendado |
|---|---|---|
| Sensibilidade (esq) | Distância de detecção 3–7m | Meio (4–5m) |
| Tempo (dir) | Tempo de saída HIGH 3s–300s | Mínimo (~3s) |
| Jumper | L (single trigger) / H (repeat) | H (repeat) |

## Configurar em `include/config.h`

```cpp
#define WIFI_SSID     "NOME_DA_REDE"
#define WIFI_PASSWORD "SENHA_DA_REDE"
#define ROOM_ID       "uuid-da-sala-no-laravel"
#define ROOM_NAME     "Nome da Sala"
#define FASTAPI_HOST  "192.168.x.x"   // IP fixo do servidor
#define FASTAPI_PORT  9000
#define PIR_PIN       14
```

## Flash via PlatformIO

```bash
cd firmware/
pio run --target upload
pio device monitor   # monitora serial para debug
```
