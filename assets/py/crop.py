"""Parte una imagen en DIVS imagenes, despues elimina la imagen"""

from PIL import Image,ImageChops
import os

DIVS = 5

files = os.listdir()
files.remove(__file__)
for f in files:
    im = Image.open(f)
    basename,ext = f.split('.')
    width, height = im.size
    regionH = height/DIVS
    crop = 0
    for i in range(DIVS):
        region = im.crop( ( 0, crop, width, crop+regionH ))
        region.save(basename+'_{}.'.format(i)+ext)
        crop += regionH

for f in files: os.remove(f)