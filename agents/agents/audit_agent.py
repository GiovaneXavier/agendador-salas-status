from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

from tools.room_status_tools import get_unscheduled_usage, get_room_history, get_all_rooms_status
from tools.booking_tools import get_bookings, get_all_rooms

SYSTEM_PROMPT = """Você é um agente de auditoria de salas da Samsung.
Seu objetivo é identificar padrões de uso não agendado e gerar relatórios claros para gestão.

Diretrizes:
- Sempre consulte get_unscheduled_usage para ter a visão geral
- Para cada sala com ocorrências, use get_room_history para detalhar os horários
- Compare com get_bookings para confirmar se realmente não havia reserva
- Apresente o relatório em português, com horários e frequência por sala
- Indique se o padrão é recorrente (mesmo horário em dias diferentes)
- Sugira ações: avisar o responsável da área, criar reserva padrão, etc.
"""


def create_audit_agent(model: str = "claude-sonnet-4-6"):
    llm = ChatAnthropic(model=model, temperature=0)
    tools = [get_unscheduled_usage, get_room_history, get_all_rooms_status, get_bookings, get_all_rooms]
    return create_react_agent(llm, tools, state_modifier=SYSTEM_PROMPT)


def run_audit(hours: int = 24) -> str:
    agent = create_audit_agent()
    result = agent.invoke({
        "messages": [{"role": "user", "content": f"Gere um relatório de auditoria das últimas {hours} horas. Identifique salas com uso não agendado e detalhe os horários e frequência."}]
    })
    return result["messages"][-1].content
