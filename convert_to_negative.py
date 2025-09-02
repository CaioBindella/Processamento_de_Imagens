import os
from skimage import io, util

def converter_para_negativo(dir_entrada, dir_saida):
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
                # Lê a imagem em escala de cinza
                img_cinza = io.imread(caminho_entrada)
                
                # Inverte a imagem (cria o negativo) com a função da scikit-image
                img_negativa = util.invert(img_cinza)
                
                # Define o caminho de saída e salva a nova imagem
                caminho_saida = os.path.join(dir_saida, nome_arquivo)
                io.imsave(caminho_saida, img_negativa)
                
                print(f"Negativo da imagem '{nome_arquivo}' salvo em '{dir_saida}'.")
            
            except Exception as e:
                print(f"Erro ao processar o arquivo {nome_arquivo}: {e}")