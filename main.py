#Bibliotecas instaladas: pandas, openpyxl, twilio
import pandas as pd

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

tabela_vendas = pd.read_excel('janeiro.xlsx')


# Para cada arquivo:
#   Verificar se algum valor na coluna de vendas é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000, não quero fazer nada