# 🧠 Prácticas de Inteligencia Artificial

¡Hola! 👋 Bienvenido a este repositorio de prácticas de **Inteligencia Artificial**. Aquí vas a encontrar ejercicios y ejemplos para entender cómo funciona la IA desde cero. No necesitas ser un experto: este material está pensado para aprender paso a paso, con ejemplos concretos.

Cada laboratorio se enfoca en un tema específico y te ayuda a aprenderlo con código y ejercicios prácticos. Si te interesa cómo aprenden las máquinas o cómo se toman decisiones automáticas, ¡este repo es para ti!

---

## 📚 ¿Qué vas a encontrar?

### 🔍 Laboratorio 2: Depth First Search (DFS)
- **¿Qué es esto?** Un algoritmo para explorar caminos, como si estuvieras buscando la salida de un laberinto sin saber nada del mapa.
- **¿Cómo funciona?** Prueba caminos uno por uno, y si se encuentra con un obstáculo, retrocede y prueba otro.
- **¿Cuándo usarlo?** Cuando quieres recorrer o explorar todos los posibles caminos, como resolver puzzles o laberintos.
- ✅ **Ejemplo práctico:** Encontrar la salida en un laberinto o resolver un rompecabezas como el 4-puzzle.

---

### 🧩 Laboratorio 3: Resolución de Problemas con Búsqueda Informada
- **¿Qué es esto?** Son técnicas más "inteligentes" que DFS, que intentan adivinar cuál camino es mejor.
- **¿Cómo funciona?** Usa pistas (llamadas heurísticas) para encontrar la solución más rápido.
- **¿Cuándo usarlo?** Cuando el problema es grande y necesitas eficiencia.
- ✅ **Ejemplo práctico:** Planear la mejor ruta para un repartidor (como en Uber o Rappi).

---

### ✅ Laboratorio 4: Métodos de Validación
- **¿Qué es esto?** Técnicas para saber si tu modelo está aprendiendo bien o solo "memorizando".
- **¿Cómo funciona?** Separa los datos en dos partes: una para entrenar y otra para probar.
- **¿Cuándo usarlo?** Siempre que entrenes un modelo, para evitar que falle con nuevos datos.
- ✅ **Ejemplo práctico:** Entrenar un modelo que reconozca correos spam y probar que funcione con nuevos mensajes.

---

### 🤖 Laboratorio 5: Clasificadores Sencillos
- **¿Qué es esto?** Modelos simples que adivinan a qué grupo pertenece algo, comparándolo con ejemplos parecidos.
- **¿Cómo funciona?** Calcula distancias y se fija qué clase tiene su vecino más cercano.
- **¿Cuándo usarlo?** Cuando tienes pocos datos o quieres entender lo básico de clasificación.
- ✅ **Ejemplo práctico:** Saber si una fruta es manzana o naranja con base en su color y tamaño.

---

### 🔄 Laboratorio 6: Validación de Modelos
- **¿Qué es esto?** Una forma más completa de probar tu modelo usando muchas divisiones de datos.
- **¿Cómo funciona?** Repite la validación varias veces con distintas partes del dataset.
- **¿Cuándo usarlo?** Cuando quieres estar más seguro del rendimiento real del modelo.
- ✅ **Ejemplo práctico:** Evaluar bien un modelo que recomienda películas según tus gustos.

---

### 🔎 Laboratorio 7: Modelos de Clasificación
- **¿Qué es esto?** Son versiones prácticas de clasificadores como 1NN o Euclidiano.
- **¿Cómo funciona?** Compara los datos nuevos con los conocidos y decide la clase por cercanía.
- **¿Cuándo usarlo?** Para problemas de clasificación básicos o para comparar con otros modelos.
- ✅ **Ejemplo práctico:** Predecir si un estudiante pasará o no con base en sus calificaciones anteriores.

---

### 📈 Laboratorio 8: Evaluación de Modelos
- **¿Qué es esto?** Comparación entre diferentes modelos para ver cuál funciona mejor.
- **¿Cómo funciona?** Usa métricas como la precisión o la matriz de confusión.
- **¿Cuándo usarlo?** Siempre que tengas varios modelos y quieras elegir el mejor.
- ✅ **Ejemplo práctico:** Comparar qué tan bien clasifican tus modelos correos como spam o no spam.

---

### 🌳 Laboratorio 9: Modelos Avanzados
- **¿Qué es esto?** Modelos más potentes como Árboles de Decisión, Bosques Aleatorios y SVM.
- **¿Cómo funciona?** Aprenden reglas más complejas para tomar decisiones.
- **¿Cuándo usarlo?** Cuando quieres mejorar la precisión de tus predicciones.
- ✅ **Ejemplo práctico:** Usar un Random Forest para predecir si un cliente dejará de usar una app.

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Algunas librerías útiles: `numpy`, `pandas`, `scikit-learn`, `matplotlib`
- Entorno recomendado: Jupyter Notebook o VSCode

---

## 🚀 ¿Cómo usar este repositorio?

1. Clona el proyecto:
   ```bash
   git clone https://github.com/tu_usuario/ia-practicas.git
   cd ia-practicas
