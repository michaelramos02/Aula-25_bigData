import pandas as pd 
import polars as pl 
import os 
from datetime import datetime

os.system('cls')

ENDERECO_DADOS = r'./../dados/'

try: 
    print('Obtendo os dados...')
    inicio = datetime.now()
    
    # Lista para guardar os arquivos csv
    lista_csv = []

    df_bolsa_familia = None

    # LISTAR OS NOMES DOS ARQUIVOS DA PASTA DADOS
    pasta = os.listdir(ENDERECO_DADOS)
    
    # Verifica se são csv
    for arquivo in pasta:
        if arquivo.endswith('.csv'):
            lista_csv.append(arquivo)
        
    # Leitura arquivos
    
    for arquivo in lista_csv:
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

        print(df.head())
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else: 
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        del df

        print(f'\nArquivo {arquivo} processado com sucesso!')
        print(df_bolsa_familia.shape)
    
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').
        str.replace(',', '.')
        .cast(pl.Float64)
    )

    # Salvando em arquivlo Parquet
    print('\nIniciando a Gravação do Arquivo Parquet...')

    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    print('\nArquivo salvo com sucesso...')

    final = datetime.now()
    print(f'\nTotal de tempo gasto {final-inicio}')

except Exception as e:
    print(f'Erro ao obter os dados {e}')
