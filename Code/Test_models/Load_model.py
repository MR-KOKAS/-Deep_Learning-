import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import matplotlib.pyplot as plt
import numpy as np
import os
from tensorflow.keras.preprocessing import image


# D_L\Scripts\activate
# deactivate

# Load the model
model = load_model("C:/Users/KOKAS/D_L/Code/Model/cnn_grayscale_model_2.h5")

# Directory with images to predict
image_folder = "C:/Users/KOKAS\D_L/Code/Img"


# Set image target size (replace with your model's expected input size)
image_size = (28, 28)  # Example for typical CNNs; adjust as needed
# Kaggle
#labels=['N', 'R', 'SPACE', 'B', 'I', 'F', 'H', 'E', 'U', 'M', 'X', 'K', 'Q', 'Y', 'S', 'G', 'A', 'O', 'T', 'V', 'Z', 'C', 'P', 'L', 'W', 'D', 'NOTHING', 'J']
# Laptop
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'NOTHING', 'O', 'P', 'Q', 'R', 'S', 'SPACE', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
# Function to preprocess and predict for a single image
def predict_image(image_path):
    # Load and preprocess the image
    # img = load_img(image_path, target_size=image_size, color_mode='grayscale')
    img = load_img(image_path, target_size=image_size)
    img_array = img_to_array(img) / 255.0  # Rescale pixel values if required by the model
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict and return the result
    prediction = model.predict(img_array)
    return prediction,img

# Iterate over all images in the folder and make predictions
for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)

    # Only process files that are images (you can add more extensions if needed)
    if image_path.endswith(('.png', '.jpg', '.jpeg')):
            # Obtiene la predicción (simulación)
            prediction,img = predict_image(image_path)  # Asumimos que esta función ya está definida
            pred_index = np.argmax(prediction)

            # Verificar si el índice coincide con la lista de etiquetas
            if 0 <= pred_index < len(labels):  # Asegura que el índice esté en el rango
                label_predicted = labels[pred_index]
                print(f"Prediction for {image_name}: {label_predicted}")
                # Mostrar la imagen y la etiqueta predicha
                plt.imshow(img)
                plt.title(f"Predicted Label {image_name}: {label_predicted}")
                plt.axis('off')
                plt.show()
            else:
                print("Prediction index out of labels range.")