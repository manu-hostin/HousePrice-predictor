# app.py
import streamlit as st
import pandas as pd
import joblib


st.set_page_config(page_title="Preditor Titanic", page_icon="🚢")

st.title("🚢 Seriados à Salvo? - Simulador Titanic")
st.markdown("Insira os dados do passageiro para prever se ele sobreviveria ao naufrágio.")


@st.cache_resource
def carregar_modelo():
    return joblib.load('modelo_titanic.pkl')

modelo = carregar_modelo()


st.header("Características do Passageiro")

col1, col2 = st.columns(2)

with col1:
    sexo_texto = st.selectbox("Sexo", ["Masculino", "Feminino"])
    idade = st.number_input("Idade", min_value=0, max_value=100, value=25)
    pclass = st.selectbox("Classe do Navio (Pclass)", [1, 2, 3], index=2)

with col2:
    sibsp = st.number_input("Número de Irmãos/Cônjuges a bordo (SibSp)", min_value=0, max_value=10, value=0)
    fare = st.number_input("Preço da Tarifa (Fare)", min_value=0.0, max_value=500.0, value=32.0)


sexo_numerico = 0 if sexo_texto == "Masculino" else 1


dados_novos = pd.DataFrame([{
    'Pclass': pclass,
    'Sex': sexo_numerico,
    'Age': idade,
    'SibSp': sibsp,
    'Fare': fare
}])

st.divider()


if st.button("Realizar Previsão", type="primary"):
    
    previsao = modelo.predict(dados_novos)[0]
    probabilidade = modelo.predict_proba(dados_novos)[0][1] # Probabilidade de sobreviver
    
    
    if previsao == 1:
        st.success(f"🎉 **Sobreviveria!**")
        st.metric(label="Chance de Sobrevivência", value=f"{probabilidade*100:.1f}%")
    else:
        st.error(f"💀 **Não Sobreviveria.**")
        st.metric(label="Chance de Sobrevivência", value=f"{probabilidade*100:.1f}%")