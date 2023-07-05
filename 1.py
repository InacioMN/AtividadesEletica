import tensorflow as tf
import numpy as np
from PIL import Image

# Carregar o modelo pré-treinado
model = tf.keras.applications.ResNet50(weights='imagenet')

# Função para pré-processar a imagem
def preprocess_image(image):
    img = image.resize((224, 224))  # Redimensionar a imagem para o tamanho esperado pelo modelo
    img_array = np.array(img)  # Converter a imagem em um array NumPy
    img_array = img_array / 255.0  # Normalizar os valores dos pixels para o intervalo [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Adicionar uma dimensão extra para representar o batch
    return img_array

# Função para identificar objetos na imagem
def identify_objects(image_path):
    image = Image.open(image_path)
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    top_predictions = tf.keras.applications.resnet50.decode_predictions(predictions, top=3)[0]
    objects = [(class_name, round(probability * 100, 2)) for (_, class_name, probability) in top_predictions]
    return objects

# Caminho da imagem que você deseja identificar
image_path = 'caminho/para/sua/imagem.jpg'

# Identificar objetos na imagem
objects = identify_objects(image_path)

# Imprimir os objetos identificados
for obj in objects:
    print(f'Objeto: {obj[0]}, Probabilidade: {obj[1]}%')

#Lembre-se de substituir 'caminho/para/sua/imagem.jpg' pelo caminho real da imagem que você deseja identificar.