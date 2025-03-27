# Vaga de estágio em Desenvolvimento (remoto) na Intuitive Care

Candidato: Iago Mauricio dos Santos Silva

<a href="https://www.linkedin.com/in/iagomauricioo/">Linkedin</a>
<a href="https://github.com/iagomauricioo">Github</a>

## Sobre o código:

#### Atenção
Antes de rodar o código, execute `pip install -r requirements.txt`. Recomendo fortemente que você crie um <a href="https://docs.python.org/3/library/venv.html">Virtual Enviroment</a> (.venv) com `python3 -m venv .venv` para que as bibliotecas python instaladas em sua máquina não conflitem com as que serão instaladas nesse projeto.

O arquivo `main.py` é responsável por ler os arquivos .csv e unificar todos eles no arquivo `dados.csv` (que só é gerado após o código rodar), após isso ele irá lhe pergunta se você quer importar os dados gerados para o Postgres, se você digitar "sim" ele irá rodar o arquivo `operacoes_no_db.py`.

O arquivo `operacoes_no_db.py` é responsável por checar se o banco de dados está rodando, iniciar o banco caso esteja offline e executar a transferência dos dados para o POSTGRES que estará rodando num container Docker. É importante que você tenha o Docker instalado em sua máquina, abaixo deixarei um link de instrução de download segundo a documentação da ferramenta. <a href="https://docs.docker.com/engine/install/">Clique aqui para baixar!</a>

Optei por utilizar o comando COPY no arquivo `import.sql` buscando maior performance visto que eram mais de 6.000.000 (seis milhões) de linhas, então iriam demorar horas (dependendo do poder de processamento) para inserir todos os dados no banco.wq