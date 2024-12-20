import streamlit as st
import requests
import pandas as pd

st.title("DASHBOARD DE VENDAS:shopping_trolley:")
url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())
if st.button("todos"):
    st.balloons()
    st.metric('Receita',df['Preço'].sum())
    st.metric('Quantidade de vendas (linhas)',df.shape[0])
    st.metric('Quantidade de variáveis (colunas)',df.shape[1])
    st.dataframe(df)
    st.snow()
else:
    st.write("clique no botão todos")



    # Aplicando a lógica de programação do Professor Rômulo, Karython e Kawã.
    # Considerando que o valor esta muito grande, crie uma forma de visualização mais agradável para o usuário.

    # 1 milhão
    # 2 milhões
    # 500 mil
    # 999



    