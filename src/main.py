import os
import pandas as pd
from data.csv_processor import CsvProcessor
from postgres.postgres_manager import PostgresManager
from data.health_data_processor import HealthDataProcessor

def import_csv(csv_folder='../documentos/demonstracoes_contabeis'):
    csv_processor = CsvProcessor()
    files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]
    files.sort()

    if not files:
        print("Arquivo CSV não encontrado.")
        return None

    dfs = []
    for file in files:
        file_path = os.path.join(csv_folder, file)
        try:
            df = csv_processor.process_csv(caminho_arquivo=file_path)
            dfs.append(df)
            print(f"Arquivo lido com sucesso: {file}")
        except Exception as e:
            print(f"Erro ao ler {file}: {e}")

    if not dfs:
        print("Nenhum arquivo pode ser lido.")
        return None

    df_total = pd.concat(dfs, ignore_index=True)
    return df_total

def process_health_data(health_folder='../documentos/operadoras_de_plano_de_saude_ativas'):
    health_processor = HealthDataProcessor(health_folder)
    csv_df = health_processor.process_csv_data(health_processor.files[1])
    health_processor.save_to_csv(csv_df, '../documentos/dados_operadoras.csv')
    print("Dados de operadoras processados e salvos em '/documentos/dados_operadoras.csv'.")

def process_and_generate_csv(df_total):
    csv_processor = CsvProcessor()
    df_total = df_total.fillna("NULL")
    df_total['VL_SALDO_INICIAL'] = df_total['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
    df_total['VL_SALDO_FINAL'] = df_total['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)

    return csv_processor.generate_csv(df_total=df_total)

def import_data_to_postgres(postgres_manager, csv_file, table):
    postgres_manager.insert_data_to_postgres(csv_file=csv_file, table_name=table)

def execute_sql_file(postgres_manager, sql_file):
    postgres_manager.execute_sql_file(sql_file)

def view_table(postgres_manager):
    num_rows = int(input("Quantas linhas você deseja visualizar? "))
    rows = postgres_manager.view_table(num_rows)
    if rows:
        for row in rows:
            print(row)
    else:
        print("Nenhum dado encontrado.")

def main():
    postgres_manager = PostgresManager()

    if not postgres_manager.is_postgres_running():
        print("Tentando iniciar o PostgreSQL via Docker...")
        if not postgres_manager.start_postgres_with_docker():
            print("Falha ao iniciar o PostgreSQL.")
            return
        postgres_manager.connect()

    print("Processando dados de operadoras de plano de saúde...")
    process_health_data()

    print("Importando e processando arquivos CSV de demonstrações contábeis...")
    df_total = import_csv()
    if df_total is None:
        print("Nenhum arquivo CSV foi importado com sucesso.")
        return
    
    csv_file = process_and_generate_csv(df_total)
    print(f"CSV gerado com sucesso: {csv_file}")

    question = "Você deseja importar os dados para o banco de dados PostgreSQL? (Digite 'sim' para prosseguir ou 'não' para cancelar): "
    if input(question).lower() == 'sim':
        execute_sql_file(postgres_manager, '../create_tables.sql')
        import_data_to_postgres(postgres_manager, csv_file=csv_file, table='demonstracoes_contabeis')
        import_data_to_postgres(postgres_manager, csv_file='../documentos/dados_operadoras.csv', table='operadoras')
    
    question = "Você deseja visualizar a tabela 'demonstracoes_contabeis' no banco de dados PostgreSQL? (Digite 'sim' para visualizar ou 'não' para cancelar): "
    if input(question).lower() == 'sim':
        view_table(postgres_manager)
    else:
        print("Operação finalizada.")

if __name__ == "__main__":
    main()
