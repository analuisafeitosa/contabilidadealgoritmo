# Dashboard de Movimentação Bancária

## Descrição do Projeto
Este projeto foi desenvolvido como parte da disciplina de **Contabilidade**, com o objetivo de criar um **dashboard interativo** para auxiliar uma empresa de publicidade na análise de suas movimentações financeiras. O sistema permite visualizar receitas, despesas e lucros mensais, fornecendo insights financeiros importantes para a tomada de decisões.

O dashboard foi implementado utilizando **Python**, com as bibliotecas **Dash** e **Plotly** para visualização de dados, e **SQLite** como banco de dados para armazenamento das movimentações financeiras.

---

## Funcionalidades
- **Visualização de Receitas e Despesas Mensais**: Gráficos interativos que mostram os valores de entrada (receitas) e saída (despesas) por mês.
- **Cálculo de Lucro Mensal**: Exibição do lucro mensal (receitas - despesas) com barras coloridas indicando lucros positivos (verde) e negativos (vermelho).
- **Indicadores Financeiros**: Exibição do total de receitas e despesas no topo do dashboard.
- **Armazenamento de Dados**: Utilização de um banco de dados SQLite para armazenar e consultar as movimentações financeiras.
- **Importação de Dados**: Possibilidade de carregar dados financeiros a partir de arquivos CSV.

---

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Dash**: Framework para criação de dashboards interativos.
- **Plotly**: Biblioteca para visualização de gráficos.
- **SQLite**: Banco de dados para armazenamento das movimentações financeiras.
- **Pandas**: Biblioteca para manipulação e análise de dados.

---

## Estrutura do Projeto
- **`dashboard.py`**: Arquivo principal que implementa o dashboard interativo.
- **`acessoaobd.py`**: Script para criar a tabela no banco de dados e carregar os dados a partir de um arquivo CSV.
- **`bd.py`**: Script para consultar e exibir os dados armazenados no banco de dados SQLite.
- **`movimentacao3.csv`**: Arquivo CSV contendo as movimentações financeiras da empresa.

---

## Como Executar o Projeto
1. **Instale as dependências necessárias**:
   - Execute o comando abaixo no terminal para instalar as bibliotecas:
     ```bash
     pip install dash pandas plotly
     ```

2. **Configure o banco de dados**:
   - Execute o arquivo `acessoaobd.py` para criar a tabela no banco de dados e carregar os dados do arquivo `movimentacao3.csv`.

3. **Inicie o dashboard**:
   - Execute o arquivo `dashboard.py`:
     ```bash
     python dashboard.py
     ```
   - O dashboard estará disponível no navegador no endereço `http://127.0.0.1:8050`.

4. **Visualize os dados**:
   - Utilize o dashboard para explorar as receitas, despesas e lucros da empresa.

---

## Exemplos de Uso
- **Análise de Receitas e Despesas**: Identifique os meses com maior receita ou despesa para planejar estratégias financeiras.
- **Monitoramento de Lucros**: Avalie os meses em que a empresa teve prejuízo e tome decisões para melhorar a lucratividade.
- **Planejamento Financeiro**: Use os dados para criar projeções e metas financeiras.

---

## Integrantes do Grupo
Este projeto foi desenvolvido pelos seguintes integrantes:
1. Amós Kinsley
2. Ana Luisa Feitosa
3. Lucas dos Santos
4. Saunay Coutinho

---

## Aplicação na Empresa de Publicidade
O dashboard foi projetado para atender às necessidades de uma empresa de publicidade, permitindo:
- Monitorar o fluxo de caixa mensal.
- Identificar períodos de maior ou menor lucratividade.
- Auxiliar na tomada de decisões estratégicas baseadas em dados financeiros.

---

## Licença
Este projeto foi desenvolvido exclusivamente para fins acadêmicos e não possui licença para uso comercial.
