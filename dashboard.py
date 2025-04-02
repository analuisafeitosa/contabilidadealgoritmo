import sqlite3
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('movimentacao_bancaria.db')

# Carregar os dados da tabela movimentacao2 para um DataFrame
df = pd.read_sql('SELECT * FROM movimentacao3', conn)

# Fechar a conexão com o banco de dados
conn.close()

# Converter a coluna 'Data' para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'], format='%m/%d/%Y')

# Extrair o mês e o ano da coluna 'Data' e converter para string
df['Ano-Mês'] = df['Data'].dt.to_period('M').astype(str)

# Criar o gráfico de "Entrada" (Receita), agrupado por mês
fig_entrada = px.bar(df, x='Ano-Mês', y='Entrada', 
                     title='Receitas (Entrada) por Mês',
                     labels={'Entrada': 'Valor da Receita'},
                     template='plotly_dark',
                     color='Ano-Mês')

# Criar o gráfico de "Saida" (Despesa), agrupado por mês
fig_saida = px.bar(df, x='Ano-Mês', y='Saida', 
                   title='Despesas (Saída) por Mês',
                   labels={'Saida': 'Valor da Despesa'},
                   template='plotly_dark',
                   color='Ano-Mês')

# Criar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do Dash com dois gráficos
app.layout = html.Div([
    html.H1("Dashboard de Movimentação Bancária", style={'textAlign': 'center'}),
    
    # Gráfico de Receitas (Entrada)
    html.Div([
        dcc.Graph(
            id='grafico-entrada',
            figure=fig_entrada
        )
    ], style={'padding': '20px'}),
    
    # Gráfico de Despesas (Saída)
    html.Div([
        dcc.Graph(
            id='grafico-saida',
            figure=fig_saida
        )
    ], style={'padding': '20px'})
])

# Rodar o servidor Dash
if __name__ == '__main__':
    app.run(debug=True)
