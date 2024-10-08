import pandas as pd

# Carrega o DataFrame
df = pd.read_csv('/data/ecommerce_tratados.csv')

# Verifica a quantidade de dados únicos em cada coluna antes de qualquer modificação
unicos = df.nunique()
print('Análise de dados únicos:\n', unicos)

# Calcula estatísticas descritivas dos campos numéricos
estatisticas = df.describe()
print('Estatísticas dos dados:\n', estatisticas)

# Cria o campo "Preço"
df['Preco'] = df['Reais'] + (df['Centavos'] / 100)

# Remove os campos citados
df = df.drop(columns=['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'])

# Verifica a quantidade de dados únicos após a remoção
unicos_apos = df.nunique()
print('Análise de dados únicos após remoção:\n', unicos_apos)

# Verifica as estatísticas dos campos numéricos novamente
estatisticas_apos = df.describe()
print('Estatísticas dos dados após remoção:\n', estatisticas_apos)