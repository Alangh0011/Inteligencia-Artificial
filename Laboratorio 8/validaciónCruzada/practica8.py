from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

while True:
    # Obtener el nombre del conjunto de datos
    dataset_name = input("\n¿Cuál es el nombre del conjunto de datos?: ")

    try:
        data = pd.read_csv(f"{dataset_name}.csv")
    except FileNotFoundError:
        print(f"Error: El archivo '{dataset_name}.csv' no existe. Por favor, asegúrate de que el archivo existe en el directorio actual o proporciona la ruta correcta al archivo.")
        continue

    # Separar las características (X) y la etiqueta (y)
    main_label = input("Escribe la etiqueta principal: ")

    try:
        X = data.drop(f'{main_label}', axis=1)
        y = data[f'{main_label}']
    except KeyError:
        print(f"Error: La etiqueta '{main_label}' no existe en el conjunto de datos.")
        continue

    # Elegir entre KNN y Naive Bayes
    classifier_choice = input("Selecciona el clasificador (knn o nb): ").lower()

    if classifier_choice == 'knn':
        vecinos = int(input ("Digita el numero de vecinos cercanos: "))
        classifier = KNeighborsClassifier(n_neighbors=vecinos)
    elif classifier_choice == 'nb':
        classifier = GaussianNB()
    else:
        print("Opción no válida. Seleccionando KNN por defecto con vecinos igual a 1.\n")
        classifier = KNeighborsClassifier(n_neighbors=1)

    # Crear un objeto KFold con k pliegues
    kf = KFold(n_splits=10)

    # Inicializar una lista para almacenar las puntuaciones de precisión de cada iteración
    accuracy_scores = []

    # Inicializar una matriz de confusión acumulada
    confusion_matrix_sum = np.zeros((len(np.unique(y)), len(np.unique(y))), dtype=int)

    # Iterar a través de los pliegues
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        # Entrenar el modelo seleccionado
        classifier.fit(X_train, y_train)

        # Hacer predicciones en el conjunto de prueba
        y_pred = classifier.predict(X_test)

        # Calcular la matriz de confusión para esta iteración
        confusion = confusion_matrix(y_test, y_pred, labels=np.unique(y))

        confusion_matrix_sum += confusion

        # Calcular la puntuación de precisión para esta iteración
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_scores.append(accuracy)

    # Calcular el promedio de las puntuaciones de precisión
    average_accuracy = sum(accuracy_scores) / k

    print("\nPuntuaciones de precisión por iteración:", accuracy_scores)
    print("\nPrecisión promedio:", average_accuracy)

    # Visualizar la matriz de confusión general utilizando ConfusionMatrixDisplay
    disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_sum, display_labels=np.unique(y))
    disp.plot(cmap='Blues', values_format='d')
    plt.title("Matriz de Confusión General")
    plt.show()

    # Preguntar al usuario si desea ejecutar nuevamente
    ejecutar_nuevamente = input("\n¿Deseas ejecutar nuevamente? (s/n): ").lower()
    if ejecutar_nuevamente != 's':
        break
