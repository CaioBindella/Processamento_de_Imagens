from skimage import io
from skimage import data
import matplotlib.pyplot as plt
import os

# Importando as imagens
img_dir = "assets"

# Loop para abrir e mostrar as imagens
def plot_all_images():
    imagens = os.listdir(img_dir)
    for nome in imagens:
        fig, ax = plt.subplots( figsize=(8, 4))
        
        caminho = os.path.join(img_dir, nome)
        # Lê a imagem com skimage
        img = io.imread(caminho)
        
        ax.imshow(img)
        ax.set_title(nome)
        ax.axis("off") # Remove os eixos (números) da imagem
        
        # Plotando o histograma
        fig.tight_layout()
        plt.show()

# Plot de uma imagem
def plot_imagens(name):
    # Criando uma figura com 1 linha e 2 colunas
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Obtendo o caminho da imagem
    caminho = os.path.join(img_dir, name)
    img = io.imread(caminho)
    
    # Plotando a imagem
    ax.imshow(img)
    ax.set_title(name)
    ax.axis("off") # Remove os eixos (números) da imagem
    
    # Plotando o histograma
    fig.tight_layout()
    plt.show()

# Chamndo a função para plotar apenas uma imagem
# plot_imagens("carro_o_n_14.jpg")

# Chamndo a função para plotar todas as imagens
plot_all_images()