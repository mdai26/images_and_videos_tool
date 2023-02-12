# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:07:48 2023

@author: daimi
"""

import imageio
import os

start, end, interval = 10000, 300000, 10000
foldername = '128_16_longer_air_moreoutput'

with imageio.get_writer('membrane.gif', mode = 'I') as writer:
    for i in range(start, end+interval, interval):
        filename = os.path.join(foldername, 'domainstructure_%d.png' % i)
        image = imageio.imread(filename)
        writer.append_data(image)