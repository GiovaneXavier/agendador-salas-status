# Plano de Materiais — Piloto (3 salas)

> Escopo: validar o ciclo completo ESP32 → API → Display em 3 salas reais.  
> Quantidade de salas escolhida para cobrir os 4 estados do sistema com cenários simultâneos.
>
> ✅ **Recursos já disponíveis (não comprar):**
> - Servidor físico próprio — API FastAPI será implantada nele
> - Tablets já existentes — serão reaproveitados como display de porta
> - Impressora 3D própria — caixas de encapsulamento serão impressas internamente

---

## 1. Hardware por Sala (× 3)

| # | Item | Especificação | Qtd | Preço unit. est. | Total est. |
|---|------|---------------|-----|-----------------|------------|
| 1 | Microcontrolador | ESP32 DevKit V1 (38 pinos) | 3 | R$ 45 | R$ 135 |
| 2 | Sensor de presença | PIR HC-SR501 | 3 | R$ 12 | R$ 36 |
| 3 | Fonte USB 5V 2A | Para alimentar o ESP32 | 3 | R$ 25 | R$ 75 |
| 4 | Cabo USB (micro ou tipo-C) | Compatível com o DevKit escolhido | 3 | R$ 12 | R$ 36 |
| 5 | Jumper wires macho-macho | Para ligação ESP32 ↔ PIR | 1 kit | R$ 15 | R$ 15 |
| 6 | Protoboard 400 pontos | Prototipagem na bancada antes de fixar | 3 | R$ 18 | R$ 54 |
| **Subtotal sala** | | | | | **R$ 351** |

---

## 2. Display Recepção (TV / Dashboard)

| # | Item | Especificação | Qtd | Preço unit. est. | Total est. |
|---|------|---------------|-----|-----------------|------------|
| 7 | TV ou Monitor | 32"–43" com entrada HDMI — verificar se já existe | 1 | R$ 900 | R$ 900 |
| 8 | Cabo HDMI | 2 m | 1 | R$ 25 | R$ 25 |
| 9 | Chromecast / Fire TV Stick | Para renderizar o `/dashboard` sem hardware extra | 1 | R$ 220 | R$ 220 |
| **Subtotal recepção** | | | | | **R$ 1.145** |

> 💡 Se já houver TV disponível na recepção, esse bloco inteiro cai para ~R$ 245 (só cabo + Chromecast).

---

## 3. Infraestrutura de Rede

| # | Item | Especificação | Qtd | Preço unit. est. | Total est. |
|---|------|---------------|-----|-----------------|------------|
| 10 | Roteador Wi-Fi dedicado | Dual-band 2.4/5 GHz — isola tráfego IoT dos demais dispositivos | 1 | R$ 180 | R$ 180 |
| 11 | Régua de tomadas | 4–6 bocas, com proteção DPS | 2 | R$ 45 | R$ 90 |
| 12 | Cabo de rede CAT5e | Conexão servidor ao switch/roteador, 2 m | 1 | R$ 20 | R$ 20 |
| **Subtotal rede** | | | | | **R$ 290** |

---

## 4. Insumos e Acabamento

| # | Item | Obs. | Qtd | Preço unit. est. | Total est. |
|---|------|------|-----|-----------------|------------|
| 13 | Filamento PLA/PETG | Para impressão das caixas do ESP32 + PIR na impressora 3D própria | 1 rolo | R$ 80 | R$ 80 |
| 14 | Fita dupla-face extra-forte | Fixação das caixas impressas e organização de cabos | 1 rolo | R$ 15 | R$ 15 |
| 15 | Abraçadeiras de nylon | Organização de cabos nas salas | 1 pacote | R$ 10 | R$ 10 |
| **Subtotal acabamento** | | | | | **R$ 105** |

---

## Resumo de Investimento

| Categoria | Total estimado |
|-----------|---------------|
| Hardware por sala (3×) | R$ 351 |
| Display recepção | R$ 1.145 |
| Infraestrutura de rede | R$ 290 |
| Insumos e acabamento | R$ 105 |
| **TOTAL PILOTO** | **R$ 1.891** |

| Economia com recursos próprios | Valor |
|-------------------------------|-------|
| ~~Servidor (RPi 4 + acessórios)~~ | R$ 645 |
| ~~Tablets (3×)~~ | R$ 1.650 |
| ~~Suportes de parede (3×)~~ | R$ 180 |
| ~~Caixas ABS compradas (3×)~~ | R$ 54 |
| **Total economizado** | **R$ 2.529** |

> 💡 Se a TV de recepção já existir, o custo total cai para **~R$ 991**.

---

## Fluxo de Montagem Sugerido

```
1. Imprimir caixas do ESP32 + PIR na impressora 3D (modelo STL a definir)
2. Implantar FastAPI no servidor físico existente via Docker
3. Flashear firmware no ESP32 e testar POST /sensor/{room_id} na bancada
4. Fixar caixa impressa + ESP32 + PIR na sala 1 — validar detecção
5. Configurar tablet existente em kiosk mode → /display/{room_id}
6. Repetir salas 2 e 3
7. Conectar webhook do Laravel ao endpoint da FastAPI
8. Configurar TV de recepção apontando para /dashboard
9. Executar os 4 cenários de estado para validação final
```

---

## Onde Comprar (referências BR)

| Canal | Indicado para |
|-------|--------------|
| [Mercado Livre](https://www.mercadolivre.com.br) | ESP32, PIR, jumpers, protoboard |
| [Eletrogate](https://www.eletrogate.com) | Kits IoT, ESP32 com suporte técnico |
| [FilipeFlop](https://www.filipeflop.com) | Componentes eletrônicos com documentação |
| [Amazon BR](https://www.amazon.com.br) | Fontes USB, Chromecast, cabos |
| [Kabum](https://www.kabum.com.br) | TV/monitor, filamento PLA/PETG |
