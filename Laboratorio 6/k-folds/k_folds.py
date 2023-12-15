import pandas as pd
import os

# Entrada para el nombre del conjunto de datos
dataset_name = input("¿Cuál es el nombre del conjunto de datos? ")
# Comprobar que el conjunto de datos existe
while not os.path.exists(f"{dataset_name}.csv"):
    print(f"\n[x] El conjunto de datos '{dataset_name}' no existe.")
    dataset_name = input("¿Cuál es el nombre del conjunto de datos? ")

# Cargar los datos desde el archivo CSV
data = pd.read_csv(f"{dataset_name}.csv")

# Asegurarse de que los datos estén aleatorizados
data = data.sample(frac=1, random_state=0)

# Entrada para la variable objetivo
target = input("¿Cuál es la variable objetivo? ")
# Comprobar que la variable objetivo existe en el conjunto de datos
while target not in data.columns:
    print(f"\n[x] La variable objetivo '{target}' no existe en el conjunto de datos.")
    target = input("¿Cuál es la variable objetivo? ")

# Número de pliegues
k = 10

# Crear directorio para guardar los pliegues
if not os.path.exists("folds"):
    os.makedirs("folds")

# Lista para almacenar los pliegues
folds = [pd.DataFrame()] * k

# Dividir cada grupo (especie) en k pliegues estratificados
for _, group in data.groupby(target):
    group_size = len(group)
    fold_size = group_size // k
    remainder = group_size % k
    fold_indices = []
    start_index = 0

    for j in range(k):
        end_index = start_index + fold_size + (1 if j < remainder else 0)
        fold_indices.append((start_index, end_index))
        start_index = end_index

    # Añadir las muestras de la especie actual a los pliegues correspondientes
    for j, (start, end) in enumerate(fold_indices):
        folds[j] = pd.concat([folds[j], group.iloc[start:end]])

# Función para mostrar la distribución de clases en un conjunto de datos
def display_class_distribution(data, target, set_name):
    class_distribution = data[target].value_counts()
    proportions = [f"{class_name}: {count} ({count / len(data) * 100:.2f}%)" for class_name, count in class_distribution.items()]
    print(f"{set_name}:  {'  '.join(proportions)}")

# Mostrar la distribución de clases en cada fold
for i, fold_data in enumerate(folds):
    display_class_distribution(fold_data, target, f"Fold {i+1}")

# Guardar los pliegues en archivos CSV
for i, fold_data in enumerate(folds):
    fold_data.to_csv(f"folds/{dataset_name}_fold_{i + 1}.csv", index=False)

print(f"\n[*] {k} pliegues se han guardado en archivos CSV en el directorio 'folds'.")

