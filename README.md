# ❚█══DEEP LEARNING══█❚
🥤- PROJECT - DL - BASE - TEC -🥤
---
**Autor:** Jorge Martínez López  
**Institución:** Tecnológico de Monterrey, Campus Querétaro  
**Email:** A01704518@tec.mx  
**Email Alterno:** jorgemartinez2555@hotmail.com  
---
# Clasificación de Lenguaje de Señas con CNN

Este proyecto explora el uso de redes neuronales convolucionales (CNN) para la clasificación automática del lenguaje de señas, evaluando modelos como MobileNet y versiones mejoradas del mismo.
---
## Objetivo
Diseñar e implementar múltiples modelos basados en CNN para clasificar el lenguaje de señas y analizar su efectividad bajo diferentes condiciones y datasets.
---
## Dataset
Se utilizó el dataset [American Sign Language](https://www.kaggle.com/datasets/kapillondhe/american-sign-language), que contiene:
- **28 clases**: 26 letras, "Espacio" y "Nada".
- **Imágenes**: Cada una de 400x400 píxeles en formato RGB.

El dataset fue dividido en:
- **Entrenamiento**: 90% del conjunto de datos.
- **Validación**: 10% del conjunto de datos.
- **Prueba**: 112 imágenes con etiquetas balanceadas.
---
## Modelos Implementados
### 1. CNN Básica
- Arquitectura clásica con capas convolucionales, max-pooling y densas.
- **Precisión en el set de prueba**: 100%.

### 2. MobileNet Pre-entrenado
- Basado en MobileNetV2, optimizado para dispositivos móviles.
- **Precisión en el set de prueba**: 100%.

### 3. MobileNet Mejorado
- Cambios realizados para mejorar la generalización:
  - Reemplazo de `Flatten` con `GlobalAveragePooling`.
  - Eliminación de `Dropout` innecesarios.
  - Incremento de neuronas en capas densas.
  - Regularización L1 en la capa de salida.
- **Precisión en el set de prueba**: 100%.
---
## Resultados
Los modelos fueron evaluados en escenarios más desafiantes:
1. **Prueba con otro dataset de lenguaje de señas**:
   - CNN: 14% de precisión.
   - MobileNet: 10% de precisión.
   - MobileNet Mejorado: 100% de precisión.

2. **Prueba con imágenes aleatorias de internet**:
   - CNN: 9% de precisión.
   - MobileNet: 18% de precisión.
   - MobileNet Mejorado: 63% de precisión.
---
## Conclusiones
- **MobileNet Mejorado** mostró ser el modelo más robusto en condiciones desafiantes, logrando una precisión del 100% en escenarios controlados y destacando en pruebas externas.
- Las mejoras aplicadas permitieron reducir el sobreajuste y mejorar la capacidad de generalización.
- Sin embargo, el rendimiento en datasets externos sugiere oportunidades de mejora en la calidad y diversidad de los datos utilizados.
---
## Requisitos
- Python 3.8+
- TensorFlow/Keras
- Bibliotecas: NumPy, Matplotlib, scikit-learn

