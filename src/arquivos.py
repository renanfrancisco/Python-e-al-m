import json

def salvar_json(dados):
    with open("leituras.json", "a") as f:
        json.dump(dados, f)
        f.write("\n")

def salvar_txt(dados, resultado):
    with open("relatorio.txt", "a") as f:
        f.write(f"{dados['data_hora']} - {dados['area']}: {resultado}\n")
