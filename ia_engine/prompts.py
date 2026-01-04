def gerar_prompt(servico):
    base = "luxury beauty salon, professional photography, soft light"

    if "mecha" in servico:
        return base + ", highlighted hair, golden tones"
    if "cor" in servico:
        return base + ", hair coloring, glossy hair"
    if "tratamento" in servico:
        return base + ", hair treatment session"

    return base + ", elegant woman"
