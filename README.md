# Vaga de estágio em Desenvolvimento (remoto) na Intuitive Care

Candidato: Iago Mauricio dos Santos Silva

<a href="https://www.linkedin.com/in/iagomauricioo/">Linkedin</a>
<a href="https://github.com/iagomauricioo">Github</a>

## Questão 1 e 2

Optei por fazer as questões 1 e 2 utilizando um serviço de computação em nuvem em um cluster do <a href="https://colab.research.google.com/drive/1Pq-1cBO6AIXMyY-JAn-PWqbUyN3mMrpF?usp=sharing"><img src="https://img.shields.io/badge/Google%20Colab-%23F9A825.svg?style=for-the-badge&logo=googlecolab&logoColor=white" width="120"></a>
, já que não seria necessário a utilização de banco de dados, então me senti mais confortável em fazer por lá.

<a href="https://colab.research.google.com/drive/1Pq-1cBO6AIXMyY-JAn-PWqbUyN3mMrpF?usp=sharing">Link para o notebook Python</a>

Esse notebook contém tanto a questão 1 como a 2, lá você vai encontrar a descrição para cada questão.

### Sobre o código:

##### Atenção
Antes de rodar o código, execute `pip install -r requirements.txt`. Recomendo fortemente que você crie um <a href="https://docs.python.org/3/library/venv.html">Virtual Enviroment</a> (.venv) com `python3 -m venv .venv` para que as bibliotecas python instaladas em sua máquina não conflitem com as que serão instaladas nesse projeto.

O arquivo `main.py` é responsável por ler os arquivos .csv e unificar todos eles no arquivo `demonstracoes_contabeis.csv` (que só é gerado após o código rodar), após isso ele irá lhe pergunta se você quer importar os dados gerados para o Postgres, se você digitar "sim" ele irá rodar o arquivo `operacoes_no_db.py`.

O arquivo `operacoes_no_db.py` é responsável por checar se o banco de dados está rodando, iniciar o banco caso esteja offline e executar a transferência dos dados para o POSTGRES que estará rodando num container Docker. É importante que você tenha o Docker instalado em sua máquina, abaixo deixarei um link de instrução de download segundo a documentação da ferramenta. <a href="https://docs.docker.com/engine/install/">Clique aqui para baixar!</a>

Optei por utilizar o comando COPY no arquivo `import.sql` buscando maior performance visto que eram mais de 6.000.000 (seis milhões) de linhas, então iriam demorar horas (dependendo do poder de processamento) para inserir todos os dados no banco.wq