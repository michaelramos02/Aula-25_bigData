import pandas as pd # install fastparquet para rodar com pandas
import polars as pl 
import os 
from datetime import datetime 

os.system('cls')

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo parquet...')
    inicio = datetime.now()

    # Leitura direta
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    
    # print(df_bolsa_familia.head())
     
    df_filtrado = df_bolsa_familia.filter(pl.col('VALOR PARCELA') > 2500)
    
    print(df_filtrado.shape)

    # ORDENANDO E MOSTRANDO 20 PRIMEIROS 
    # print(df_bolsa_familia.sort('VALOR PARCELA', descending=True).head(20))

    final = datetime.now()
    print(f'\nTotal de tempo gasto {final-inicio}')



except Exception as e:
    print(f'Erro ao ler arquivo parquet {e}')