def detectar_intencao(texto):
    t = texto.lower()

    if any(p in t for p in ["agendar","marcar","horário","agenda"]):
        return "agendamento"

    if any(p in t for p in ["promo","oferta","desconto"]):
        return "promocao"

    if any(p in t for p in ["antes","depois","resultado"]):
        return "antes_depois"

    if any(p in t for p in ["especialista","profissional","experiência"]):
        return "autoridade"

    if any(p in t for p in ["imagem","foto","arte"]):
        return "imagem"

    return "emocional"
