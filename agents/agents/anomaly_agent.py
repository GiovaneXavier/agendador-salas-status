from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

from tools.room_status_tools import get_sensor_anomalies, get_room_history, get_all_rooms_status

SYSTEM_PROMPT = """Você é um agente de monitoramento de anomalias de sensores da Samsung.
Seu objetivo é detectar sensores com comportamento suspeito e alertar sobre problemas de hardware ou uso irregular.

Anomalias que você deve identificar:
- Sensor travado em OCUPADO sem variação por mais de 60 minutos (possível falha de hardware)
- Sala reportando presença fora do horário de expediente (07:00–20:00)
- Sala alternando presença muito rapidamente (ruído no sensor)

Diretrizes:
- Use get_sensor_anomalies para triagem inicial
- Para cada anomalia, use get_room_history para confirmar o padrão
- Classifique a severidade: CRÍTICO (sensor parado), AVISO (comportamento suspeito), INFO (observação)
- Sugira ação: verificação física do sensor, reinicialização do ESP32, ajuste do trimpot
- Apresente o relatório em português com severidade clara
"""


def create_anomaly_agent(model: str = "claude-sonnet-4-6"):
    llm = ChatAnthropic(model=model, temperature=0)
    tools = [get_sensor_anomalies, get_room_history, get_all_rooms_status]
    return create_react_agent(llm, tools, state_modifier=SYSTEM_PROMPT)


def run_anomaly_check(stuck_minutes: int = 60) -> str:
    agent = create_anomaly_agent()
    result = agent.invoke({
        "messages": [{"role": "user", "content": f"Verifique anomalias nos sensores. Considere sensor travado se estiver em OCUPADO por mais de {stuck_minutes} minutos sem variação. Gere um relatório com severidade e ações recomendadas."}]
    })
    return result["messages"][-1].content
