# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:56:58 2018

@author: bisheng
"""
from PIL import Image
import matplotlib.pyplot as plt
srcImage=Image.open('lena.jpg')
dstImage=srcImage.copy()
pix=dstImage.load()
width=dstImage.size[0]
height=dstImage.size[1]
for i in range (width):
    for j in range( height):
        r,g,b=pix[i,j]
        pix[i,j]=int(r/2),int(g/2),int(b/2)
plt.figure('lena1')
plt.imshow(srcImage)
plt.axis('off')
plt.show()
plt.figure('lena2')
plt.imshow(dstImage)
plt.axis('off')
plt.show()
dstImage.save('lena1.jpg')
