import os
import numpy as np
from skimage import io
from skimage.util import img_as_float
import matplotlib.pyplot as plt

def aplicar_transformacao_logaritmica(dir_entrada, dir_saida, imagens_classe):
    """
    Aplica a transformação de intensidade logarítmica em uma lista de imagens.
    Esta transformação realça detalhes nas áreas mais escuras da imagem.
    A fórmula é s = c * log(1 + r), onde 'c' é uma constante.
    """
    if not os.path.exists(dir_saida):
        os.makedirs(dir_saida)
        print(f"Diretório '{dir_saida}' criado com sucesso.")

    for nome_arquivo in imagens_classe:
        caminho_entrada = os.path.join(dir_entrada, nome_arquivo)

        if os.path.isfile(caminho_entrada):
            try:
                # Carrega a imagem e converte para float para preservar a precisão
                img = img_as_float(io.imread(caminho_entrada, as_gray=True))

                # Calcula a constante 'c'. O valor máximo de 'r' em float é 1.
                c = 255 / np.log(1 + np.max(img))

                # Aplica a transformação logarítmica
                img_log = c * (np.log(img + 1))

                # Converte a imagem de volta para 8-bit (0-255)
                img_log_8bit = img_log.astype(np.uint8)

                # Salva a imagem resultante
                nome_base = os.path.splitext(nome_arquivo)[0]
                caminho_saida = os.path.join(dir_saida, f"{nome_base}_log.jpg")
                io.imsave(caminho_saida, img_log_8bit)

                print(f"Transformação logarítmica aplicada em '{nome_arquivo}'.")

            except Exception as e:
                print(f"Erro ao processar '{nome_arquivo}': {e}")


def plotar_comparacao_log(dir_entrada, dir_saida, nome_arquivo):
    """
    Plota a imagem original e sua versão com transformação logarítmica lado a lado.
    """
    nome_base = os.path.splitext(nome_arquivo)[0]
    caminho_original = os.path.join(dir_entrada, nome_arquivo)
    caminho_log = os.path.join(dir_saida, f"{nome_base}_log.jpg")

    if os.path.exists(caminho_original) and os.path.exists(caminho_log):
        img_original = io.imread(caminho_original)
        img_log = io.imread(caminho_log)

        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        ax = axes.ravel()

        ax[0].imshow(img_original, cmap='gray')
        ax[0].set_title('Imagem Original')
        ax[0].axis('off')

        ax[1].imshow(img_log, cmap='gray')
        ax[1].set_title('Transformação Logarítmica')
        ax[1].axis('off')

        fig.suptitle(f'Comparação para: {nome_arquivo}', fontsize=16)
        plt.tight_layout()
        plt.show()