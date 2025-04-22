import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

from sensor_simulador import simular_dados
from irrigacao import avaliar_irrigacao
from arquivos import salvar_json, salvar_txt
from banco import inserir_leitura

def menu_principal():
    print("🌱 Bem-vindo ao Sistema de Monitoramento de Irrigação Inteligente 🌦️")
    while True:
        print("\nMenu Principal:")
        print("1. Inserir dados manualmente")
        print("2. Simular sensores")
        print("3. Exportar relatório para CSV")
        print("4. Visualizar dashboard")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dados = coletar_dados_manualmente()
        elif opcao == "2":
            dados = simular_dados()
            print("\n📊 Dados Simulados:")
            exibir_dados(dados)
        elif opcao == "3":
            from relatorio import exportar_para_csv
            exportar_para_csv()
            continue
        elif opcao == "4":
            from relatorio import gerar_dashboard
            gerar_dashboard()
            continue
        elif opcao == "5":
            print("Encerrando... Até logo!")
            break
        else:
            print("❌ Opção inválida.")
            continue

        resultado = avaliar_irrigacao(dados)
        print(f"💧 Ação recomendada: {resultado}")
        salvar_json(dados)
        salvar_txt(dados, resultado)
        inserir_leitura(dados, resultado)

def coletar_dados_manualmente():
    from datetime import datetime
    area = input("Nome da área: ").strip()

    while True:
        try:
            umidade = int(input("Umidade do solo (%): "))
            if not 0 <= umidade <= 100:
                raise ValueError
            break
        except ValueError:
            print("❌ Digite um número inteiro entre 0 e 100.")

    while True:
        try:
            temperatura = float(input("Temperatura (°C): "))
            break
        except ValueError:
            print("❌ Digite um valor numérico válido para a temperatura.")

    while True:
        chuva_input = input("Há previsão de chuva? (s/n): ").strip().lower()
        if chuva_input in ['s', 'n']:
            chuva = chuva_input == 's'
            break
        else:
            print("❌ Digite apenas 's' ou 'n'.")

    dados = {
        "area": area,
        "umidade": umidade,
        "temperatura": temperatura,
        "chuva_prevista": chuva,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("\n📋 Dados inseridos:")
    exibir_dados(dados)
    return dados

def exibir_dados(dados):
    print(f"Área: {dados['area']}")
    print(f"Umidade: {dados['umidade']}%")
    print(f"Temperatura: {dados['temperatura']}°C")
    print(f"Previsão de chuva: {'Sim' if dados['chuva_prevista'] else 'Não'}")
    print(f"Data e Hora: {dados['data_hora']}")

if __name__ == "__main__":
    menu_principal()