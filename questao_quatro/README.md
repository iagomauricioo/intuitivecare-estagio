# API para realizar busca textual no arquivo de Operadoras

Essa API está rodando na porta `8000` que é padrão do FastAPI.
O front-end está rodando na porta 3000 do VueJS.

Ambos estão em produção rodando nos seguintes links: <br><br>
<a href="https://iagomauricio.com">https://iagomauricio.com</a> -> Front <br><br>
<a href="https://api.iagomauricio.com">https://api.iagomauricio.com</a> -> API

Existem 2 endpoints nessa API.

Ambos precisam do prefixo `/api/v1`

`GET /operadoras` (/api/v1/operadoras) <br>
`GET /operadoras/buscar?` + parâmetros http (/api/v1/operadoras/buscar)

Recomendo que para facilitar sua vida e facilitar a visualização de dados você entre no Swagger para entender melhor, lá terá tudo que você precisa, desde as rotas até os parâmetros necessários para enviar requisições.

o swagger se encontra em:

<a href="https://api.iagomauricio.com/docs">
https://api.iagomauricio.com/docs
</a>
<br>
ou se estiver rodando local:

<a href="http://localhost:8080/docs">
http://localhost:8000/docs
</a>