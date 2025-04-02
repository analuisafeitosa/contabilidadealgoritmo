import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('movimentacao_bancaria.db')
cursor = conn.cursor()

# Criar a tabela no banco de dados (ajuste os tipos de dados conforme necessário)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movimentacao3 (
        Data TEXT,
        Nome_Natureza TEXT,
        Entrada REAL,
        Saida REAL
    )
''')

# Carregar o CSV no DataFrame
df = pd.read_csv('movimentacao3.csv')

# Inserir os dados do DataFrame na tabela
df.to_sql('movimentacao3', conn, if_exists='replace', index=False)

# Confirmar e fechar a conexão
conn.commit()
conn.close()
