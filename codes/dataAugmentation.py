import os
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2 as cv

class dataAugmentation:
    def __init__(self):
        pass

    def inputs(self):
        self.source = input("\nInforme o diretório das imagens: \n")
        self.destination = input("\nInforme o diretório de destino das imagens: \n")
        self.genetationNumber = int(input("\nInforme o número de imagens que deseja gerar baseado em uma única imagem: \n"))

    def execute(self):
        datagen = ImageDataGenerator(
            rotation_range=90,
            brightness_range=[0.1,0.7],
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            horizontal_flip=True, 
            vertical_flip=True,
            fill_mode='reflect'
        )
        # Loop sobre todas as imagens no diretório de entrada
        for filename in os.listdir(self.source):
            # Verifica se o arquivo é uma imagem
            if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                img = Image.open(os.path.join(self.source, filename))
                img_array = np.array(img)
                img_array = img_array.reshape((1,) + img_array.shape)
            
                i = 0
                for batch in datagen.flow(img_array, batch_size=1, save_to_dir=self.destination, save_prefix=filename[:-4], save_format='jpg'):
                    i += 1
                    print(f'Imagem {filename} gerada com sucesso!')
                    if i > self.genetationNumber:
                        break
    
