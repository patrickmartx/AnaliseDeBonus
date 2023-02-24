#Bibliotecas instaladas: pandas, openpyxl, twilio
import pandas as pd
from twilio.rest import Client #https://www.twilio.com

# Your Account SID from twilio.com/console
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# Para cada arquivo:
    # Verificar se algum valor na coluna de vendas é maior que 55.000
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes.capitalize()}, alguém bateu a meta.\nVendedor: {vendedor}\nVendas: {vendas}')
        # Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
        message = client.messages.create(
            to="+XXXXXXXXXXXXX",
            from_="+XXXXXXXXXXX",
            body=f'No mês de {mes.capitalize()}, alguém bateu a meta.\nVendedor: {vendedor}\nVendas: {vendas}')
        print(message.sid)