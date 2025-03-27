# Vaga de estágio em Desenvolvimento (remoto) na Intuitive Care

Candidato: Iago Mauricio dos Santos Silva

<a href="https://www.linkedin.com/in/iagomauricioo/">Linkedin</a>
<a href="https://github.com/iagomauricioo">Github</a>

## Sobre o código:

O arquivo `questao3_intuitivecare.py` é responsável por ler os arquivos .csv e unificar todos eles no arquivo `dados.csv` (que só é gerado após o código rodar).

O arquivo `inserir_dados_no_banco.py` é responsável por executar a transferência dos dados para o POSTGRES que estará rodando num container Docker. É importante que você tenha o Docker instalado em sua máquina, abaixo deixarei um link de instrução de download segundo a documentação da ferramenta. <a href="https://docs.docker.com/engine/install/">Clique aqui para baixar!</a>

Optei por utilizar o comando COPY no arquivo `import.sql` buscando maior performance visto que eram mais de 6.000.000 (seis milhões) de linhas, então iriam demorar horas (dependendo do poder de processamento) para inserir todos os dados no banco.