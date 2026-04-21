"""
Ponto de entrada dos agentes IA do Room Status System.

Uso:
    python main.py audit          → relatório de uso não agendado (24h)
    python main.py audit --hours 48
    python main.py anomaly        → verifica sensores com comportamento anômalo
    python main.py anomaly --minutes 30
    python main.py ask "Qual sala está livre agora?"
"""

import argparse
import sys
from dotenv import load_dotenv

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Agentes IA — Room Status System")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # audit
    audit_parser = subparsers.add_parser("audit", help="Relatório de uso não agendado")
    audit_parser.add_argument("--hours", type=int, default=24, help="Janela de análise em horas (padrão: 24)")

    # anomaly
    anomaly_parser = subparsers.add_parser("anomaly", help="Detecção de anomalias em sensores")
    anomaly_parser.add_argument("--minutes", type=int, default=60, help="Minutos sem variação para considerar travado (padrão: 60)")

    # ask
    ask_parser = subparsers.add_parser("ask", help="Pergunta em linguagem natural")
    ask_parser.add_argument("question", type=str, help="Pergunta a ser respondida")

    args = parser.parse_args()

    if args.command == "audit":
        from agents.audit_agent import run_audit
        print(f"\n── Relatório de Auditoria ({args.hours}h) ──\n")
        print(run_audit(hours=args.hours))

    elif args.command == "anomaly":
        from agents.anomaly_agent import run_anomaly_check
        print(f"\n── Verificação de Anomalias (>{args.minutes}min travado) ──\n")
        print(run_anomaly_check(stuck_minutes=args.minutes))

    elif args.command == "ask":
        from agents.assistant_agent import ask
        print(f"\n── Assistente ──\n")
        print(ask(args.question))


if __name__ == "__main__":
    main()
