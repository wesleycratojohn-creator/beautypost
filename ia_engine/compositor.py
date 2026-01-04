import random

def compor_texto(base, ideia):
    abertura = random.choice([
        "✨ Transforme sua beleza.",
        "💖 Seu momento de cuidado começa agora.",
        "🌸 Realce o que você tem de melhor."
    ])

    fechamento = random.choice([
        "Agende seu horário.",
        "Viva essa experiência.",
        "Cuidar de você é nossa prioridade."
    ])

    return f"{abertura}\n\n{base}\n\n{ideia.capitalize()}\n\n{fechamento}"
