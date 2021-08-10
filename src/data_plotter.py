###
# define here functions to plot data
###

import matplotlib.pyplot as plt
import numpy as np

def plot_xy(x,y):
    """simple plot x and y

    Args:
        x ([type]): [description]
        y ([type]): [description]
    """
    fig=plt.figure()
    ax1=plt.subplot(111)
    
    ax1.plot(x,y)
    plt.show()

def plot_complex(x,re,im,log=False):
    """Plot a complex series of complex data .

    Args:
        x ([type]): [description]
        re ([type]): [description]
        im ([type]): [description]
        log (bool, optional): [description]. Defaults to False.
    """
    fig=plt.figure()
    ax1=plt.subplot(111)
    z=np.array(re,dtype=complex)+np.array(1j *im,dtype=complex)
    if log: 
        ax1.plot(x,20*np.log(np.abs(z)))
        ax1.set_ylabel("Z in dB")
    else:
        ax1.plot(x,abs(z))
        ax1.set_ylabel("Z in Ohm")
    ax1.set_xlabel("Frequency in Hz")
    plt.show()
