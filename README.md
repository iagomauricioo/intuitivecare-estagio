# Vaga de estágio em Desenvolvimento (remoto) na Intuitive Care

Candidato: Iago Mauricio dos Santos Silva

<a href="https://www.linkedin.com/in/iagomauricioo/">Linkedin</a> / / /
<a href="https://github.com/iagomauricioo">Github</a>

## Questão 1 e 2

Optei por fazer as questões 1 e 2 utilizando um serviço de computação em nuvem em um cluster do <a href="https://colab.research.google.com/drive/1Pq-1cBO6AIXMyY-JAn-PWqbUyN3mMrpF?usp=sharing"><img src="https://img.shields.io/badge/Google%20Colab-%23F9A825.svg?style=for-the-badge&logo=googlecolab&logoColor=white" width="120"></a>
, já que não seria necessário a utilização de banco de dados, então me senti mais confortável em fazer por lá.

<a href="https://colab.research.google.com/drive/1Pq-1cBO6AIXMyY-JAn-PWqbUyN3mMrpF?usp=sharing">Link para o notebook Python</a>

Esse notebook contém tanto a questão 1 como a 2, lá você vai encontrar a descrição para cada questão.

Não precisa se preocupar com instalações, apenas execute o código inteiro!

### Sobre o código:

##### Atenção
Antes de rodar o código, execute `pip install -r requirements.txt`. Recomendo fortemente que você crie um <a href="https://docs.python.org/3/library/venv.html">Virtual Enviroment</a> (.venv) com `python3 -m venv .venv` para que as bibliotecas python instaladas em sua máquina não conflitem com as que serão instaladas nesse projeto. Observe que existem 2 requirements.txt no projeto, um na raiz do projeto e outro em /questao_quatro, recomendo que você crie .venv's diferentes, um para cada requirement.

Na raiz do projeto, encontra-se a terceira questão, ou seja, arquivos percentes a `/src` e `/documentos` são da 3º questão. O arquivo `main.py` é responsável por ler os arquivos .csv e unificar todos eles no arquivo `demonstracoes_contabeis.csv` (que só é gerado após o código rodar), após isso ele irá lhe perguntar se você quer importar os dados gerados para o Postgres, você digita "sim" ou "não".

A classe `PostgresManager` é responsável por checar se o banco de dados está rodando, iniciar o banco caso esteja offline e executar a transferência dos dados para o POSTGRES que estará rodando num container Docker. É importante que você tenha o Docker instalado em sua máquina, abaixo deixarei um link de instrução de download segundo a documentação da ferramenta. <a href="https://docs.docker.com/engine/install/">Clique aqui para baixar!</a>

A resolução do tópico 3.5 é o arquivo `relatorios_operadoras.sql` que pode ser localizado na raiz do projeto. Ele responde aquelas perguntas `Quais as 10 operadoras que fizeram tal coisa... no último trimestre`.

### Questão 4

Foi solicitado a criação de um front-end em ![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D) que consome uma API em Python. 

Optei por fazer a API utilizando FastAPI já que era algo simples como ler um CSV e transformar em um JSON.

Portanto, na pasta `/questao_quatro` você encontrará a pasta `/front-end` que conterá o VueJS e todo o restante pertence ao back-end da aplicação em Python. Nessa parte você precisará criar um novo .venv e instalar os `requirements.txt`.

### API hospedada num servidor

A API dessa aplicação já está rodando em um Servidor Virtual Privado (VPS). Portanto, se você quiser, não precisa rodar a API, mas sim só consumir pelo Swagger/Postman.

<a href="http://165.22.1.202:8000/docs" target="_blank">Link para coleção do Swagger (http://165.22.1.202:8000/docs)</a>

Se você quiser importar essa coleção para o seu POSTMAN, crie um novo workspace e importe a coleção de `http://165.22.1.202:8000/openapi.json`, ele lhe trará 2 endpoints.

Caso você decida consumir o back-end de forma local é EXTREMAMENTE importante que você altere a URL com o IPv4 do servidor para `localhost` no arquivo `/questao_quatro/front-end/src/components/HealthData.vue` na `linha 73`.

É isso! Espero que tenha gostado e conseguido executar todas as etapas com sucesso, deu um trabalhão! Foi um aprendizado muito massa. Enfim, fico disponível para mais informações.

Contato:

Whatsapp -> (82) 99102-1732 <br>
E-mail -> iagomauricio7@gmail.com