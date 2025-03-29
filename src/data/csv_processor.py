import pandas as pd

class CsvProcessor:
    def __init__(self, sep=';', encoding='utf-8', decimal='.'):
        self.sep = sep
        self.encoding = encoding
        self.decimal = decimal

    def process_csv(self, caminho_arquivo):
        try:
            df = pd.read_csv(caminho_arquivo, sep=self.sep, encoding=self.encoding, on_bad_lines="skip")
            return df
        except Exception as e:
            raise Exception(f"Erro ao processar o arquivo CSV: {e}")

    def generate_csv(self, df_total, output_file='../documentos/demonstracoes_contabeis.csv'):
        df_total.to_csv(output_file, sep=self.sep, index=False, header=False, encoding=self.encoding, decimal=self.decimal)
        return output_file

