import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Calculadora de Imóveis Londres", page_icon="🏠", layout="centered")

st.title("🏠 Precificação Inteligente de Imóveis")
st.write("Insira as características do imóvel abaixo para estimar o valor de mercado via Machine Learning.")

@st.cache_resource
def load_model():
    return joblib.load('modelo.pkl')

model = load_model()

st.subheader("📋 Características do Imóvel")

col1, col2 = st.columns(2)

with col1:
    m2 = st.number_input("Área Útil (Square Meters)", min_value=10, max_value=1000, value=120, step=5)
    quartos = st.slider("Quantidade de Quartos (Bedrooms)", min_value=1, max_value=10, value=3)
    banheiros = st.slider("Quantidade de Banheiros (Bathrooms)", min_value=1, max_value=5, value=2)

with col2:
    idade_predio = st.number_input("Idade do Prédio (Building Age)", min_value=0, max_value=200, value=20, step=1)
    andares = st.number_input("Total de Andares da Propriedade (Floors)", min_value=1, max_value=5, value=1, step=1)

st.divider()

dados_usuario = pd.DataFrame([{
    'Bedrooms': quartos,
    'Bathrooms': banheiros,
    'Square Meters': m2,
    'Building Age': idade_predio,
    'Floors': andares
}])

if st.button("💰 Calcular Preço Estimado", use_container_width=True):
   
    predicao = model.predict(dados_usuario)[0]
    
    st.success("🎯 Previsão calculada com sucesso!")
    st.metric(
        label="Valor Estimado da Propriedade", 
        value=f"£ {predicao:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
    
    st.info("Nota: Este valor é uma estimativa estatística baseada no padrão dos dados históricos fornecidos.")