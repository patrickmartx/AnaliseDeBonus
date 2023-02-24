#Bibliotecas instaladas: pandas, openpyxl, twilio
import pandas as pd

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# Para cada arquivo:
    if (tabela_vendas['Vendas'] > 55000).any():   # Verificar se algum valor na coluna de vendas é maior que 55.000
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes.capitalize()}, alguém bateu a meta.\nVendedor: {vendedor}\nVendas: {vendas}')
        # Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor



# Caso não seja maior do que 55.000, não quero fazer nada