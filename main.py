from skimage import io
from skimage import data
import matplotlib.pyplot as plt
import os
import numpy as np

#Importando a função de conversão
from convert_to_cinza import converter_para_cinza
from convert_to_negative import converter_para_negativo
from histogram import histogram_plot
from equalize_histogram import equalizar_e_analisar_imagem
from plot_images import plot_imagens, plot_all_images
from apply_filters import aplicar_filtros_e_salvar, plotar_comparacao_filtros
from intensity_transformations import aplicar_transformacao_logaritmica, plotar_comparacao_log
from spatial_filtering import aplicar_filtro_espacial, plotar_comparacao_espacial

# Importando as imagens
img_dir = "assets/rgb"
dir_cinza = "assets/gray"
dir_negativo = "assets/negative"
dir_histogramas = "assets/histograms_gray"
dir_resultados_equalizados = "assets/equalized_histogram"
dir_resultados_filtros = "assets/filtered_results"
dir_logaritmico = "assets/log_transformed"
dir_espacial = "assets/spatial_filtered"


if __name__ == "__main__":
    
    # plot_all_images("assets/log_transformed")
    
    # print("\nIniciando análise com filtros de nitidez para a classe 'carro'...")
    
    # imagens_carro_para_filtros = [
    #     "carro_o_d_14.jpg",
    #     "carro_o_n_14.jpg",
    #     "carro_i_d_14.jpg",
    #     "carro_i_n_14.jpg"
    # ]

    # # Aplicar os filtros e salvar as imagens resultantes
    # aplicar_filtros_e_salvar(dir_cinza, dir_resultados_filtros, imagens_carro_para_filtros)
    
    # # Plotar as comparações para análise visual
    # plotar_comparacao_filtros(dir_cinza, dir_resultados_filtros, imagens_carro_para_filtros)
            
    # print("\nAnálise com filtros de nitidez concluída.")
    
    # converter_para_cinza(img_dir, dir_cinza)
    # converter_para_negativo(dir_cinza, dir_negativo)
    # gerar histogramas
    # histogram_plot(dir_cinza, "assets/histograms_gray")
      
    # print("\nExibindo uma imagem original como exemplo:")
    # plot_imagens("carro_o_n_14.jpg")
    
    
    # print("\nIniciando análise com equalização de histograma para a classe 'carro'...")
    
    # imagens_carro = [
    #     "carro_o_d_14.jpg",
    #     "carro_o_n_14.jpg",
    #     "carro_i_d_14.jpg",
    #     "carro_i_n_14.jpg"
    # ]

    # for nome_imagem in imagens_carro:
    #     caminho_completo = os.path.join(dir_cinza, nome_imagem)
    #     if os.path.exists(caminho_completo):
    #         # Chama a nova função do arquivo separado
    #         equalizar_e_analisar_imagem(caminho_completo, dir_resultados_equalizados)
    #     else:
    #         print(f"Arquivo não encontrado: {caminho_completo}")
            
    # print("\nAnálise concluída.")
    
    # --- Execução da Transformação de Intensidade Logarítmica ---
    # print("\nIniciando transformação logarítmica em imagens escuras...")

    # # Imagens escuras são ideais para esta transformação
    # imagens_para_log = [
    #     "carro_o_n_14.jpg",
    #     "carro_i_n_14.jpg",
    #     "carro_o_d_14.jpg",
    #     "carro_i_d_14.jpg", 
    # ]

    # # 1. Aplicar a transformação e salvar as imagens
    # aplicar_transformacao_logaritmica(dir_cinza, dir_logaritmico, imagens_para_log)

    # # 2. Plotar as comparações para análise
    # for imagem in imagens_para_log:
    #     plotar_comparacao_log(dir_cinza, dir_logaritmico, imagem)
        
    # print("\nAnálise com transformação logarítmica concluída.")
    
    # Imagem de exemplo para aplicar os filtros
    imagem_teste = "moon.TIF"
    caminho_original = os.path.join(dir_cinza, imagem_teste)

    # --- Definição das Máscaras (Kernels) 3x3 ---

    #  Filtro de Média (Blur/Suavização)
    # Soma de todos os coeficientes é 1 (1/9 * 9) para não alterar o brilho.
    kernel_blur = (1/9) * np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])

    #  Filtro de Nitidez (Sharpen)
    # Realça as diferenças entre os pixels.
    kernel_sharpen = np.array([
        [ 0, -1,  0],
        [-1,  5, -1],
        [ 0, -1,  0]
    ])
  
    #  Filtro de Detecção de Bordas (Laplaciano)
    kernel_laplacian = np.array([
        [ 0,  1,  0],
        [ 1, -4,  1],
        [ 0,  1,  0]
    ])

    # Lista de filtros para aplicar
    filtros = {
        "blur": kernel_blur,
        "sharpen": kernel_sharpen,
        "laplacian": kernel_laplacian
    }

    caminhos_resultados = []
    nomes_resultados = []

    for nome, kernel in filtros.items():
        caminho_resultado = aplicar_filtro_espacial(
            dir_cinza, dir_espacial, imagem_teste, kernel, nome
        )
        if caminho_resultado:
            caminhos_resultados.append(caminho_resultado)
            nomes_resultados.append(nome.capitalize())

    # Plotar a comparação dos resultados
    if caminhos_resultados:
        plotar_comparacao_espacial(caminho_original, caminhos_resultados, nomes_resultados)
