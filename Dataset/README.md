# Proyecto: Reconocimiento de Lenguaje de Señas Americano

Este proyecto tiene como objetivo desarrollar un modelo de aprendizaje profundo para reconocer signos del lenguaje de señas americano (ASL). Se utilizaron diferentes datasets para entrenar, validar y evaluar los modelos desarrollados, incluyendo arquitecturas basadas en CNN y MobileNet.

## Datasets Utilizados

A continuación, se describen los datasets utilizados y su propósito en el proyecto:

### 1. [American Sign Language Dataset](https://www.kaggle.com/datasets/kapillondhe/american-sign-language)
- **Descripción**: Este dataset contiene imágenes de signos del lenguaje de señas americano.
- **Uso**: 
  - Entrenamiento de los modelos basados en CNN y MobileNet.
  - Validación y pruebas de los modelos mencionados. A su vez se usó el set de prueba para evaluar el modelo MobilNet Mejorado.
- **Etiquetas**: Consta de múltiples clases correspondientes a diferentes signos del ASL.

### 2. [Dataset Hand Full Sign](https://www.kaggle.com/datasets/jorgemartinezkokas/dataset-hand-full-sign/data)
- **Descripción**: Dataset personalizado construido a partir de la combinación de cuatro datasets diferentes disponibles en Kaggle.
- **Uso**: 
  - Entrenamiento del modelo MobileNet mejorado.
  - Evaluación de las capacidades del modelo para generalizar características provenientes de distintas fuentes.
- **Construcción**: Este dataset unifica datos para proporcionar un conjunto más robusto y diverso.

### 3. [ASL Alphabet Dataset](https://www.kaggle.com/datasets/debashishsau/aslamerican-sign-language-aplhabet-dataset)
- **Descripción**: Dataset que contiene imágenes del alfabeto ASL en distintas poses y estilos.
- **Uso**: 
  - Solamente se utilizó el conjunto de prueba (test set).
  - Prueba 1: Evaluar la capacidad del modelo para predecir las 28 etiquetas presentes en este dataset.
- **Propósito**: Validar la precisión del modelo en un entorno conocido.

### 4. [Dataset Internet](https://www.kaggle.com/datasets/jorgemartinezkokas/dataset-internet/settings)
- **Descripción**: Conjunto de imágenes recolectadas aleatoriamente de internet.
- **Uso**: 
  - Evaluar la capacidad del modelo para generalizar y reconocer signos en un entorno más diverso y menos controlado.
  - Prueba 2: Determinar si el modelo aprendió las características de los signos o simplemente memorizó los datos de entrenamiento.
- **Propósito**: Demostrar la capacidad del modelo para manejar datos no vistos previamente.

