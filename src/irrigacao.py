def avaliar_irrigacao(dados):
    if dados['umidade'] < 30 and not dados['chuva_prevista']:
        return "IRRIGAR"
    elif dados['umidade'] >= 70 or dados['chuva_prevista']:
        return "NÃO IRRIGAR"
    return "AGUARDAR MONITORAMENTO"
