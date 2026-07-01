import polars as pl 
import os 
from datetime import datetime 
import numpy as np
import matplotlib.pyplot as plt
os.system('cls')

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo parquet...')
    inicio = datetime.now()

    # Leitura Preguiçosa 
    df_plano_execucao = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') #
    
    df_bolsa_familia = df_plano_execucao.collect()
    print(df_bolsa_familia.head(10))


    # ORDENANDO E MOSTRANDO 20 PRIMEIROS 
    # print(df_bolsa_familia.sort('VALOR PARCELA', descending=True).head(20))


except Exception as e:
    print(f'Erro ao ler arquivo parquet {e}')

try:
    #array
    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])

except Exception as e:
    print(f'Erro ao obter o array {e}')

try:
    #array
    plt.boxplot(array_valor_parcela, vert=False)
    plt.title('Distribuição bolsa familía')
    
    final = datetime.now()
    print(f'\nTotal de tempo gasto {final-inicio}')
    plt.show()

except Exception as e:
    print(f'Erro ao plotar o gráfico {e}')