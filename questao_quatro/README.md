# 🚀 API de Busca Textual em Operadoras

## 🌐 Endpoints Disponíveis

### Base URL
- Produção: `https://api.iagomauricio.com`
- Local: `http://localhost:8000`

### Prefixo da API
Todos os endpoints requerem o prefixo `/api/v1`

### Endpoints
1. **Listar Operadoras**
   - Método: `GET`
   - Rota: `/operadoras`
   - URL Completa: `/api/v1/operadoras`

2. **Buscar Operadoras**
   - Método: `GET`
   - Rota: `/operadoras/buscar`
   - URL Completa: `/api/v1/operadoras/buscar`
   - Parâmetros: Query parameters HTTP

## 📚 Documentação

### Swagger UI
Para uma melhor experiência de desenvolvimento e visualização da API, utilize o Swagger UI:

- **Produção:** [https://api.iagomauricio.com/docs](https://api.iagomauricio.com/docs)
- **Local:** [http://localhost:8000/docs](http://localhost:8000/docs)

## 🖥️ Frontend

O frontend da aplicação está disponível em:
- **URL:** [https://iagomauricio.com](https://iagomauricio.com)
- **Porta:** 3000

## 🔧 Configuração Local

### Portas
- API: 8000 (FastAPI)
- Frontend: 3000 (Vue.js)

### Requisitos
- Python 3.x
- Node.js (para o frontend)
- Dependências listadas em `requirements.txt`

## 📝 Observações
- Utilize o Swagger UI para facilitar o entendimento das rotas e parâmetros
- A documentação completa da API está disponível no Swagger
- Para desenvolvimento local, ajuste as URLs conforme necessário