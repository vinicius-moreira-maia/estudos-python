import sys
from PIL import Image

images = []

# nomes das imagens passados como argumentos da CLI
for arg in sys.argv[1:]:
    # abrindo cada imagem e adicionando à lista 'images'
    image = Image.open(arg)
    print(type(image))
    images.append(image)

images[0].save(
    "costumes.gif", save_all = True, append_images = [images[1]], duration = 200, loop = 0
)