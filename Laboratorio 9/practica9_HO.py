import pandas as pd
import sklearn.model_selection as ms
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

if __name__ == "__main__":
    dataset = input("¿Cuál es el nombre del conjunto de datos? ")
    data = pd.read_csv(f"{dataset}.csv")
    target = input("¿Cuál es la variable objetivo? ")
    X = data.drop(columns=[target])
    y = data[target]
    
    # Dividir el conjunto de datos en entrenamiento y prueba 70/30
    X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.3, random_state=0, stratify=y, shuffle=True)

    # Seleccionar entre J48 (ID5), Random Forest, SVM lineal, SVM polinomial o SVM gaussiana
    classifier_choice = input("Selecciona el clasificador (j48, rf, svm_linear, svm_poly, svm_rbf): ").lower()

    if classifier_choice == 'j48':
        clf = DecisionTreeClassifier()
    elif classifier_choice == 'rf':
        clf = RandomForestClassifier()
    elif classifier_choice == 'svm_linear':
        clf = SVC(kernel='linear')
    elif classifier_choice == 'svm_poly':
        degree = int(input("Ingresa el grado del kernel polinomial: "))
        clf = SVC(kernel='poly', degree=degree)
    elif classifier_choice == 'svm_rbf':
        clf = SVC(kernel='rbf')
    else:
        print("Opción no válida. Seleccionando J48 por defecto.\n")
        clf = DecisionTreeClassifier()

    # Entrenar el clasificador
    clf.fit(X_train, y_train)

    # Realizar las predicciones
    y_pred = clf.predict(X_test)

    # Calcular la precisión del clasificador
    accuracy = (y_pred == y_test).mean()
    print(f"\nPrecisión: {accuracy * 100:.2f}%")

    # Imprimir la matriz de confusión con matplotlib y seaborn
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 7))
    cmap = sns.color_palette("flare", as_cmap=True)
    class_labels = data[target].unique()
    sns.set(font_scale=2)
    sns.heatmap(cm, annot=True, fmt='d', cmap=cmap, xticklabels=class_labels, yticklabels=class_labels)
    plt.xlabel('Predicho')
    plt.ylabel('Verdadero')
    plt.show()
