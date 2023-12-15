import pandas as pd
import os

dataset_name = input("¿Cuál es el nombre del conjunto de datos? ")
# Comprobar que el conjunto de datos existe
while not os.path.exists(f"{dataset_name}.csv"):
    print(f"\n[x] El conjunto de datos '{dataset_name}' no existe.")
    dataset_name = input("¿Cuál es el nombre del conjunto de datos? ")

# Cargar los datos desde el archivo CSV
data = pd.read_csv(f"{dataset_name}.csv")

# Asegurarse de que los datos estén aleatorizados
data = data.sample(frac=1, random_state=0)

# Definir la proporción para la división
train_ratio = 0.8  # 70% para entrenamiento, 30% para prueba

# Declaramos los conjuntos de entrenamiento y prueba
train_data = pd.DataFrame()
test_data = pd.DataFrame()

target = input("¿Cuál es la variable objetivo? ")
# Comprobar que la variable objetivo existe en el conjunto de datos
while target not in data.columns:
    print(f"\n[x] La variable objetivo '{target}' no existe en el conjunto de datos.")
    target = input("¿Cuál es la variable objetivo? ")


# Dividir los datos en conjuntos de entrenamiento y prueba según la proporción
for _, group_data in data.groupby(target):
    # Obtener el número de ejemplos para cada especie
    n = len(group_data)
    # Calcular el número de ejemplos para cada conjunto
    n_train = int(n * train_ratio)
    n_test = n - n_train
    # Dividir los datos en conjuntos de entrenamiento y prueba
    train_data = pd.concat([train_data, group_data.iloc[:n_train]])
    test_data = pd.concat([test_data, group_data.iloc[n_train:]])

# Comprobar que los conjuntos generados son disjuntos
intersection = set(train_data.index) & set(test_data.index)
if len(intersection) == 0:
    print("\n[*] Los conjuntos de entrenamiento y prueba son disjuntos.")
else:
    print("\n[x] Los conjuntos de entrenamiento y prueba NO son disjuntos.")

# Comprobar que los conjuntos generados tienen la misma proporción de clases
train_class_distribution = train_data[target].value_counts()
test_class_distribution = test_data[target].value_counts()

# Mostrar la distribución de clases en el conjunto de entrenamiento en porcentaje
# y en número de ejemplos

print("\nDistribución de clases en el conjunto de entrenamiento:")
for class_name, count in train_class_distribution.items():
    print(f"{class_name}: {count} ({count / len(train_data) * 100:.2f}%)")

print("\nDistribución de clases en el conjunto de prueba:")
for class_name, count in test_class_distribution.items():
    print(f"{class_name}: {count} ({count / len(test_data) * 100:.2f}%)")


# Guardar los conjuntos de entrenamiento y prueba en archivos CSV
train_data.to_csv(f"{dataset_name}_train.csv", index=False)
test_data.to_csv(f"{dataset_name}_test.csv", index=False)
