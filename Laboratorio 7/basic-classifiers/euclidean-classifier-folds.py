import pandas as pd
import numpy as np

def classify_point(point, centroids):
    # Calcular la distancia euclidiana entre el punto y cada centroide
    # linalg = linear algebra, norm = norma, axis=1 para calcular la norma de cada fila
    distancias = np.linalg.norm(centroids - point, axis=1)
    # Obtener el índice del centroide más cercano
    return centroids.index[distancias.argmin()]


def cross_validate(folds, target):
    accuracies = []
    num_folds = len(folds)
    for i in range(num_folds):
        # Obtener los conjuntos de entrenamiento y prueba
        # El conjunto de entrenamiento es la unión de todos los folds excepto el i-ésimo
        try:
            train_data = pd.concat([folds[j] for j in range(num_folds) if j != i])
            X_train = train_data.drop(columns=[target])
            y_train = train_data[target]

            # El conjunto de prueba es el i-ésimo fold
            test_data = folds[i]
            X_test = test_data.drop(columns=[target])
            y_test = test_data[target]
        except KeyError:
            print(f"\n[x] La variable objetivo {target} no existe en los datos.")
            exit()

        # Entrenar el clasificador, es decir, calcular los centroides
        centroids = X_train.groupby(y_train).mean()
        # Imprimir los centroides
        print("\nCentroides - Fold", i + 1)
        print(centroids)

        # Calcular la distancia euclidiana entre cada ejemplo de prueba y cada centroide
        y_pred = X_test.apply(classify_point, axis=1, centroids=centroids)

        # Calcular la precisión del clasificador
        accuracy = (y_pred == y_test).mean()
        accuracies.append(accuracy)

    return np.mean(accuracies)


# Comprobar que el conjunto de datos existe
try:
    dataset_name = input("¿Cuál es el nombre del conjunto de datos? ")
    # Cargar los datos desde el archivo CSV
    train_data = [pd.read_csv(f"folds/{dataset_name}_folds/{dataset_name}_fold_{i}.csv") for i in range(1, 11)]
except FileNotFoundError:
    print(f"\n[x] No se encontraron los datos ingrsados.")
    exit()

target = input("¿Cuál es la variable objetivo? ")

# Mostrar las predicciones vs los valores reales
# print("\nPredicciones vs valores reales:")
# print(pd.DataFrame({"Predicción": y_pred, "Real": y_test}))


# Calcular la precisión del clasificador
accuracy = cross_validate(train_data, target)
print(f"\nPrecisión: {accuracy * 100:.2f}%")
