#3rd party modules

import csv
import os
import pathlib
import xlsxwriter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.io import loadmat
from scipy.signal import butter,filtfilt
from scipy.stats import ttest_1samp

#created for the script
from getbrain4 import getbrain4
from ctmr_gauss_plot import ctmr_gauss_plot


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Main = sign_change')

    cortexout,hem = getbrain4('EC91',1,1,'lr')


