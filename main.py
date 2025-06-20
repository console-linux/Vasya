import os

# Директория, которую хотим просмотреть
folder_path = 'data'
output_html_file = 'index.html'

def generate_html(folder):
    images = []
    # Рекурсивно ищем все изображения в данной папке и подпапках
    for root, dirs, files in os.walk(folder):
        for filename in files:
            fullpath = os.path.join(root, filename)
            relative_path = os.path.relpath(fullpath, folder)
            images.append(relative_path)

    with open(output_html_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="en">\n')
        f.write('<head>\n')
        f.write('   <meta charset="utf-8">\n')
        f.write('   <title>Васины Работы</title>\n')
        f.write('   <style>\n')
        f.write('       body {\n')
        f.write('           font-family: Arial, Helvetica, sans-serif;\n')
        f.write('       }\n')
        f.write('       .image-container img {\n')
        f.write('           width: auto;\n')
        f.write('           height: 500px;\n')
        f.write('           object-fit: contain;\n')
        f.write('           border-radius: 5px;\n')
        f.write('           box-shadow: 0 0 10px rgba(0,0,0,.1);\n')
        f.write('           display: block;\n')
        f.write('           margin-left: auto;\n')
        f.write('           margin-right: auto;\n')
        f.write('       }\n')
        f.write('       .image-container h3 {\n')
        f.write('           text-align: center;\n')
        f.write('           color: #333;\n')
        f.write('           padding-top: 10px;\n')
        f.write('       }\n')
        f.write('   </style>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write(f'<h1>Васькины Поделки</h1>\n')
        for image in sorted(images):  # Сортируем изображения по имени файла
            f.write(f'   <div class="image-container">\n')
            f.write(f'       <img src="{os.path.join(folder, image)}" alt="{image}"/>\n')
            f.write(f'       <h3>{image}</h3>\n')
            f.write(f'   </div>\n')
        f.write('</body>\n')
        f.write('</html>')

if __name__ == "__main__":
    generate_html(folder_path)
