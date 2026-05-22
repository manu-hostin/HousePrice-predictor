# 🚢 Titanic Survival Predictor - Machine Learning com Streamlit

Este projeto foi desenvolvido como atividade prática para a disciplina de **Data Science**. O objetivo é aplicar os conceitos de Machine Learning para treinar um modelo preditivo baseado no famoso dataset do Titanic (Kaggle) e disponibilizá-lo através de uma interface web interativa utilizando o Streamlit.

---

## 🎯 Objetivo

O sistema utiliza o algoritmo **Random Forest Classifier** para prever se um passageiro sobreviveria ou não ao naufrágio do Titanic, baseando-se em características informadas em tempo real pelo usuário, tais como:
* Idade
* Sexo
* Classe do navio (Pclass)
* Número de irmãos/cônjuges a bordo (SibSp)
* Preço da tarifa da passagem (Fare)

---

## 📁 Estrutura de Arquivos

```text
/projeto_titanic/
├── train.py           # Código de processamento dos dados e treino do modelo
├── app.py             # Interface gráfica e lógica da aplicação Streamlit
├── train.csv          # Dataset oficial do Titanic (Kaggle)
├── modelo_titanic.pkl # Modelo preditivo treinado e salvo pelo Joblib
└── requirements.txt   # Bibliotecas e dependências do projeto
