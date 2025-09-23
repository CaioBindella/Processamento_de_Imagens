import os
from skimage import io, img_as_float
from skimage.filters import unsharp_mask
import matplotlib.pyplot as plt
import numpy as np

def aplicar_filtros_e_salvar(dir_entrada, dir_saida, imagens_classe):
    """
    Aplica os filtros Máscara de Nitidez e High-Boost em uma lista de imagens
    e salva os resultados.
    """
    if not os.path.exists(dir_saida):
        os.makedirs(dir_saida)
        print(f"Diretório '{dir_saida}' criado com sucesso.")

    for nome_arquivo in imagens_classe:
        caminho_entrada = os.path.join(dir_entrada, nome_arquivo)

        if os.path.isfile(caminho_entrada):
            try:
                img_original = io.imread(caminho_entrada, as_gray=True)
                img_float = img_as_float(img_original)

                # Aplicar Máscara de Nitidez (Unsharp Masking)
                img_unsharp = unsharp_mask(img_float, radius=2, amount=1.0)

                # Aplicar High-Boost Filter
                img_high_boost = unsharp_mask(img_float, radius=2, amount=4.0)

                nome_base = os.path.splitext(nome_arquivo)[0]
                caminho_saida_unsharp = os.path.join(dir_saida, f"{nome_base}_unsharp.jpg")
                caminho_saida_highboost = os.path.join(dir_saida, f"{nome_base}_highboost.jpg")

                io.imsave(caminho_saida_unsharp, (np.clip(img_unsharp, 0, 1) * 255).astype(np.uint8))
                io.imsave(caminho_saida_highboost, (np.clip(img_high_boost, 0, 1) * 255).astype(np.uint8))

                print(f"Filtros aplicados e imagens salvas para '{nome_arquivo}'.")

            except Exception as e:
                print(f"Erro ao processar o arquivo {nome_arquivo}: {e}")

def plotar_comparacao_filtros(dir_entrada, dir_saida, imagens_classe):
    """
    Plota uma comparação das imagens original, com máscara de nitidez e com high-boost.
    """
    for nome_arquivo in imagens_classe:
        nome_base = os.path.splitext(nome_arquivo)[0]
        
        caminho_original = os.path.join(dir_entrada, nome_arquivo)
        caminho_unsharp = os.path.join(dir_saida, f"{nome_base}_unsharp.jpg")
        caminho_highboost = os.path.join(dir_saida, f"{nome_base}_highboost.jpg")

        if all(os.path.exists(p) for p in [caminho_original, caminho_unsharp, caminho_highboost]):
            img_original = io.imread(caminho_original)
            img_unsharp = io.imread(caminho_unsharp)
            img_highboost = io.imread(caminho_highboost)

            fig, axes = plt.subplots(1, 3, figsize=(18, 6))
            ax = axes.ravel()

            ax[0].imshow(img_original, cmap='gray')
            ax[0].set_title('Imagem Original')
            ax[0].axis('off')

            ax[1].imshow(img_unsharp, cmap='gray')
            ax[1].set_title('Máscara de Nitidez')
            ax[1].axis('off')

            ax[2].imshow(img_highboost, cmap='gray')
            ax[2].set_title('High-Boost Filter')
            ax[2].axis('off')

            fig.suptitle(f'Comparação de Filtros para: {nome_arquivo}', fontsize=16)
            plt.tight_layout()
            plt.show()