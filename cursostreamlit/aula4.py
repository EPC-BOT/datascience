import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Gato")
    st.image("https://www.superpet.club/blog/wp-content/uploads/2024/02/estimular-gatos.jpg")


with col2:
    st.header("Cachorro")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi2F3rB_YW8BvsvYtXPOsScDmQTMUwpBi_Og&s")


with col3:
    st.header("Coruja")
    st.image("https://www.revistacircuito.com/wp-content/uploads/2023/07/Coruja-das-Neves.jpg")