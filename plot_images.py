from skimage import io
import matplotlib.pyplot as plt
import os

# Importando as imagens
dir_rgb = "assets/rgb"
dir_cinza = "assets/gray"
dir_negativo = "assets/negative"
dir_histogramas = "assets/histograms_gray"
dir_resultados_equalizados = "assets/equalized_histogram"

# Loop para abrir e mostrar as imagens
def plot_all_images(img_dir):
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
def plot_imagens(img_dir, name):
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