import os
import numpy as np
from skimage import io
from scipy.ndimage import convolve
import matplotlib.pyplot as plt

def aplicar_filtro_espacial(dir_entrada, dir_saida, nome_arquivo, kernel, nome_filtro):
    """
    Aplica um filtro espacial (kernel de convolução) 3x3 a uma imagem.
    """
    if not os.path.exists(dir_saida):
        os.makedirs(dir_saida)

    caminho_entrada = os.path.join(dir_entrada, nome_arquivo)

    if os.path.isfile(caminho_entrada):
        try:
            img_original = io.imread(caminho_entrada, as_gray=True)
            img_filtrada = convolve(img_original, kernel, mode='reflect')
            img_filtrada = np.clip(img_filtrada, 0, 255)
            img_filtrada_8bit = img_filtrada.astype(np.uint8)

            nome_base = os.path.splitext(nome_arquivo)[0]
            caminho_saida = os.path.join(dir_saida, f"{nome_base}_{nome_filtro}.jpg")
            io.imsave(caminho_saida, img_filtrada_8bit)

            print(f"Filtro '{nome_filtro}' aplicado em '{nome_arquivo}'.")
            # Garanta que esta linha retorne a string com o caminho do arquivo
            return caminho_saida

        except Exception as e:
            print(f"Erro ao aplicar filtro em '{nome_arquivo}': {e}")
            return None
        else: 
            print(f"AVISO: Arquivo não encontrado no caminho: '{caminho_entrada}'")
            return None

def plotar_comparacao_espacial(caminho_original, caminhos_filtrados, nomes_filtros):
    """
    Plota a imagem original ao lado de suas versões filtradas.
    """
    num_filtros = len(caminhos_filtrados)
    img_original = io.imread(caminho_original)

    fig, axes = plt.subplots(1, num_filtros + 1, figsize=(6 * (num_filtros + 1), 6))
    
    axes[0].imshow(img_original, cmap='gray')
    axes[0].set_title('Imagem Original')
    axes[0].axis('off')

    for i, caminho in enumerate(caminhos_filtrados):
        img_filtrada = io.imread(caminho)
        axes[i+1].imshow(img_filtrada, cmap='gray')
        axes[i+1].set_title(f'Filtro: {nomes_filtros[i]}')
        axes[i+1].axis('off')

    plt.tight_layout()
    plt.show()