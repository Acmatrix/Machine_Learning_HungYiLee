# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:54:44 2018

@author: bisheng
"""

from PIL import Image
srcImage=Image.open('lena.jpg')
dstImage=srcImage.rotate(180)
dstImage.save('lena2.jpg')