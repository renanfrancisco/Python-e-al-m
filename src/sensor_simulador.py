import random
from datetime import datetime

def simular_dados():
    area = "Área Simulada"
    umidade = random.randint(10, 90)
    temperatura = random.uniform(15, 35)
    chuva_prevista = random.choice([True, False])
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "area": area,
        "umidade": umidade,
        "temperatura": temperatura,
        "chuva_prevista": chuva_prevista,
        "data_hora": data_hora
    }
