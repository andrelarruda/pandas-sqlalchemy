import pandas as pd
from sqlalchemy import create_engine #lib para estabelecer conexão com o servidor MySQL

#                      dialect        usuario:senha@localhost/nomeDb
engine = create_engine("mysql+pymysql://root:@localhost/exemplo") #Nesta linha é criada uma conexão com o banco de dados

#print(engine.table_names())

with engine.connect() as conn, conn.begin():

    # Faz a leitura do CSV
    dataframe = pd.read_csv("C:/Users/Andre Arruda/Documents/UFRPE/7º período - 2019.2/Projeto de Banco de Dados/teste1.csv",
                            usecols=['nome', 'sobrenome'], #definir quais as colunas serão pegas
                            sep='\t',
                            dtype={'nome': str, 'sobrenome': str}) #tipo de cada coluna
    
    dataframe.to_sql('pessoa', conn, if_exists='append', index=False)
# Opções if_exists: 'append': adiciona à tabela existente, 'replace': substitui as linhas que ja estiverem na tabela, 'fail'
