import os
import pandas as pd

class HealthDataProcessor:
    def __init__(self, directory: str):
        self.directory = directory
        self.files = self._list_files()

    def _list_files(self):
        return os.listdir(self.directory)

    def load_odf_data(self, filename: str) -> pd.DataFrame:
        file_path = os.path.join(self.directory, filename)
        df = pd.read_excel(file_path, engine="odf")
        return self._clean_initial_rows(df)

    def _clean_initial_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.iloc[5:].reset_index(drop=True)
        df.columns = df.iloc[0]
        return df.iloc[1:]

    def save_to_csv(self, df: pd.DataFrame, output_filename: str):
        df.to_csv(output_filename, sep=';', index=False, header=False, encoding='utf-8', decimal='.')

    def process_csv_data(self, filename: str) -> pd.DataFrame:
        file_path = os.path.join(self.directory, filename)
        df = pd.read_csv(file_path, sep=';', encoding='utf-8')

        df['Registro_ANS'] = df['Registro_ANS'].astype(str)
        df['Telefone'] = df['Telefone'].astype('Int64').astype(str)
        df['Regiao_de_Comercializacao'] = df['Regiao_de_Comercializacao'].fillna(0).astype(int)
        df['Fax'] = df['Fax'].astype(str).str.replace('.', '', regex=False)
        df['Fax'] = pd.to_numeric(df['Fax'], errors='coerce').fillna(0).astype(str)

        return df

if __name__ == "__main__":
    diretorio_dados = '../documentos/operadoras_de_plano_de_saude_ativas'
    processor = HealthDataProcessor(diretorio_dados)

    # Processar arquivo CSV
    csv_df = processor.process_csv_data(processor.files[1])
    processor.save_to_csv(csv_df, '../documentos/dados_operadoras.csv')
