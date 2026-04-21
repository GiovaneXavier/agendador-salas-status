from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

from tools.room_status_tools import get_all_rooms_status, get_room_status, get_room_history
from tools.booking_tools import get_all_rooms, get_bookings

SYSTEM_PROMPT = """Você é um assistente de salas da Samsung. Responda de forma direta e útil em português.

Você pode responder perguntas como:
- "Qual sala está livre agora?"
- "A sala Carvalho está ocupada?"
- "Quais salas têm reunião amanhã de manhã?"
- "Quem está usando a sala Ipê agora sem reserva?"

Diretrizes:
- Seja conciso: responda em 1-3 frases quando possível
- Use get_all_rooms_status para perguntas gerais sobre disponibilidade atual
- Use get_room_status para perguntas sobre uma sala específica
- Use get_bookings com a data correta para perguntas sobre agenda futura
- Para "agora" use o status em tempo real (get_all_rooms_status / get_room_status)
- Nunca invente dados — use sempre as ferramentas
"""


def create_assistant_agent(model: str = "claude-sonnet-4-6"):
    llm = ChatAnthropic(model=model, temperature=0)
    tools = [get_all_rooms_status, get_room_status, get_room_history, get_all_rooms, get_bookings]
    return create_react_agent(llm, tools, state_modifier=SYSTEM_PROMPT)


def ask(question: str) -> str:
    agent = create_assistant_agent()
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    return result["messages"][-1].content
