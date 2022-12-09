import numpy as np


def ctmr_gauss_plot(cortex,elecmatrix,weights,hemi='diag',do_lighting=1,cax=0,addl=0,CM='cmSz3D',gsp=10):

# MATLAB:
# Copyright (C) 2009  K.J. Miller & D. Hermes, Dept of Neurology and Neurosurgery, University Medical Center Utrecht
# Version 1.1.0, released 26-11-2009
# Edited 2016 by Liberty Hamilton
# Edited 2017-21 by Jon Kleen

# PYTHON:
# Created 2022 by N.S. Munizaga

    if np.empty(elecmatrix):
        elecmatrix = [0,0,0]
    if np.empty(weights):
        weights = np.zeros(np.shape(elecmatrix)[0])

    if CM != 'cmSz3D':
        cm = CM

    # cortex = cortex['cortex']

    # vert = cortex.select_dtypes(include='vert',exclude='tri')
    # tri = cortex.select_dtypes(include='tri',exclude='vert')

    # print('keys: ')
    # print(cortex.keys())
    #
    # print('values: ')
    # print(cortex.values())
    #
    # print('items: ')
    # print(cortex.items())
    # for item in cortex:
    #     print(item)
    # print(cortex['vert'])
    # brain = cortex['vert']
