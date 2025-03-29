import pandas as pd
import os
import numpy as np

def carregar_dados_operadoras() -> list:
    caminho_csv = os.path.join('documentos', 'dados_operadoras.csv')
    
    df = pd.read_csv(caminho_csv, encoding='utf-8', delimiter=';')
    df = df.replace([np.inf, -np.inf], np.nan)
    dados = df.to_dict(orient='records')

    def clean_data(item):
        if isinstance(item, dict):
            return {k: clean_data(v) for k, v in item.items()}
        elif isinstance(item, (list, tuple)):
            return [clean_data(v) for v in item]
        elif pd.isna(item):
            return None
        elif isinstance(item, (np.generic)):
            return item.item()
        else:
            return item
    
    return [clean_data(record) for record in dados]