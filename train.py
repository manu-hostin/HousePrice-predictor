# train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib


df = pd.read_csv('train.csv')


features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Fare']
target = 'Survived'

X = df[features].copy()
y = df[target]


X['Age'] = X['Age'].fillna(X['Age'].median())

X['Fare'] = X['Fare'].fillna(X['Fare'].median())

X['Sex'] = X['Sex'].map({'male': 0, 'female': 1})


modelo = RandomForestClassifier(random_state=42, n_estimators=100)
modelo.fit(X, y)


joblib.dump(modelo, 'modelo_titanic.pkl')
print("Modelo treinado e salvo com sucesso como 'modelo_titanic.pkl'!")