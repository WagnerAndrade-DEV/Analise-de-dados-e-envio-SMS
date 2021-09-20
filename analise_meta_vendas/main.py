import pandas as pd
from twilio.rest import Client

account_sid = "ACb8f18cfb7921fed7a6d7ea56b45a111a"

auth_token = "bfb585ddd4e8b70d45915b8abd5b4a6c"

client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        message = client.messages.create(
            to="+5512981881894",
            from_="+14807712228",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)