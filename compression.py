#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
from PIL import Image

quality = 85
raw_root = '.'
export_root = '.'

for root, dirs, files in os.walk(raw_root):
    for bmpfig in files:
        if not bmpfig.endswith('.bmp') and not bmpfig.endswith('.png'):
            continue
        raw_path = os.path.join(root, bmpfig)
        export_name = bmpfig[:-4] + ".jpg"
        img = Image.open(raw_path)
        img = img.convert('RGB')
        export_path = os.path.join(export_root, export_name)
        img.save(export_path, format='jpeg', quality=quality)
        print("converting from", raw_path, "to", export_path)
        img.close()
        os.remove(raw_path)


