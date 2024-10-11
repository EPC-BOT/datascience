# Aplicando a lógica de programação do Professor Rômulo, Karython e Kawã.
    # Considerando que o valor esta muito grande, crie uma forma de visualização mais agradável para o usuário.

    # 1 milhão
    # 2 milhões
    # 500 mil
    # 999


import streamlit as st
import requests
import pandas as pd

# Função para formatar valores
def formatar_valor(valor):
    if valor >= 1_000_000:
        return f"{valor / 1_000_000:.1f} milhões"
    elif valor >= 1_000:
        return f"{valor / 1_000:.1f} mil"
    else:
        return str(valor)

st.title("DASHBOARD DE VENDAS:shopping_trolley:")
url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())

if st.button("todos"):
    st.balloons()
    
    receita_total = df['Preço'].sum()
    st.metric('Receita', formatar_valor(receita_total))
    st.metric('Quantidade de vendas (linhas)', df.shape[0])
    st.metric('Quantidade de variáveis (colunas)', df.shape[1])
    st.dataframe(df)
    st.snow()
else:
    st.write("clique no botão todos")
