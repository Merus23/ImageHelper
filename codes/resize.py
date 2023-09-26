import os
import cv2

class Resize:
    def __init__(self):
        pass

    def inputs(self):
        self.porcentagem = int(input("\nInforme a porcentagem de redimensionamento: \n"))
        self.source = input("\nInforme o diretório das imagens: \n")
        self.destination = input("\nInforme o diretório de destino das imagens: \n")

    def ler_imagens(self):
        self.imagens = []
        for arquivo in os.listdir(self.source):
            if arquivo.lower().endswith(('.tif', '.jpg', '.jpeg', '.png', '.gif')):
                caminho_arquivo = os.path.join(self.source, arquivo)
                self.imagens.append(caminho_arquivo)

    def redimensionar_imagens(self):
        for imagem_path in self.imagens:
            imagem = cv2.imread(imagem_path, cv2.IMREAD_UNCHANGED)

            width = int(imagem.shape[1] * self.porcentagem / 100)
            height = int(imagem.shape[0] * self.porcentagem / 100)
            dim = (width, height)

            imagem_redimensionada = cv2.resize(imagem, dim)

            # Extrair o nome do arquivo sem a extensão
            nome_arquivo, extensao = os.path.splitext(os.path.basename(imagem_path))

            # Criar o caminho completo de destino com nome de arquivo único
            destino_completo = os.path.join(self.destination, f"{nome_arquivo}_redimensionada{extensao}")

            cv2.imwrite(destino_completo, imagem_redimensionada)

            print(f"Imagem {nome_arquivo} redimensionada com sucesso!")


