# Plano de Materiais — Piloto (3 salas)

> Escopo: validar o ciclo completo ESP32 → API → Display em 3 salas reais.  
> Quantidade de salas escolhida para cobrir os 4 estados do sistema com cenários simultâneos.

---

## 1. Hardware por Sala (× 3)

| # | Item | Especificação | Qtd | Preço unit. est. | Total est. |
|---|------|---------------|-----|-----------------|------------|
| 1 | Microcontrolador | ESP32 DevKit V1 (38 pinos) | 3 | R$ 45 | R$ 135 |
| 2 | Sensor de presença | PIR HC-SR501 | 3 | R$ 12 | R$ 36 |
| 3 | Tablet (display porta) | Android 8" mín., Wi-Fi, Chromium suportado — ex.: Samsung Tab A7 Lite / Positivo Tab Q8 | 3 | R$ 550 | R$ 1.650 |
| 4 | Suporte de parede tablet | Fixação na porta/parede, ajustável | 3 | R$ 60 | R$ 180 |
| 5 | Fonte USB 5V 2A | Para alimentar o ESP32 | 3 | R$ 25 | R$ 75 |
| 6 | Cabo USB (micro ou tipo-C) | Compatível com o DevKit escolhido | 3 | R$ 12 | R$ 36 |
| 7 | Jumper wires macho-macho | Para ligação ESP32 ↔ PIR | 1 kit | R$ 15 | R$ 15 |
| 8 | Protoboard 400 pontos | Prototipagem (pode reusar entre salas se não for fixo) | 3 | R$ 18 | R$ 54 |
| **Subtotal sala** | | | | | **R$ 2.181** |

---

## 2. Servidor Local (API FastAPI)

> Para o piloto use um mini PC ou Raspberry Pi na mesma rede.  
> Alternativa zero-custo: notebook existente rodando Docker.

| # | Item | Especificação | Qtd | Preço unit. est. | Total est. |
|---|------|---------------|-----|-----------------|------------|
| 9 | Single-board computer | Raspberry Pi 4 Model B 4 GB (ou equivalente Orange Pi 5 / Radxa) | 1 | R$ 480 | R$ 480 |
| 10 | Cartão SD | 32 GB Classe 10 / A1 | 1 | R$ 50 | R$ 50 |
| 11 | Fonte oficial RPi 5V 3A | USB-C com proteção de corrente | 1 | R$ 70 | R$ 70 |
| 12 | Case para RPi 4 | Com dissipadores passivos | 1 | R$ 45 | R$ 45 |
| **Subtotal servidor** | | | | | **R$ 645** |

---

## 3. Display Recepção (TV / Dashboard)

| # | Item | Especificação | Qtd | Preço unit. est. | Total est. |
|---|------|---------------|-----|-----------------|------------|
| 13 | TV ou Monitor | 32"–43" com entrada HDMI — verificar se já existe | 1 | R$ 900 | R$ 900 |
| 14 | Cabo HDMI | 2 m | 1 | R$ 25 | R$ 25 |
| 15 | Chromecast / Fire TV Stick | Para renderizar o `/dashboard` sem RPi extra | 1 | R$ 220 | R$ 220 |
| **Subtotal recepção** | | | | | **R$ 1.145** |

---

## 4. Infraestrutura de Rede

| # | Item | Especificação | Qtd | Preço unit. est. | Total est. |
|---|------|---------------|-----|-----------------|------------|
| 16 | Roteador Wi-Fi dedicado | Dual-band 2.4/5 GHz — isola tráfego IoT | 1 | R$ 180 | R$ 180 |
| 17 | Régua de tomadas | 4–6 bocas, com proteção DPS | 2 | R$ 45 | R$ 90 |
| 18 | Cabo de rede CAT5e | Conexão RPi ao switch/roteador, 2 m | 1 | R$ 20 | R$ 20 |
| **Subtotal rede** | | | | | **R$ 290** |

---

## 5. Insumos e Acabamento

| # | Item | Qtd | Preço unit. est. | Total est. |
|---|------|-----|-----------------|------------|
| 19 | Caixa de embutir ABS | Para encapsular ESP32 + PIR na sala | 3 | R$ 18 | R$ 54 |
| 20 | Fita dupla-face extra-forte | Fixação de caixas e cabos | 1 rolo | R$ 15 | R$ 15 |
| 21 | Abraçadeiras de nylon | Organização de cabos | 1 pacote | R$ 10 | R$ 10 |
| **Subtotal acabamento** | | | | | **R$ 79** |

---

## Resumo de Investimento

| Categoria | Total estimado |
|-----------|---------------|
| Hardware por sala (3×) | R$ 2.181 |
| Servidor local (API) | R$ 645 |
| Display recepção | R$ 1.145 |
| Infraestrutura de rede | R$ 290 |
| Insumos e acabamento | R$ 79 |
| **TOTAL PILOTO** | **R$ 4.340** |

> 💡 **Reduções possíveis:**
> - Servidor: se houver notebook disponível, elimina R$ 645.
> - TV recepção: se já existir, elimina R$ 900–R$ 1.125.
> - Tablets: modelos básicos (Positivo, Multilaser) reduzem para ~R$ 350 un.

---

## Fluxo de Montagem Sugerido

```
1. Configurar servidor (RPi / notebook) + subir FastAPI via Docker
2. Flashear firmware no ESP32 e testar POST /sensor/{room_id} na bancada
3. Fixar ESP32 + PIR na sala 1 — validar detecção de presença
4. Configurar tablet em kiosk mode — apontar para /display/{room_id}
5. Repetir salas 2 e 3
6. Conectar webhook do Laravel ao endpoint da FastAPI
7. Configurar TV de recepção apontando para /dashboard
8. Executar os 4 cenários de estado para validação
```

---

## Onde Comprar (referências BR)

| Canal | Indicado para |
|-------|--------------|
| [Mercado Livre](https://www.mercadolivre.com.br) | ESP32, PIR, jumpers, caixas ABS |
| [Eletrogate](https://www.eletrogate.com) | Kits IoT, ESP32, protoboard |
| [FilipeFlop](https://www.filipeflop.com) | Componentes eletrônicos com suporte técnico |
| [Amazon BR](https://www.amazon.com.br) | Tablets, fontes, Chromecast |
| [Kabum](https://www.kabum.com.br) | SD card, Raspberry Pi, monitores |
