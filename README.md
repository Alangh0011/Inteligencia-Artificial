# 🧠 Prácticas de Inteligencia Artificial

¡Hola! 👋 Bienvenido a este repositorio de prácticas de **Inteligencia Artificial**. Aquí vas a encontrar ejercicios paso a paso para entender cómo funciona la IA, incluso si estás empezando. Cada laboratorio tiene ejemplos, código y una explicación sencilla de qué hace, cómo lo hace y para qué sirve.

---

## 📚 ¿Qué vas a encontrar?

### 🔍 Laboratorio 2: Depth First Search (DFS)

- **Algoritmo:** Búsqueda en profundidad (DFS).
- **¿Cómo funciona?**
  - Usa una estructura tipo _pila_ (stack) para explorar un camino hasta el final antes de retroceder.
  - Es útil cuando quieres recorrer todos los caminos posibles.
- **Fórmula/Pasos:**
  1. Elige un nodo inicial.
  2. Agrégalo a la pila.
  3. Mientras la pila no esté vacía:
     - Saca el último nodo.
     - Si es la meta, termina.
     - Si no, agrega sus hijos (vecinos) a la pila.
- ✅ **Ejemplo práctico:** Resolver un laberinto o el puzzle 4-puzzle.
- 📦 **Librerías usadas:** `collections`, `copy`

---

### 🧩 Laboratorio 3: Resolución de Problemas con Búsqueda Informada

- **Algoritmos:** A\* (A estrella), Simulated Annealing.
- **¿Cómo funciona?**
  - A\* busca el camino más corto usando heurísticas.
    - `f(n) = g(n) + h(n)`
    - Donde:
      - `g(n)` es el costo del camino hasta el nodo.
      - `h(n)` es la estimación al objetivo.
  - Simulated Annealing simula cómo se enfría un metal para encontrar una solución óptima evitando quedarse en mínimos locales.
- ✅ **Ejemplo práctico:** Planear rutas óptimas para entregas.
- 📦 **Librerías usadas:** `heapq`, `math`, `random`

---

### ✅ Laboratorio 4: Métodos de Validación

- **Técnicas:** Hold-Out, Cross-Validation.
- **¿Cómo funciona?**
  - Hold-Out: divide el dataset en entrenamiento y prueba.
  - Cross-Validation: repite esto varias veces y promedia los resultados.
- **Pasos:**
  1. Separar datos (por ejemplo 80% entrenamiento, 20% prueba).
  2. Entrenar el modelo.
  3. Evaluar el modelo.
- ✅ **Ejemplo práctico:** Validar un modelo que predice si un correo es spam.
- 📦 **Librerías usadas:** `pandas`, `numpy`, `sklearn.model_selection`

---

### 🤖 Laboratorio 5: Clasificadores Sencillos

- **Algoritmos:** 1-NN (Nearest Neighbor), Distancia Euclidiana.
- **¿Cómo funciona?**
  - Calcula la distancia entre el nuevo dato y todos los demás.
  - Elige la clase del dato más cercano.
- **Fórmula:**  
  Euclidiana:  
  `d = sqrt((x1 - x2)^2 + (y1 - y2)^2 + ...)`
- ✅ **Ejemplo práctico:** Clasificar frutas por tamaño y color.
- 📦 **Librerías usadas:** `pandas`, `numpy`, `matplotlib.pyplot`

---

### 🔄 Laboratorio 6: Validación de Modelos

- **Técnica:** K-Fold Cross Validation.
- **¿Cómo funciona?**
  - Divide los datos en _k_ partes y evalúa el modelo _k_ veces cambiando los datos de prueba.
- **Pasos:**
  1. Dividir en K bloques.
  2. Entrenar con K-1 bloques.
  3. Probar con el bloque restante.
  4. Repetir K veces.
- ✅ **Ejemplo práctico:** Evaluar modelo de recomendación.
- 📦 **Librerías usadas:** `pandas`, `numpy`, `sklearn.model_selection.KFold`

---

### 🔎 Laboratorio 7: Modelos de Clasificación

- **Algoritmos:** 1-NN, Clasificador Euclidiano.
- **¿Cómo funciona?**
  - El nuevo punto se clasifica según la clase del punto más cercano.
- ✅ **Ejemplo práctico:** Predecir si un alumno pasará con base en sus calificaciones.
- 📦 **Librerías usadas:** `pandas`, `numpy`, `sklearn.preprocessing`, `sklearn.metrics`

---

### 📈 Laboratorio 8: Evaluación de Modelos

- **Modelos:** 1-NN, K-NN, Naive Bayes.
- **¿Cómo funciona?**
  - K-NN: considera los _k_ vecinos más cercanos.
  - Naive Bayes: calcula la probabilidad de una clase usando Bayes.
- **Fórmula (Naive Bayes):**  
  `P(C|X) = (P(X|C) * P(C)) / P(X)`
- ✅ **Ejemplo práctico:** Detectar correos spam con diferentes algoritmos.
- 📦 **Librerías usadas:** `pandas`, `numpy`, `sklearn.model_selection`, `sklearn.metrics`, `sklearn.naive_bayes`, `sklearn.neighbors`

---

### 🌳 Laboratorio 9: Modelos Avanzados

- **Modelos:** Árboles de Decisión, Random Forest, SVM.
- **¿Cómo funciona?**
  - Árboles: dividen los datos con reglas simples.
  - Random Forest: muchos árboles decidiendo en conjunto.
  - SVM: encuentra el mejor margen para separar clases.
- ✅ **Ejemplo práctico:** Predecir si un usuario dejará de usar una app.
- 📦 **Librerías usadas:** `pandas`, `numpy`, `sklearn.tree`, `sklearn.ensemble`, `sklearn.svm`, `sklearn.metrics`

---

## ⚙️ Requisitos generales

- Python 3.8 o superior
- Algunas librerías comunes:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scikit-learn`

---

## 🚀 ¿Cómo usar este repositorio?

1. Clona el proyecto:
   ```bash
   git clone https://github.com/Alangh0011/Inteligencia-Artificial.git
   cd Inteligencia-Artificial
   ```
