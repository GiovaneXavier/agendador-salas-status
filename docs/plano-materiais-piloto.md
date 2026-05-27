# Plano de Materiais — Piloto (3 salas)

> Escopo: validar o ciclo completo ESP32 → API → Display em 3 salas reais.
>
> ✅ **Recursos já disponíveis (não comprar):**
> - Servidor físico, rede Wi-Fi, tablets, TV de recepção e toda a infraestrutura

---

## O que comprar

| # | Item | Especificação | Qtd | Preço unit. est. | Total est. |
|---|------|---------------|-----|-----------------|------------|
| 1 | Microcontrolador | ESP32 DevKit V1 (38 pinos) | 3 | R$ 45 | R$ 135 |
| 2 | Sensor de presença | PIR HC-SR501 | 3 | R$ 12 | R$ 36 |
| 3 | Fonte USB 5V 2A | Para alimentar o ESP32 | 3 | R$ 25 | R$ 75 |
| 4 | Cabo USB (micro ou tipo-C) | Compatível com o DevKit escolhido | 3 | R$ 12 | R$ 36 |
| 5 | Jumper wires macho-macho | Ligação ESP32 ↔ PIR | 1 kit | R$ 15 | R$ 15 |
| 6 | Protoboard 400 pontos | Prototipagem na bancada antes de fixar | 3 | R$ 18 | R$ 54 |
| 7 | Filamento PLA/PETG | Para impressão das caixas na impressora 3D própria | 1 rolo | R$ 80 | R$ 80 |
| 8 | Fita dupla-face extra-forte | Fixação das caixas impressas na parede/porta | 1 rolo | R$ 15 | R$ 15 |
| 9 | Abraçadeiras de nylon | Organização dos cabos | 1 pacote | R$ 10 | R$ 10 |
| | | | | **TOTAL** | **R$ 456** |

---

## Fluxo de Montagem

```
1. Imprimir caixas do ESP32 + PIR na impressora 3D
2. Flashear firmware no ESP32 e testar POST /sensor/{room_id} na bancada
3. Fixar caixa + ESP32 + PIR na sala 1 — validar detecção de presença
4. Repetir salas 2 e 3
5. Executar os 4 cenários de estado para validação final
```

---

## Onde Comprar

| Canal | Indicado para |
|-------|--------------|
| [Eletrogate](https://www.eletrogate.com) | ESP32, PIR, protoboard, jumpers |
| [FilipeFlop](https://www.filipeflop.com) | ESP32, PIR com documentação técnica |
| [Mercado Livre](https://www.mercadolivre.com.br) | Fontes USB, cabos, abraçadeiras |
| [Kabum](https://www.kabum.com.br) | Filamento PLA/PETG |
