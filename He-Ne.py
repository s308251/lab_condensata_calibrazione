# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 20:59:37 2025

@author: Marta
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import voigt_profile as voigt

legend=["He-Ne-4"]
#legend=["He-Ne-3","He-Ne-4","He-Ne-5"] 
first_col_arrays=[]
second_col_arrays=[]


'''
1 He-Ne 6320-6340-fend 0.5-step 0.5-sens 5 (satura)
2 He-Ne 6328-6337-step 0,1 (satura)
3 He-Ne 6328-6337-fend 0.2-step 0,1
4 He-Ne 6328-6337-fend 0.2- step 0.08-sens 10 (fenditura + stretta)
5 He-Ne 6328-6337-fend 0.1- step 0.1-sens 2 (non prende tutto il grafico)
6 He-Ne 6328-6337-fend 0.2- step 0.1-sens 2

'''



def load_data_from_files():
    folder_path=r"C:\Users\Marta\Desktop\Marta-Alessia\He-Ne"
    for file_nam in legend:
        file_path = str(folder_path) + "/" + str(file_nam)
        data = np.loadtxt(str(file_path))
        first_col_arrays.append(data[:, 0])
        second_col_arrays.append(data[:, 1])
    return(first_col_arrays,second_col_arrays)

# Define the Gaussian function
def gaussian(x, amp, mu, sigma):
    return amp * np.exp(-(x - mu)**2 / (2 * sigma**2))

# Define the Lorentzian function
def lorentzian(x, amp, mu, gamma):
    return amp * ((gamma)**2 / ((x - mu)**2 + (gamma)**2))

# Funzione di adattamento Voigt
def voigt_fit(x ,amplitude, center, sigma, gamma):
    return amplitude*voigt((x - center), sigma, gamma)


 # Stima iniziale per ampiezza, posizione del picco e larghezza 
p0s = [[1.66, 633.26, 0.2],[2, 633.25, 0.2]]

# Carica i dati
first_col_arrays, second_col_arrays = load_data_from_files()

# Crea i grafici
plt.figure()
for l in range(len(first_col_arrays)):
    #Dati
    x=np.array(first_col_arrays[l]/10) #in nm
    y=np.array(second_col_arrays[l]*1000) #in mV
    plt.plot(x,y,'-',color='gray',label="{}".format(legend[l]))
    
    
    
    # Fit della funzione voigt
    params, covariance = curve_fit(voigt_fit, x, y, p0=[0.05, 633, 0.05, 0.05])
    amplitude_fit,center_fit, sigma_fit, gamma_fit = params
    error = np.sqrt(np.diag(covariance))
    print(amplitude_fit,center_fit, sigma_fit, gamma_fit,error)
    
    # Creazione del grafico
    
    y_fit = voigt_fit(x, amplitude_fit, center_fit, sigma_fit, gamma_fit)
    plt.plot(x, y_fit,'o',color='blue',label=f'Fit voigt\nAmplitude = {amplitude_fit:.3f}+/-0.001,\nCentro = {center_fit:.0f}+/-1 nm,\n$\\sigma$={sigma_fit:.4f}+/-0.0004,\n$\\gamma$ = {gamma_fit:.4f}+/-0.0006')
    plt.xlabel('$\\lambda$[nm]')
    plt.ylabel('$Tensione$[mV]')
    plt.title('Fit voigt del picco di emissione del laser He-Ne')
    plt.legend()
    plt.grid()
    
    
    
    

plt.show()



'''


    # Fit della funzione Lorentziana
    params, covariance = curve_fit(lorentzian, x, y, p0=[2, 633.25, 0.2])

    # Parametri adattati
    a_fit, x0_fit, gamma_fit = params
    error = np.sqrt(np.diag(covariance))
    #print(params,error)

    # Creazione del grafico
    
    y_fit = lorentzian(x, a_fit, x0_fit, gamma_fit)
    a_fit=round(a_fit)
    x0_fit=round(x0_fit)
    plt.plot(x, y_fit,'o',color='green',label=f'Fit Lorentziano\nAmpiezza = {a_fit:.0f}+/-0.10 mV,\nCentro = {x0_fit:.0f}+/-1 nm,\n$\\gamma$ = {gamma_fit:.2f}+/-0.01')
    plt.xlabel('$\\lambda$[nm]')
    plt.ylabel('$V$[mV]')
    plt.title('Fit Lorentziano del picco di emissione del laser He-Ne')
    plt.legend()
    plt.grid()
  
'''