# Processo Seletivo - Estágio em Desenvolvimento (Remoto) - Intuitive Care

## 👤 Candidato
**Nome:** Iago Mauricio dos Santos Silva  
**LinkedIn:** [iagomauricioo](https://www.linkedin.com/in/iagomauricioo/)  
**GitHub:** [iagomauricioo](https://github.com/iagomauricioo)  
**Contato:**  
- WhatsApp: (82) 99102-1732  
- E-mail: iagomauricio7@gmail.com

## 📋 Sobre o Projeto
Este repositório contém as soluções desenvolvidas para o processo seletivo de estágio em desenvolvimento da Intuitive Care. O projeto está dividido em 4 questões principais, cada uma com sua própria estrutura e requisitos.

## 🚀 Questões 1 e 2 - Análise de Dados
As questões 1 e 2 foram desenvolvidas utilizando o Google Colab para processamento em nuvem.

### 🔗 Links
- [Notebook Python no Google Colab](https://colab.research.google.com/drive/1Pq-1cBO6AIXMyY-JAn-PWqbUyN3mMrpF?usp=sharing)
- [Badge Google Colab](https://img.shields.io/badge/Google%20Colab-%23F9A825.svg?style=for-the-badge&logo=googlecolab&logoColor=white)

### 📝 Observações
- Não é necessário instalação local
- Basta executar o código no ambiente do Colab
- Todas as dependências estão configuradas no ambiente

## 📊 Questão 3 - Processamento de Dados e PostgreSQL
A terceira questão está localizada na raiz do projeto, com os seguintes componentes:

### Estrutura de Arquivos
```
/
├── src/
├── documentos/
├── main.py
└── relatorios_operadoras.sql
```

### Requisitos
- Python 3.x
- Docker
- PostgreSQL

### Configuração
1. Criar ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate  # Windows
   ```

2. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Iniciar o container Docker com PostgreSQL

### Funcionalidades
- `main.py`: Processa arquivos CSV e gera `demonstracoes_contabeis.csv`
- `PostgresManager`: Gerencia conexão e importação de dados para PostgreSQL
- `relatorios_operadoras.sql`: Contém as consultas para análise dos dados

## 🌐 Questão 4 - Frontend Vue.js e API FastAPI
A quarta questão implementa uma aplicação web com frontend em Vue.js e backend em FastAPI.

### Estrutura
```
/questao_quatro
├── front-end/          # Aplicação Vue.js
└── back-end/          # API FastAPI
```

### Configuração
1. Criar ambiente virtual específico:
   ```bash
   python3 -m venv .venv-questao4
   source .venv-questao4/bin/activate
   ```

2. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```

### API em Produção
A API está disponível em produção:
- **Swagger UI:** [https://api.iagomauricio.com/docs](https://api.iagomauricio.com/docs)
- **OpenAPI Spec:** [https://api.iagomauricio.com/openapi.json](https://api.iagomauricio.com/openapi.json)

### Configuração do Frontend
Para desenvolvimento local:
1. Alterar a URL da API no arquivo `/questao_quatro/front-end/src/components/HealthData.vue` (linha 73)
2. Substituir o IPv4 do servidor por `localhost`

## 📚 Documentação Adicional
- [Documentação Docker](https://docs.docker.com/engine/install/)
- [Documentação Python venv](https://docs.python.org/3/library/venv.html)

## 🤝 Considerações Finais
Este projeto foi desenvolvido com o objetivo de demonstrar habilidades técnicas e capacidade de resolução de problemas. Fique à vontade para entrar em contato caso tenha dúvidas ou sugestões.