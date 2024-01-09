# Proyecto Semestral 2: Reconocimiento de Formas en Inteligencia Artificial

## Descripción
Este proyecto se enfoca en el reconocimiento de formas utilizando el dataset de imágenes "Four Shapes" disponible en Kaggle. El objetivo principal es crear una muestra de 1000 patrones que contemple datos de todas las clases presentes en el dataset. Se emplearán momentos invariantes, con dos opciones a considerar: Momentos Invariantes de Hu y Momentos de Zernike.

Además, se explorará la identificación del mejor clasificador para esta tarea utilizando WEKA. Se evaluarán diferentes métodos de validación, como Hold-Out 70/30, 5-Fold Cross-Validation y 10-Fold Cross-Validation. Las medidas de desempeño a considerar incluyen Accuracy, AUC y medidas basadas en la Matriz de Confusión.

Se deben evaluar al menos 10 modelos, donde cada kernel utilizado en el caso de las SVM contará como un modelo aparte. También se realizarán variaciones en los parámetros de los modelos cuando sea aplicable.

## Instrucciones

1. **Descarga del Dataset:**
   - Descarga el dataset de imágenes "Four Shapes" desde el sitio Kaggle: [Four Shapes Dataset](https://www.kaggle.com/datasets/smeschke/four-shapes)

2. **Creación de Muestra de Patrones:**
   - Crea una muestra de 1000 patrones que contemple datos de todas las clases presentes en el dataset.

3. **Empleo de Momentos Invariantes:**
   - Utiliza momentos invariantes para crear patrones (o vectores) de datos. Considera dos opciones: Momentos Invariantes de Hu y Momentos de Zernike.

4. **Selección y Evaluación de Clasificadores:**
   - Utiliza WEKA para identificar el mejor clasificador.
   - Evalúa al menos 10 modelos, considerando diferentes métodos de validación como Hold-Out 70/30, 5-Fold Cross-Validation y 10-Fold Cross-Validation.
   - Medidas de desempeño a evaluar: Accuracy, AUC y medidas basadas en la Matriz de Confusión.
   - En el caso de SVM, cuenta cada kernel utilizado como un modelo aparte y realiza variaciones en sus parámetros cuando sea aplicable.


