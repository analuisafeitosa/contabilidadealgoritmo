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

# Calcular a Receita Mensal e Despesa Mensal por mês
df_monthly = df.groupby('Ano-Mês').agg({'Entrada': 'sum', 'Saida': 'sum'}).reset_index()

# Calcular o lucro (Receita - Despesa) para cada mês
df_monthly['Lucro'] = df_monthly['Entrada'] - df_monthly['Saida']

# Criar o gráfico de "Entrada" (Receita), agrupado por mês
fig_entrada = px.bar(df_monthly, x='Ano-Mês', y='Entrada', 
                     title='Receitas (Entrada) por Mês',
                     labels={'Entrada': 'Valor da Receita'},
                     template='plotly_dark',
                     color='Ano-Mês')

# Criar o gráfico de "Saida" (Despesa), agrupado por mês
fig_saida = px.bar(df_monthly, x='Ano-Mês', y='Saida', 
                   title='Despesas (Saída) por Mês',
                   labels={'Saida': 'Valor da Despesa'},
                   template='plotly_dark',
                   color='Ano-Mês')

# Criar o gráfico de "Lucro" (Lucro Mensal), com barras para lucro negativo abaixo do eixo X
fig_lucro = px.bar(df_monthly, x='Ano-Mês', y='Lucro',
                   title='Lucro Mensal',
                   labels={'Lucro': 'Valor do Lucro'},
                   template='plotly_dark')

# Atualizar o gráfico para colorir as barras de acordo com o lucro (verde para positivo, vermelho para negativo)
fig_lucro.update_traces(marker_color=df_monthly['Lucro'].apply(lambda x: 'green' if x >= 0 else 'red'))

# Criar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do Dash com três gráficos (Receitas, Despesas e Lucro)
app.layout = html.Div([
    # Importando a fonte do Google Fonts
    html.Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap'),
    
    html.H1("BeeFin", style={'textAlign': 'center', 'fontFamily': 'Roboto'}),
    
    # Exibir o total de Receita e Despesa no topo
    html.Div([
        html.Div([
            html.H4(f"Total Receita: R$ {df['Entrada'].sum():,.2f}", style={'textAlign': 'center', 'fontFamily': 'Roboto'}),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'backgroundColor': '#4CAF50', 'color': 'white'}),
        
        html.Div([
            html.H4(f"Total Despesa: R$ {df['Saida'].sum():,.2f}", style={'textAlign': 'center', 'fontFamily': 'Roboto'}),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'backgroundColor': '#f44336', 'color': 'white'}),
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'margin': '20px'}),
    
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
    ], style={'padding': '20px'}),
    
    # Gráfico de Lucro (Mensal)
    html.Div([
        dcc.Graph(
            id='grafico-lucro',
            figure=fig_lucro
        )
    ], style={'padding': '20px'})
])

# Rodar o servidor Dash
if __name__ == '__main__':
    app.run(debug=True)
