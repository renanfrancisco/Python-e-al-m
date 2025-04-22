import oracledb
import json
conexao = None

def conectar():
    global conexao
    try:
        with open("config/db_config.json", "r") as f:
            config = json.load(f)
        dsn = f"{config['host']}:{config['port']}/{config['service_name']}"
        conexao = oracledb.connect(user=config['user'], password=config['password'], dsn=dsn)
        print("\n✅ Conectado ao Oracle com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro ao conectar ao Oracle: {e}")

def inserir_leitura(dados, resultado):
    global conexao
    if not conexao:
        conectar()
    if not conexao:
        print("⚠️ Conexão com Oracle não foi estabelecida.")
        return
    try:
        cursor = conexao.cursor()
        cursor.execute("""BEGIN
            EXECUTE IMMEDIATE '
                CREATE TABLE leituras_irrigacao (
                    id_leitura NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    area VARCHAR2(100),
                    umidade NUMBER,
                    temperatura NUMBER,
                    chuva_prevista NUMBER(1),
                    acao VARCHAR2(50),
                    data_leitura TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )';
        EXCEPTION
            WHEN OTHERS THEN
                IF SQLCODE != -955 THEN
                    RAISE;
                END IF;
        END;""")
        conexao.commit()
        cursor.execute("""
            INSERT INTO leituras_irrigacao (area, umidade, temperatura, chuva_prevista, acao)
            VALUES (:1, :2, :3, :4, :5)
        """, (
            dados['area'],
            dados['umidade'],
            dados['temperatura'],
            1 if dados['chuva_prevista'] else 0,
            resultado
        ))
        conexao.commit()
        cursor.close()
        print("🗃️ Dados salvos no Oracle com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao salvar no Oracle: {e}")
