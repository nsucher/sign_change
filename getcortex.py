from scipy.io import loadmat
from ctmr_gauss_plot import ctmr_gauss_plot

def getcortex(ptdir,hem0):
    pial_mat = '_'+hem0+'h_pial.mat'
    cortex = loadmat(ptdir+pial_mat,struct_as_record=False,squeeze_me=True)
    vert = cortex['cortex'].__dict__['vert'] #TODO: Access tri and vert (matlab: struct --> py: dict)
    tri = cortex['cortex'].__dict__['tri'] #TODO: Access tri and vert (matlab: struct --> py: dict)

    # cortexout=[cortexout cortex];
    return cortex #TODO: define cortex
