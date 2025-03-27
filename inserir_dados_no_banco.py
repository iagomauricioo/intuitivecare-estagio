import subprocess
import time

host = "localhost"
user = "intuitivecare"
password = "intuitivecare@2025"
database = "app"
sql_file = "import.sql"

def verificar_postgres_rodando():
    try:
        comando = f"pg_isready -h {host} -U {user}"
        subprocess.run(comando, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
def iniciar_postgres_com_docker():
    try:
        subprocess.run("docker-compose up -d", shell=True, check=True)
        print("Aguardando o PostgreSQL iniciar...")
        time.sleep(10)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao iniciar o PostgreSQL: {e}")
        return False
    return True

def inserir_dados_no_postgres():
    if not verificar_postgres_rodando():
        print("PostgreSQL não está rodando. Iniciando com Docker...")
        if not iniciar_postgres_com_docker():
            print("❌ Não foi possível iniciar o PostgreSQL.")
            return
        print("PostgreSQL iniciado com sucesso.")
    
    try:
        comando = f"PGPASSWORD='{password}' psql -h {host} -U {user} -d {database} -f {sql_file}"
        subprocess.run(comando, shell=True, check=True)
        print("🚀 Arquivo SQL executado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar o SQL: {e}")