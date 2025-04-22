# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Sistema de Monitoramento de Irrigação Inteligente

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/joão-vitor-severo-oliveira-87904134b/">João Vitor Severo Oliveira -rm566251</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Jonas Luis da Silva - rm561465</a>
- <a href="https://www.linkedin.com/in/renan-francisco-de-paula-b3320915b/">Renan Francisco de Paula - rm561454</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>

## 📜 Descrição

O projeto tem como objetivo criar uma solução prática e funcional para otimizar o uso da água em plantações, evitando tanto o desperdício quanto a deficiência hídrica. Por meio de simulações de sensores de umidade do solo e dados climáticos, o sistema é capaz de avaliar a necessidade de irrigação em áreas de plantio. Ele permite o registro manual ou automatizado dos dados, armazena os registros em banco de dados Oracle e exporta relatórios em formatos `.csv` e gráficos em `.png` com análise cronológica. O projeto também foca em promover a sustentabilidade e o uso consciente dos recursos hídricos no agronegócio.

## 📁 Estrutura de pastas

- <b>config</b>: arquivo `db_config.json` com as credenciais de conexão ao banco Oracle.
- <b>document</b>: documentos complementares do projeto.
- <b>scripts</b>: scripts auxiliares, se houver.
- <b>src</b>: código-fonte principal do projeto (menu, banco, sensores, relatórios).
- <b>README.md</b>: documentação principal do projeto.

## 🔧 Como executar o código

### Pré-requisitos:
- Python 3.8+
- Oracle Database
- Pacotes Python:
```bash
pip install -r requirements.txt
```

### Passo a passo:

#### 1. Clone o repositório:
```bash[
git clone https://github.com/seuusuario/Python-e-al-m.git
cd Python-e-al-m
```

#### 2. Configure a conexão com o banco Oracle:
Edite o arquivo `config/db_config.json` com suas credenciais:
```json
{
  "user": "seu_usuario",
  "password": "sua_senha",
  "host": "localhost",
  "port": "1521",
  "service_name": "XEPDB1"
}
```

#### 3. Execute o sistema:
```bash
python menu.py
```

### Funcionalidades:
- Inserção manual ou simulação de dados
- Armazenamento em JSON, TXT e Oracle DB
- Geração de CSV (`relatorio.csv`)
- Geração de gráfico cronológico (`dashboard.png`)

## 🗃 Histórico de lançamentos

* 1.0.0 - 21/04/2025
    * Projeto finalizado com coleta, simulação, exportação e dashboard funcional

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
