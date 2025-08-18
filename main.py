from skimage import io
import matplotlib.pyplot as plt
import os

# Importando as imagens
img_dir = "assets"

imagens = os.listdir(img_dir)

# Loop para abrir e mostrar as imagens
for nome in imagens:
    caminho = os.path.join(img_dir, nome)
    
    # Lê a imagem com skimage
    img = io.imread(caminho)
    
    # Plota
    plt.figure(figsize=(5, 5))
    plt.imshow(img)
    plt.title(nome)
    plt.axis("off")
    plt.show()
    
# Plot de imagem específica
# img = io.imread(os.path.join(img_dir, "chave_o_d_14.jpg"))
# plt.imshow(img)
# plt.axis("off")
# plt.show()