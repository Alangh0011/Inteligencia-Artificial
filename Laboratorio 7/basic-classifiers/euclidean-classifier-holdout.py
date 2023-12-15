import pandas as pd
import numpy as np
import os


def classify_point(point, centroids):
    # Calcular la distancia euclidiana entre el punto y cada centroide
    # linalg = linear algebra, norm = norma, axis=1 para calcular la norma de cada fila
    distancias = np.linalg.norm(centroids - point, axis=1)
    # Obtener el índice del centroide más cercano
    return centroids.index[distancias.argmin()]


# Comprobar que el conjunto de datos existe
try:
    dataset_name = input("¿Cuál es el nombre del conjunto de datos? ")
    # Cargar los datos desde el archivo CSV
    train_data = pd.read_csv(f"holdout/{dataset_name}_train.csv")
    test_data = pd.read_csv(f"holdout/{dataset_name}_test.csv")
    target = input("¿Cuál es la variable objetivo? ")
    # Obtener los conjuntos de entrenamiento y prueba
    X_train = train_data.drop(columns=[target])
    y_train = train_data[target]

    X_test = test_data.drop(columns=[target])
    y_test = test_data[target]
except FileNotFoundError:
    print(f"\n[x] No se encontraron los datos ingrsados.")
    exit()

# Entrenar el clasificador, es decir, calcular los centroides
centroids = X_train.groupby(y_train).mean()

print("\nCentroides:")
print(centroids)

# Calcular la distancia euclidiana entre cada ejemplo de prueba y cada centroide
y_pred = X_test.apply(classify_point, axis=1, centroids=centroids)

# Mostrar las predicciones vs los valores reales
# print("\nPredicciones vs valores reales:")
# print(pd.DataFrame({"Predicción": y_pred, "Real": y_test}))


# Calcular la precisión del clasificador
accuracy = (y_pred == y_test).mean()
print(f"\nPrecisión: {accuracy * 100:.2f}%")
