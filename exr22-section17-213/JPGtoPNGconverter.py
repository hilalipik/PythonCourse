#         <script location>                     <source directory>         <destination directory>
# exr22-section17-213/JPGtoPNGconverter.py exr22-section17-213/animals/ exr22-section17-213/new_folder/
# example ^^

from PIL import Image, ImageFilter
import sys
import os

if len(sys.argv) != 3:
    print("Must enter 2 parameters.")
    exit()

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

if not (os.path.exists(source_dir)):
    print("The source path '" + source_dir + "' does not exist.")
    exit()

if not (os.path.exists(dest_dir)):
    os.makedirs(dest_dir)

for name in os.listdir(source_dir):
    if name.endswith('jpg'):
        img = Image.open(f'{source_dir}{name}')
        name = name[:name.find('jpg')]
        img.save(f'{dest_dir}{name}png', 'png')
