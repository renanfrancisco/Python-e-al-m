import csv
import json
import matplotlib.pyplot as plt
from datetime import datetime

def exportar_para_csv(json_path="leituras.json", csv_path="relatorio.csv"):
    try:
        with open(json_path, "r") as f_json:
            linhas = [json.loads(linha) for linha in f_json if linha.strip()]

        with open(csv_path, "w", newline="") as f_csv:
            writer = csv.DictWriter(f_csv, fieldnames=["area", "umidade", "temperatura", "chuva_prevista", "data_hora"])
            writer.writeheader()
            for linha in linhas:
                writer.writerow(linha)

        print(f"📁 Relatório exportado para: {csv_path}")
    except Exception as e:
        print("Erro ao exportar relatório:", e)

def gerar_dashboard(json_path="leituras.json"):
    try:
        with open(json_path, "r") as f_json:
            dados = [json.loads(linha) for linha in f_json if linha.strip()]

        if not dados:
            print("⚠️ Nenhum dado encontrado para visualização.")
            return

        timestamps = [datetime.strptime(d["data_hora"], "%Y-%m-%d %H:%M:%S") for d in dados]
        umidades = [d["umidade"] for d in dados]
        temperaturas = [d["temperatura"] for d in dados]

        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, umidades, marker='o', label="Umidade (%)")
        plt.plot(timestamps, temperaturas, marker='s', label="Temperatura (°C)")
        plt.xlabel("Data e Hora")
        plt.ylabel("Valor")
        plt.title("Evolução da Umidade e Temperatura")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.xticks(rotation=45)
        plt.savefig("dashboard.png")
        print("📈 Gráfico salvo como 'dashboard.png'.")

    except Exception as e:
        print("Erro ao gerar dashboard:", e)
