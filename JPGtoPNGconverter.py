import os
import sys
from pathlib import Path

from PIL import Image


def jpg_to_png(jpg, png):
    for img in os.listdir(f'.{jpg}'):
        name = Path(f'{img}').stem
        img_obj = Image.open(f'.{jpg}\\{img}')
        img_obj.save(f'.{png}\\{name}.png', 'png')


input_folder = sys.argv[1]
output_folder = sys.argv[2]

try:
    os.mkdir(f'.{output_folder}')
except FileExistsError:
    print('Directory Already Exists')
    pass

jpg_to_png(input_folder, output_folder)
