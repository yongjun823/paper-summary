import os
import sys

dir_name = sys.argv[1]

img_dir_path = os.path.join(dir_name, 'images')
image_arr = os.listdir(img_dir_path)

image_arr = sorted(image_arr, key=lambda x: int(x.split('.')[0][4:]))

with open(f'{dir_name}/README.md', 'w', encoding='utf-8') as f:
    f.write('## ' + dir_name + '\n\n\n')
    
    for img in image_arr:
        f.write(f'![ww](./images/{img})  \n')

template = """* [{title} Summary](https://github.com/yongjun823/paper-summary/tree/master/{title})  
[paper_title](paper_url) (author)  \n"""

with open('README.md', 'a') as f:
    f.writelines(template.format(title=dir_name))
