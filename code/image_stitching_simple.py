# importação de pacotes necessários

from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

# Construindo o analisador de argumentos e analise dos argumentos

ap = argparse.ArgumentParser()
ap.add_argument("-i", "../image", type=str, required=True,
	help="../image")
ap.add_argument("-o", "../", type=str, required=True,
	help="../")
args = vars(ap.parse_args())

# inicialização lista de imagens
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["../image"])))
image = []

# percorrer os caminhos da imagem, carregar cada uma e adicioná-las
# lista de imagens
