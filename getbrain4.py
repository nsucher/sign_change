import matplotlib.pyplot as plt

from getcortex import getcortex
from ctmr_gauss_plot import ctmr_gauss_plot
from litebrain import litebrain

def getbrain4(pt, plotbrain, newfig, hem):
    mainpath = '/Users/nataliasucher/Desktop/UCSF/Coding/OPSCEA/'
    # if any(strcmp(hem,{'b','lr'})); bilat=1; else; bilat=0; end
    if hem == 'b' or 'lr':
        bilat = 1
    else:
        bilat = 0

    if pt == 'mni':
        pt = 'cvs_avg35_inMNI152'

    ptdir = mainpath + 'OPSCEADATA/' + pt + '/Imaging/Meshes/' + pt
    cortexout = []
    if plotbrain:
        if newfig:
            fig = plt.figure()
            if bilat:
                # plt.hold(True)
                if bilat or hem[0] == 'l':
                    # establish path
                    cortex = getcortex(ptdir, hem[0])
                    ctmr_gauss_plot(cortex, [], [], 'lh') #TODO: need to bypass matlab's version nargins
                    cortexout = [cortexout,cortex]
                if bilat or hem[0] == 'r':
                    cortex = getcortex(ptdir, hem[0])
                    ctmr_gauss_plot(cortex, [], [], 'rh') #TODO: need to bypass matlab's version nargins
                    cortexout = [cortexout,cortex]
                litebrain('a',.25)



    # return cortexout, hem
    return cortexout, hem