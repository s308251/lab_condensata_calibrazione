# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 23:40:20 2025

@author: Marta
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
legend=["He-Ne-t_lock 1","He-Ne-t_lock 3","He-Ne-t_lock 10","He-Ne-t_lock 30","He-Ne-t_lock 100","He-Ne-t_lock 300"]
x_data=np.linspace(0,39,num=40)
t_l=[1,3,10,30,100,300]
second_col_arrays=[]
v=[]
p0s=[[0,1.7],[0,1.7],[0,1.7],[0,1.7],[0,1.7],[0,1.7]]


'''
He-Ne-t_lock 1 - 40 pt-sens 5
He-Ne-t_lock 3 - 40 pt-sens 5
He-Ne-t_lock 10 - 40 pt-sens 5
He-Ne-t_lock 30 - 40 pt-sens 5
He-Ne-t_lock 100 - 40 pt-sens 5
He-Ne-t_lock 300 - 40 pt-sens 5

'''

def load_data_from_files():
    folder_path=r"C:\Users\Marta\Desktop\Marta-Alessia\He-Ne"
    for file_nam in legend:
        file_path = str(folder_path) + "/" + str(file_nam)
        data = np.loadtxt(str(file_path))
        second_col_arrays.append(data[:, 1])
    return(second_col_arrays)


def retta(x, m, q):
        return m*x+q
#Dati
second_col_arrays= load_data_from_files()
 

# Crea i grafici

plt.figure()
for i in range(len(legend)):
        y_data=np.array(second_col_arrays[i]*1000) #in mV
        y=np.sum(y_data)/len(y_data)
        y=round(y)
        v.append(y)
        plt.plot(x_data, y_data,'-',color='gray',label="{}".format(legend[i]))
        params, covariance = curve_fit(retta,x_data, y_data, p0=p0s[i])
        m,q= params
        error = np.sqrt(np.diag(covariance))
        y_fit=retta(x_data,m,q)
        plt.plot(x_data, y_fit,'-',color='green',label=f'Fit retta\nm = {m:.0f}, q= {q:.0f}')
        plt.xlabel('$punti$')
        plt.ylabel('$V$[mV]')
        plt.title('Influenza su intensità He-Ne del tempo integrazione')
        plt.legend()
        plt.grid()

print(v)
plt.figure()
for i in range(len(legend)):
    plt.plot(t_l[i],v[i],'-',color='blue',label="{}".format(legend[i]))
    plt.xlabel('$time lock-in$[ms]')
    plt.ylabel('$V$[mV]')
    plt.title('Influenza su intensità He-Ne del tempo integrazione')
    plt.legend()
    plt.grid()
'''    

plt.figure()
for i in range(len(legend)):
    plt.plot(t_l[i],u[i],'-',color='blue',label="{}".format(legend[i]))
    plt.xlabel('$time lock-in$[ms]')
    plt.ylabel('$V$[mV]')
    plt.title('Influenza su intensità He-Ne del tempo integrazione')
    plt.legend()
    plt.grid()
 '''   
    

plt.show()
    