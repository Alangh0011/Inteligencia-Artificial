import pandas as pd
import numpy as np

def knn_classify(k, X_train, y_train, X_test):
    y_pred = []
    for test_point in X_test.iterrows():
        distances = np.linalg.norm(X_train - test_point[1], axis=1)
        nearest_indices = np.argsort(distances)[:k]
        nearest_labels = y_train.iloc[nearest_indices]
        unique, counts = np.unique(nearest_labels, return_counts=True)
        predicted_label = unique[np.argmax(counts)]
        y_pred.append(predicted_label)
    return y_pred

def cross_validate(folds, target, k):
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

        # Entrenar el clasificador KNN
        y_pred = knn_classify(k, X_train, y_train, X_test)

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
    print(f"\n[x] No se encontraron los datos ingresados.")
    exit()

target = input("¿Cuál es la variable objetivo? ")
k = 1 

# Calcular la precisión del clasificador
accuracy = cross_validate(train_data, target, k)
print(f"\nPrecisión (K={k}): {accuracy * 100:.2f}%")
