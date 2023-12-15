import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

import joblib

# Cargar los datos de entrenamiento desde un archivo Excel
train_data = pd.read_csv('./train.csv')  # Reemplaza 'train.xlsx' con el nombre de tu archivo Excel de entrenamiento

# Cargar los datos de prueba desde un archivo Excel
test_data = pd.read_csv('./test.csv')  # Reemplaza 'test.xlsx' con el nombre de tu archivo Excel de prueba

# Separar las características (X) y la etiqueta (y) para los datos de entrenamiento
X_train = train_data.drop('class', axis=1)
y_train = train_data['class']

# Separar las características (X) y la etiqueta (y) para los datos de prueba
X_test = test_data.drop('class', axis=1)
y_test = test_data['class']

# Crear y entrenar el modelo Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluar el modelo (opcional)
accuracy = model.score(X_test, y_test)
report = classification_report(y_test, y_pred)

print("Precisión del modelo:", accuracy)
print(f'Exactitud del modelo: {accuracy}')
print("Informe de precisión:", report)

# Guardar el modelo en un archivo .pkl
joblib.dump(model, 'modelo_naive_bayes.pkl')
