import os
import re
import imageio.v2 as imageio

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def create_gif(image_folder, gif_filename, duration):
    images = []
    filenames = sorted([filename for filename in os.listdir(image_folder) if filename.endswith(".png")], key=natural_sort_key)

    for filename in filenames:
        file_path = os.path.join(image_folder, filename)
        images.append(imageio.imread(file_path))

    gif_path = os.path.join(image_folder, gif_filename)
    imageio.mimsave(gif_path, images, duration=duration)

def main():
    image_folder = input("Digite o nome da pasta onde estão as imagens (sem barras): ")
    gif_filename = input("Digite o nome do arquivo GIF (com a extensão .gif): ")
    duration = float(input("Digite a duração do GIF em segundos: "))

    create_gif(image_folder, gif_filename, duration)

if __name__ == "__main__":
    main()
