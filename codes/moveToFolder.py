import shutil
import os

class moveToFolder:
    def __init__(self):
        pass

    def inputs(self):
        self.source = input('\nInforme a pasta fonte: \n')
        self.destination = input('\nInforme a pasta destino: \n')
        self.fileExtension = input('\nInforme a extensão dos arquivos (.jpeg ou jpeg): \n')
        self.itensAmount = int(input('\nInforme a quantidade de arquivos: \n'))

    def moveFiles(self):
        if not self.source.endswith('/'):
            self.source = self.source + '/'

        files = os.listdir(self.source)
        count = 0
        for file in files:
            if file.endswith(self.fileExtension):
                shutil.move(self.source + file, self.destination)
                print('O arquivo '+file+' foi movido com sucesso!')
                count += 1
                if count == self.itensAmount:
                    break