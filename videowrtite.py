# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 16:59:16 2023

@author: daimi
"""

import cv2
import os

img_array = []

start, end, interval = 10000, 300000, 10000
foldername = '128_16_longer_moreoutput'

for i in range(start, end+interval, interval):
    filename = os.path.join(foldername, 'domainstructure_%d.png' % i)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    
out = cv2.VideoWriter('thinfilm.mp4', cv2.VideoWriter_fourcc(*'MP4V'),2,size)

for i in range(len(img_array)):
    out.write(img_array[i])

out.release()