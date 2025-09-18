import os
import matplotlib.pyplot as plt
from skimage import io, exposure
import numpy as np

def equalizar_e_analisar_imagem(caminho_imagem, dir_saida):
    # Garante que o diretório de saída exista
    if not os.path.exists(dir_saida):
        os.makedirs(dir_saida)
        print(f"Diretório '{dir_saida}' criado.")

    try:
        # Carrega a imagem em escala de cinza
        img_cinza = io.imread(caminho_imagem, as_gray=True)
        # Converte para o formato de 8 bits para garantir consistência
        img_cinza_8bit = (img_cinza * 255).astype(np.uint8)

        # Aplica a equalização de histograma
        img_equalizada = exposure.equalize_hist(img_cinza_8bit)

        # Cria uma figura para exibir a análise completa
        fig, axes = plt.subplots(2, 2, figsize=(14, 12))
        nome_base = os.path.splitext(os.path.basename(caminho_imagem))[0]
        fig.suptitle(f'Análise de Histograma - {nome_base}.jpg', fontsize=16)

        # Imagem Original e seu Histograma
        axes[0, 0].imshow(img_cinza_8bit, cmap='gray')
        axes[0, 0].set_title('Imagem Original')
        axes[0, 0].axis('off')

        axes[0, 1].hist(img_cinza_8bit.ravel(), bins=256, range=[0, 256], color='blue')
        axes[0, 1].set_title('Histograma Original')
        axes[0, 1].set_xlabel('Intensidade de Pixel')
        axes[0, 1].set_ylabel('Quantidade de Pixels')

        # Imagem Equalizada e seu Histograma
        axes[1, 0].imshow(img_equalizada, cmap='gray')
        axes[1, 0].set_title('Imagem Equalizada')
        axes[1, 0].axis('off')

        axes[1, 1].hist(img_equalizada.ravel(), bins=256, range=[0, 1], color='green')
        axes[1, 1].set_title('Histograma Equalizado')
        axes[1, 1].set_xlabel('Intensidade de Pixel (normalizada)')
        axes[1, 1].set_ylabel('Quantidade de Pixels')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])

        # Salva a figura de análise
        caminho_saida_analise = os.path.join(dir_saida, f"analise_{nome_base}.png")
        plt.savefig(caminho_saida_analise)
        plt.close(fig)

        print(f"Análise de '{nome_base}.jpg' salva em '{caminho_saida_analise}'.")

    except Exception as e:
        print(f"Erro ao processar o arquivo {caminho_imagem}: {e}")