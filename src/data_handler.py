import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

import csv_importer as ci
import data_plotter as dplt

#plot_xy([1,2,3],[12,3,4])
data = ci.read_network_analyzer_csv("IIDEAL.csv")

dplt.plot_complex(data.f,data.re,data.im)
#data=read_csv("src\IIDEAL.csv",header_line=2,col_name=['f','re','im','na1'],delimiter=',')

#print(data)

#data['z']=np.abs(np.array(data.re,dtype=complex)+np.array(1j *data.im,dtype=complex))
#print(data.z.values.max())
#res_freq=data[data['z']==np.max(data.z.values())]
#print(res_freq)
#plot_complex(data.f,data.re,data.im)



