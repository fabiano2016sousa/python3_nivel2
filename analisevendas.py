import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir("/home/fabiano/Documentos/Cursos/analise1/Vendas")
tabela_total = pd.DataFrame()
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"/home/fabiano/Documentos/Cursos/analise1/Vendas/{arquivo}")
        tabela_total = pd.concat([tabela, tabela_total])
        #print(tabela)

#criação da tabela de produtos vendidos
tabela_produtos = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
#print(tabela_produtos)

#criação da tabela faturamento
#criando primeiramente a aba faturamento
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
#print(tabela_faturamento)
#criando tablea das lojas que mais venderam
tabela_lojas = tabela_total.groupby('Loja').sum(numeric_only=True)
tabela_lojas = tabela_lojas[['Faturamento']]
#print(tabela_lojas)
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y= "Faturamento")
grafico.show()
