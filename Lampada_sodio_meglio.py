# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 20:36:56 2025

@author: Marta
"""

#Lampada al sodio

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


'''
Commenti sui picchi:
    15-10
    1 sovrapposti
    2 sovrapposti ed intensità 2° sbagliata
    3 Non si distinguono i due picchi
    4-5-6 tanto rumore e picchi sovrapposti
    22-10
    1 5000 Bello-picchi a 5895 (I=0.01899) 5901 (I=0.01262)  
    2 5000 Bello-5894 (I=0.01848) 5900 (I=0.01201) 
    3 8000 bello- 8187 (I=0.00038)  8198 (I=0.00053)
    4 8000 bello- 8187 (I=0.00041)  8198 (I=0.00057) 
    13-12
    1 5000 Bello-5894 (I=0.00042) 5900 (I=0.00029) 
    2 5000 Bello-5894 (I=0.00090) 5900 (I=0.00062) 
    3 8000 bello- 8187 (I=0.00045)  8198 (I=0.00063)
    4 8000 bello- 8187 (I=0.00086)  8198 (I=0.00120)
    
    Valori teorici dal nist
    5890 I -  5896(I=1\2)
    8183 (I=1/2) -8194 I
'''
# Funzione per caricare i dati dai file dalla stessa cartella

#percorso del file


#legend=["22-10-5894-1","22-10-5894-2","13-12-5894-1","13-12-5894-2","22-10-8100-1","22-10-8100-2", "13-12-8100-1","13-12-8100-2"] 
legend=["22-10-5894-2", "13-12-8100-1"]
first_col_arrays = [] # in A
second_col_arrays = [] # in V
title=["Spettro Lampada al sodio [picchi 588 nm -589 nm]","Spettro Lampada al sodio [picchi 818 nm -819 nm]"]
parametri=["Picchi 588 nm - 589 nm","Picchi 518 nm - 819 nm","Fit gaussiano","Fit gaussiano"]
#p0s=[[18.7,589.5,0.25,12.4,590,0.25],[18.2,589.5,0.25,12,590,0.25],[0.41,589,0.25,0.28,590,0.25],[0.89,589.3,0.25,0.62,590,0.25],[0.45,819,0.25,0.63,820,0.25],[0.45,819,0.25,0.63,820,0.25],[0.45,819,0.25,0.63,820,0.25],[0.45,819,0.25,0.63,820,0.25],[0.45,819,0.25,0.63,820,0.25]]
p0s=[[18.2,589.5,0.25,12,590,0.25],[0.45,819,0.25,0.63,820,0.25]]

def load_data_from_files():
    folder_path=r"C:\Users\Marta\Desktop\Marta-Alessia\lampada_sodio"
    for file_nam in legend:
        file_path = str(folder_path) + "/" + str(file_nam)
        data = np.loadtxt(str(file_path))
        first_col_arrays.append(data[:, 0])
        second_col_arrays.append(data[:, 1])
    return(first_col_arrays,second_col_arrays)


# Define the Gaussian function
def gaussian(x, amp, mu, sigma):
    return amp * np.exp(-(x - mu)**2 / (2 * sigma**2))

# Sum of two Gaussians
def two_gaussian(x, amp1, mu1, sigma1, amp2, mu2, sigma2):
    return gaussian(x, amp1, mu1, sigma1) + gaussian(x, amp2, mu2, sigma2) 

# Carica i dati
first_col_arrays, second_col_arrays = load_data_from_files() #in A,V


# Crea i grafici

for l in range(len(first_col_arrays)):
    plt.figure()
    #Dati
    x=np.array(first_col_arrays[l]/10) #in nm
    y=np.array(second_col_arrays[l]*1000) #in mV
    plt.plot(x,y,'-',color='gray',label="per")#label="{}".format(parametri[l])
    

    #Fit gaussiano
    popt,pcov=curve_fit(two_gaussian,x,y,p0=p0s[l])
    amp1,cen1,wid1,amp2,cen2,wid2=popt
    error = np.sqrt(np.diag(pcov))
    print(cen1,cen2,error)
    y_fit=two_gaussian(x,amp1,cen1,wid1,amp2,cen2,wid2)
    round(amp1,0),round(cen1,0),round(wid1,2),round(amp2,0),round(cen2,0),round(wid2,2)
    plt.plot(x,y_fit,'o',color='green',label=f'Fit Gaussiano\nAmpiezza_1 = {amp1:.0f}+/-0.1 mV, Centro_1 = {cen1:.0f}+/-0.1 nm, $\\sigma_1$ = {wid1:.2f},Ampiezza_2 = {amp2:.0f}+/-0.1 mV, Centro_2 = {cen2:.0f}+/-0.1 nm, $\\sigma_2$ = {wid2:.2f}')
    #plt.title("{}".format(title[l]))
    plt.xlabel('$\\lambda$[nm]', fontstyle='italic')
    plt.ylabel('$V$[mV]', fontstyle='italic')
    plt.legend()
    plt.grid(True)
    





plt.show()