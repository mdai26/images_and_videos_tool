# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:04:47 2023

@author: daimi
"""


import numpy as np
import os
import matplotlib.pyplot as plt


def readfile(filename, eorm, Nx, Ny, Nz):
    indata = np.loadtxt(filename)
    # read eta 
    if eorm == 'e':
        data = np.zeros((Nx, Ny, Nz), dtype = int)
        for i in range(len(indata)):
            # pick the one with largest eta value
            data[int(indata[i,0])-1, int(indata[i,1])-1, int(indata[i,2])-1] = np.argmax(indata[i, 3:6]) + 1
    # read magnetization
    if eorm == 'm':
        data = np.zeros((Nx, Ny, Nz, 3), dtype = float)
        for i in range(len(indata)):
            data[int(indata[i,0])-1, int(indata[i,1])-1, int(indata[i,2])-1,:] = indata[i,3:6]
    return data

def ploteandm(eta, mag, filename, Nx, Ny):
    # plot etaimg
    etaimg = np.zeros((Nx, Ny, 3), dtype = int)
    for i in range(Nx):
        for j in range(Ny):
            # specify the color of eta
            if eta[i, j] == 1:
                etaimg[j, i, :] = [255, 170, 127]
            elif eta[i, j] == 2:
                etaimg[j, i, :] = [170, 170, 255]
            elif eta[i, j] == 3:
                etaimg[j, i, :] = [170, 255, 126]
    fig, ax = plt.subplots(figsize = (10, 10))
    ax.imshow(etaimg, origin = 'lower')
    # plot magnetization 
    grid = 4
    X, Y = np.meshgrid(np.arange(0,Nx,grid), np.arange(0,Ny,grid))
    U, V = mag[::grid,::grid,0], mag[::grid,::grid,1]
    C = mag[::grid,::grid,2]
    qplot = ax.quiver(Y, X, U, V, C, cmap='bwr', scale = 32, width = 0.004)
    qplot.set_clim(-1,1)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    
    
# foldername = '128_16_longer_air_moreoutput'
# start, end, interval = 10000, 300000, 10000
# for i in range(start, end+interval, interval):
#     etafile = os.path.join(foldername,'eta_PT.%d.dat' % i)
#     magfile = os.path.join(foldername,'m.%d.dat' % i)
#     Nx, Ny, Nz = 128, 128, 16
#     eta = readfile(etafile, 'e', Nx, Ny, Nz)
#     eta = eta[4:124, 4:124, :8]
#     mag = readfile(etafile, 'm', Nx, Ny, Nz)
#     mag = mag[4:124, 4:124, :8, :]
#     # get 2D slice
#     eta_2D = eta[:, :, 0].reshape((120, 120))
#     mag_2D = mag[:, :, 0, :].reshape((120, 120, 3))
#     filename = os.path.join(foldername, 'domainstructure_%d.png' % i)
#     ploteandm(eta_2D, mag_2D, filename ,120, 120)

foldername = '128_16_longer_moreoutput'
start, end, interval = 10000, 300000, 10000
for i in range(start, end+interval, interval):
    etafile = os.path.join(foldername,'eta_PT.%d.dat' % i)
    magfile = os.path.join(foldername,'m.%d.dat' % i)
    Nx, Ny, Nz = 128, 128, 16
    eta = readfile(etafile, 'e', Nx, Ny, Nz)
    eta = eta[:,:,:8]
    mag = readfile(etafile, 'm', Nx, Ny, Nz)
    mag = mag[:,:, :8, :]
    # get 2D slice
    eta_2D = eta[:, :, 0].reshape((128, 128))
    mag_2D = mag[:, :, 0, :].reshape((128, 128, 3))
    filename = os.path.join(foldername, 'domainstructure_%d.png' % i)
    ploteandm(eta_2D, mag_2D, filename ,128, 128)


    