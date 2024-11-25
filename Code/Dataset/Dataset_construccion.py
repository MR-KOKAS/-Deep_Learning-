import os
import shutil

# Directorios de entrada
input_dirs = [
    'K://DATASET//ASL_Dataset//Train',
    'K://DATASET//ASL_Dataset2//ASL_Alphabet_Dataset//asl_alphabet_train',
    'K://DATASET//ASL_Dataset3//asl_dataset',
    'K://DATASET//ASL_Dataset4//Train'
]

# Directorio de salida
output_dir = 'K://DATASET//DATSET_BIG'

# Crear el directorio de salida
os.makedirs(output_dir, exist_ok=True)

# Crear carpetas para cada letra del abecedario en el directorio de salida
letters =letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','NOTHING','SPACE']
for letter in letters:
    os.makedirs(os.path.join(output_dir, letter), exist_ok=True)

# Copiar archivos por letra
for input_dir in input_dirs:
    for letter in letters:
        letter_dir = os.path.join(input_dir, letter)
        if os.path.exists(letter_dir):
            for filename in os.listdir(letter_dir):
                src_path = os.path.join(letter_dir, filename)
                dst_path = os.path.join(output_dir, letter, filename)
                
                # Evita duplicados
                if not os.path.exists(dst_path):
                    shutil.copy2(src_path, dst_path)

print("Archivos copiados correctamente en el directorio de salida por letra.")
