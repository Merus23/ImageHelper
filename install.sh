#!/bin/bash

# Instalação das bibliotecas Python usando pip
pip install numpy
pip install Pillow
pip install tensorflow
pip install opencv-python
pip install opencv-python-headless

# Verifica se a instalação foi bem-sucedida
if [ $? -eq 0 ]; then
    echo "Bibliotecas Python instaladas com sucesso."
else
    echo "Ocorreu um erro durante a instalação das bibliotecas Python."
fi
