


# 1. Crie um algoritimo que descubra um numero secreto!

# 2. Criar o numero secreto

# 3. Título na aplicação

# 4. Dar uma mensagem de boas vindas

# 5. Receber o chute do usuário

# 6. Verificar o chute com o número secreto

# 7. Mostrar uma mensagem personalizada

import streamlit as st
import random

# 1. Título na aplicação
st.title("Adivinhe o Número Secreto!")

# 2. Criar o número secreto
numero_secreto = random.randint(1, 5)

# 3. Mensagem de boas-vindas
st.write("Bem-vindo ao jogo! Tente adivinhar o número secreto entre 1 e 100.")

# 4. Receber o chute do usuário
chute = st.number_input("Digite seu palpite:", min_value=1, max_value=100, step=0)

# 5. Verificar o chute com o número secreto
if st.button("Adivinhar"):
    if chute < numero_secreto:
        st.balloons()
        st.write("Seu palpite é muito baixo! Tente novamente.")
        st.snow()
    elif chute > numero_secreto:
        st.write("Seu palpite é muito alto! Tente novamente.")
    else:
        st.write(f"Parabéns! Você adivinhou o número secreto!{numero_secreto}")
    


