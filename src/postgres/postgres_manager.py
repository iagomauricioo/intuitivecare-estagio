import psycopg2
import time
import subprocess
import re
from .config import HOST, USER, PASSWORD, DATABASE, SQL_FILE

class PostgresManager:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.host = HOST
        self.user = USER
        self.password = PASSWORD
        self.database = DATABASE
        self.sql_file = SQL_FILE

    def is_postgres_running(self):
        try:
            self.connect()
            if self.conn:
                print("PostgreSQL está online.")
                return True
        except psycopg2.Error:
            print("PostgreSQL não está acessível.")
        finally:
            self.close_connection()
        return False

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Conectado ao PostgreSQL.")
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")

    def start_postgres_with_docker(self):
        try:
            subprocess.run("docker-compose up -d", shell=True, check=True)
            print("Aguardando PostgreSQL iniciar...")
            time.sleep(10)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao iniciar PostgreSQL: {e}")
            return False
        return True
    
    def is_valid_table_name(self, table_name, allowed_tables):
        if table_name not in allowed_tables:
            print(f"Tabela '{table_name}' não permitida.")
            return False
        if not re.match(r'^[\w]+$', table_name):
            print(f"Nome da tabela '{table_name}' inválido. Caracteres especiais não são permitidos.")
            return False
        
        return True

    def insert_data_to_postgres(self, table_name, csv_file, skip_header=True):
        if not self.is_valid_table_name(table_name=table_name, allowed_tables=['demonstracoes_contabeis', 'operadoras']):
            return
        self.connect()
        if not self.conn:
            print("Falha na conexão.")
            return
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                if skip_header:
                    next(file)
                copy_query = f"COPY {table_name} FROM STDIN WITH CSV HEADER DELIMITER ';' NULL 'NULL' ENCODING 'UTF8'"
                self.cursor.copy_expert(copy_query, file)
            self.conn.commit()
            print(f"\033[32mDados importados para a tabela {table_name} com sucesso! ✅\033[0m")
        except psycopg2.Error as e:
            print(f"\033[31mErro ao importar dados do CSV para {table_name}: {e} ❌\033[0m")
        finally:
            self.close_connection()

    def execute_sql_file(self, sql_file):
        self.connect()
        if not self.conn:
            print("Falha na conexão.")
            return
        try:
            with open(sql_file, 'r', encoding='utf-8') as file:
                sql_commands = file.read()
            self.cursor.execute(sql_commands)
            self.conn.commit()
            print("Tabelas criadas com sucesso!")
        except psycopg2.Error as e:
            print(f"Erro ao executar SQL: {e}")
        finally:
            self.close_connection()

    def view_table(self, num_rows: int):
        self.connect()
        if not self.conn:
            return
        try:
            self.cursor.execute("SELECT * FROM demonstracoes_contabeis LIMIT %s", (num_rows,))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except psycopg2.Error as e:
            print(f"Erro ao visualizar a tabela: {e}")
        finally:
            self.close_connection()