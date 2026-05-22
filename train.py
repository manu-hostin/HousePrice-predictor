import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv('data/dataset.csv')

features = ['Bedrooms', 'Bathrooms', 'Square Meters', 'Building Age', 'Floors']
X = df[features]
y = df['Price (£)']

X = X.fillna(X.median())

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, 'modelo.pkl')

print("✨ Sucesso! O modelo de propriedades foi treinado e salvo como 'modelo.pkl'.")