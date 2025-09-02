import os
from skimage import io, data, img_as_float, exposure
import matplotlib.pyplot as plt

def histogram_plot(dir_entrada, dir_saida):
    # Verifica se o diretório de saída existe; se não, cria.
    if not os.path.exists(dir_saida):
        os.makedirs(dir_saida)
        print(f"Diretório '{dir_saida}' criado com sucesso.")
    
    for nome_arquivo in os.listdir(dir_entrada):
        caminho_entrada = os.path.join(dir_entrada, nome_arquivo)
        
        # Garante que estamos processando apenas arquivos
        if os.path.isfile(caminho_entrada):
            try:
                # Lê a imagem em escala de cinza
                img_cinza = io.imread(caminho_entrada, as_gray=True)
                
                # Calculo o histograma
                fig, ax = plt.subplots(figsize=(8, 6))
                
                # img.ravel() transforma a matriz 2D da imagem em um array 1D
                # bins=256 cria uma "caixa" para cada intensidade de cinza (0 a 255)
                # range=[0, 256] define o intervalo do eixo X
                ax.hist(img_cinza.ravel(), bins=256, range=[0, 256])
                
                # Adiciona títulos e rótulos para clareza
                ax.set_title(f'Histograma - {nome_arquivo}')
                ax.set_xlabel('Intensidade de Pixel')
                ax.set_ylabel('Quantidade de Pixels')
                
                # Define um nome de arquivo de saída para o gráfico
                nome_base = os.path.splitext(nome_arquivo)[0]
                nome_saida = f"histograma_{nome_base}.png"
                caminho_saida = os.path.join(dir_saida, nome_saida)
                
                # Salva a figura do gráfico no caminho de saída
                plt.savefig(caminho_saida)
                
                # Fecha a figura para liberar a memória. MUITO IMPORTANTE!
                plt.close(fig)
                
                print(f"Histograma de '{nome_arquivo}' salvo como '{nome_saida}'.")
            
            except Exception as e:
                print(f"Erro ao processar o arquivo {nome_arquivo}: {e}")