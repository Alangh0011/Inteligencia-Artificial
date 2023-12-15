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

try:
    dataset_name = input("¿Cuál es el nombre del conjunto de datos? ")
    train_data = pd.read_csv(f"holdout/{dataset_name}_train.csv")
    test_data = pd.read_csv(f"holdout/{dataset_name}_test.csv")
    target = input("¿Cuál es la variable objetivo? ")

    X_train = train_data.drop(columns=[target])
    y_train = train_data[target]
    X_test = test_data.drop(columns=[target])
    y_test = test_data[target]

except FileNotFoundError:
    print(f"\n[x] No se encontraron los datos ingresados.")
    exit()

k = 1  
y_pred = knn_classify(k, X_train, y_train, X_test)

# Calcular la precisión del clasificador
accuracy = (y_pred == y_test).mean()
print(f"\nPrecisión: {accuracy * 100:.2f}%")
