# Esquema de Montagem — ESP32 + PIR HC-SR501

## Diagrama de Conexão

```
                        ┌─────────────────────────────┐
                        │      ESP32 DevKit V1         │
                        │                              │
              ┌─────────┤ 5V (VIN)          GPIO13 ├──────────┐
              │         │                              │          │
              │    ┌────┤ GND               GPIO12 │  │          │
              │    │    │                              │          │
              │    │    │         ...                  │          │
              │    │    └─────────────────────────────┘          │
              │    │               │                              │
              │    │            USB-C                             │
              │    │          (5V / PC)                           │
              │    │                                              │
              │    │    ┌──────────────────┐                      │
              │    │    │  PIR HC-SR501    │                      │
              │    └────┤ GND              │                      │
              │         │                  │                      │
              └─────────┤ VCC              │                      │
                        │                  │                      │
                        │ OUT ─────────────┘──────────────────────┘
                        │                  │
                        └──────────────────┘
```

---

## Conexões — Tabela Resumo

| Fio | PIR HC-SR501 | ESP32 DevKit V1 | Cor sugerida |
|-----|-------------|-----------------|-------------|
| Alimentação | VCC | 5V (VIN) | Vermelho |
| Terra | GND | GND | Preto |
| Sinal | OUT | GPIO 13 | Amarelo |

---

## Diagrama Visual Detalhado

```
   FONTE USB 5V
   ┌──────────┐
   │  ⚡ 5V   │
   └────┬─────┘
        │ cabo USB
        │
   ┌────▼──────────────────────────────────────────────────┐
   │                  ESP32 DevKit V1                       │
   │                                                        │
   │  ┌──┐                                          ┌──┐   │
   │  │EN│  ┌────────────────────────────────────┐  │23│   │
   │  ├──┤  │                                    │  ├──┤   │
   │  │VP│  │         ___________                │  │22│   │
   │  ├──┤  │        |           |               │  ├──┤   │
   │  │VN│  │        |  ESP32    |               │  │TX│   │
   │  ├──┤  │        |  WROOM    |               │  ├──┤   │
   │  │34│  │        |___________|               │  │RX│   │
   │  ├──┤  │                                    │  ├──┤   │
   │  │35│  └────────────────────────────────────┘  │21│   │
   │  ├──┤                                          ├──┤   │
   │  │32│                                          │19│   │
   │  ├──┤                                          ├──┤   │
   │  │33│                                          │18│   │
   │  ├──┤                                          ├──┤   │
   │  │25│                                          │05│   │
   │  ├──┤                                          ├──┤   │
   │  │26│                                          │17│   │
   │  ├──┤                                          ├──┤   │
   │  │27│                                          │16│   │
   │  ├──┤                                          ├──┤   │
   │  │14│                                          │04│   │
   │  ├──┤                                          ├──┤   │
   │  │12│◄────── (reserva)               GPIO13 ──►│13│◄──┼──── SINAL PIR
   │  ├──┤                                          ├──┤   │
   │  │GND│◄───── GND PIR ◄────────────────── GND ──┤GND│  │
   │  ├──┤                                          ├──┤   │
   │  │15│                                          │VIN│──┼──── VCC PIR (5V)
   │  ├──┤                                          ├──┤   │
   │  │02│                                          │3V3│   │
   │  ├──┤                                          ├──┤   │
   │  │00│                                          │EN │   │
   │  └──┘                                          └──┘   │
   │                      [ USB-C ]                        │
   └────────────────────────┬───────────────────────────────┘
                            │
                         Fonte 5V

```

---

## PIR HC-SR501 — Pinout

```
        ┌─────────────────────────────┐
        │                             │
        │   ╔═══════════════════╗     │
        │   ║                   ║     │
        │   ║   Lente Fresnel   ║     │
        │   ║    (dome branco)  ║     │
        │   ╚═══════════════════╝     │
        │                             │
        │  [Sens.]         [Delay]    │  ← Trimpots de ajuste
        │                             │
        └──────────────────────────────┘
               │       │       │
              VCC     OUT     GND
           (5–12V)  (3.3V)  (terra)

        ┌───────┬──────────────────────────────────────┐
        │ Pino  │ Descrição                             │
        ├───────┼──────────────────────────────────────┤
        │ VCC   │ Alimentação 5V (do ESP32 VIN)         │
        │ OUT   │ Sinal digital: HIGH=presença detectada│
        │ GND   │ Terra                                 │
        └───────┴──────────────────────────────────────┘
```

---

## Ajustes do Trimpot no PIR

```
   PIR HC-SR501 — Vista superior

   ┌─────────────────────────────────┐
   │          ┌───────────┐          │
   │          │   Lente   │          │
   │          └───────────┘          │
   │                                  │
   │   [Sx]────────────    ────────[Tx]│
   │    Sensibilidade          Delay   │
   │   (↑ = mais range)   (↑ = + tempo)│
   └──────────────────────────────────┘

   Recomendação para o piloto:
   • Sensibilidade: 3/4 para a direita (~5–7m de alcance)
   • Delay: mínimo (1/4 para a esquerda) → resposta rápida (~3s)
```

---

## Montagem na Caixa (impressão 3D)

```
   Vista lateral da caixa impressa:

   ┌─────────────────────────────────────┐
   │  ┌──────────┐    ┌───────────────┐  │
   │  │   ESP32  │    │  PIR HC-SR501 │  │  ← fixados com fita dupla-face
   │  │  DevKit  │    │  (dome virado │  │
   │  └──────────┘    │   para fora)  │  │
   │                  └───────────────┘  │
   │                        ║            │
   │       ┌────────────────╝            │
   │       │  abertura para dome do PIR  │  ← furo circular na tampa
   └───────┴─────────────────────────────┘
                │
           parede/porta
         (fita dupla-face)

   Dimensões sugeridas da caixa: 90mm × 60mm × 35mm
```

---

## Checklist de Montagem

```
[ ] 1. Imprimir caixa na impressora 3D
[ ] 2. Conectar PIR ao ESP32 (3 fios: VCC, GND, OUT → GPIO13)
[ ] 3. Testar na bancada antes de fixar (LED do PIR pisca ao detectar)
[ ] 4. Flashear firmware com SSID/senha da rede e IP do servidor
[ ] 5. Verificar envio do POST /sensor/{room_id} via monitor serial
[ ] 6. Fixar caixa na parede ao lado da porta (~1,5m de altura)
[ ] 7. Passar cabo USB até tomada ou régua
[ ] 8. Confirmar status no dashboard
```
