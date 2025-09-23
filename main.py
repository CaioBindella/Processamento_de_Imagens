from skimage import io
from skimage import data
import matplotlib.pyplot as plt
import os

#Importando a função de conversão
from convert_to_cinza import converter_para_cinza
from convert_to_negative import converter_para_negativo
from histogram import histogram_plot
from equalize_histogram import equalizar_e_analisar_imagem
from plot_images import plot_imagens, plot_all_images
from apply_filters import aplicar_filtros_e_salvar, plotar_comparacao_filtros

# Importando as imagens
img_dir = "assets/rgb"
dir_cinza = "assets/gray"
dir_negativo = "assets/negative"
dir_histogramas = "assets/histograms_gray"
dir_resultados_equalizados = "assets/equalized_histogram"
dir_resultados_filtros = "assets/filtered_results"


if __name__ == "__main__":
    
    # plot_all_images("assets/filtered_results")
    
    # print("\nIniciando análise com filtros de nitidez para a classe 'carro'...")
    
    imagens_carro_para_filtros = [
        "carro_o_d_14.jpg",
        "carro_o_n_14.jpg",
        "carro_i_d_14.jpg",
        "carro_i_n_14.jpg"
    ]

    # # Aplicar os filtros e salvar as imagens resultantes
    # aplicar_filtros_e_salvar(dir_cinza, dir_resultados_filtros, imagens_carro_para_filtros)
    
    # # Plotar as comparações para análise visual
    plotar_comparacao_filtros(dir_cinza, dir_resultados_filtros, imagens_carro_para_filtros)
            
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