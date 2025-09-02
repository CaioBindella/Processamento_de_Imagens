import os
from skimage import io, color, util

def converter_para_cinza(dir_entrada, dir_saida):
    # Verifica se o diretório de saída existe; se não, cria.
    if not os.path.exists(dir_saida):
        os.makedirs(dir_saida)
        print(f"Diretório '{dir_saida}' criado com sucesso.")

    # Lista todos os arquivos no diretório de entrada
    for nome_arquivo in os.listdir(dir_entrada):
        caminho_entrada = os.path.join(dir_entrada, nome_arquivo)
        
        # Garante que estamos processando apenas arquivos
        if os.path.isfile(caminho_entrada):
            try:
                # Lê a imagem colorida
                img_colorida = io.imread(caminho_entrada)
                
                # Converte a imagem para escala de cinza
                img_cinza = color.rgb2gray(img_colorida)
                
                # Converte a imagem para o formato uint8 (ideal para salvar)
                img_cinza_8bit = util.img_as_ubyte(img_cinza)
                
                # Define o caminho de saída e salva a nova imagem
                caminho_saida = os.path.join(dir_saida, nome_arquivo)
                io.imsave(caminho_saida, img_cinza_8bit)
                
                print(f"Imagem '{nome_arquivo}' convertida e salva em '{dir_saida}'.")
            
            except Exception as e:
                print(f"Erro ao processar o arquivo {nome_arquivo}: {e}")