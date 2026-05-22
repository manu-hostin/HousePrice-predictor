# 🏠 London House Price Predictor

Este é um projeto de Machine Learning desenvolvido para a **Prova 04 da disciplina de Data Science**. A aplicação utiliza um modelo preditivo supervisionado para estimar o valor de propriedades em Londres com base em suas características estruturais.

## 🚀 Tecnologias Utilizadas
* **Python 3.9+**
* **Streamlit** (Interface Gráfica Interativa)
* **Scikit-Learn** (Algoritmo Random Forest Regressor)
* **Joblib** (Persistência e carregamento do modelo treinado)
* **Pandas** (Manipulação de dados)

## 📁 Estrutura do Projeto
```text
projeto_propriedades/
├── data/
│   └── dataset.csv       # Base de dados das propriedades
├── train.py              # Script de tratamento e treino do modelo
├── app.py                # Interface web interativa do Streamlit
├── modelo.pkl            # Modelo treinado salvo via Joblib
└── requirements.txt      # Bibliotecas necessárias para execução
````


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
