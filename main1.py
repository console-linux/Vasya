import os

# Список директорий, из которых мы собираемся извлекать контент
directories = ['data/животные', 'data/растения', 'data/смешарики']
output_html_file = 'index.html'

def generate_html(directories):
    with open(output_html_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="en">\n')
        f.write('<head>\n')
        f.write('   <meta charset="utf-8">\n')
        f.write('   <title>Васины Работы</title>\n')
        f.write('   <style>\n')
        f.write('       body {font-family: Arial, Helvetica, sans-serif;}\n')
        f.write('       nav ul {list-style-type: none; background-color: #f1f1f1; overflow: hidden;}\n')
        f.write('       nav li {float: left;}\n')
        f.write('       nav a {display: inline-block; color: black; text-decoration: none; padding: 14px 16px; transition-duration: 0.3s;}\n')
        f.write('       nav a:hover {background-color: #ddd;}\n')
        f.write('       section {margin-bottom: 50px;}\n')
        f.write('       .image-container img {width: auto; height: 500px; object-fit: contain; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,.1); display: block; margin-left: auto; margin-right: auto;}\n')
        f.write('       .image-container h3 {text-align: center; color: #333; padding-top: 10px;}\n')
        f.write('   </style>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        
        # Навигационная панель
        f.write('<nav>\n')
        f.write('   <ul>\n')
        for directory in directories:
            dir_name = os.path.basename(directory)
            id_attr = dir_name.replace(" ", "-").lower()
            f.write(f'      <li><a href="#{id_attr}">{dir_name.capitalize()}</a></li>\n')
        f.write('   </ul>\n')
        f.write('</nav>\n')
        
        # Теперь создаём сами секции
        for directory in directories:
            dir_name = os.path.basename(directory)
            id_attr = dir_name.replace(" ", "-").lower()
            
            # Начинаем новую секцию
            f.write(f'<section id="{id_attr}">\n')
            f.write(f'   <h2>{dir_name.capitalize()}</h2>\n')
            
            # Собираем изображения из директории
            images = []
            for root, _, files in os.walk(directory):
                for file in files:
                    fullpath = os.path.join(root, file)
                    rel_path = os.path.relpath(fullpath, directory)
                    images.append(rel_path)
            
            # Формируем блоки с изображениями
            for image in sorted(images):
                f.write(f'   <div class="image-container">\n')
                f.write(f'       <img src="{os.path.join(directory, image)}" alt="{image}"/>\n')
                f.write(f'       <h3>{image}</h3>\n')
                f.write(f'   </div>\n')
            
            # Завершаем секцию
            f.write('</section>\n')
    
        f.write('</body>\n')
        f.write('</html>')

if __name__ == "__main__":
    generate_html(directories)
