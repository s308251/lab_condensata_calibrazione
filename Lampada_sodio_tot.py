#Lampada al sodio

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
[18*10*(-3),5894,0.5,9*10*(-3),5901,0.5]
[3.8*10**(-4),8187.8,0.5,5.6*10**(-4),8198,0.5]


# Funzione per caricare i dati dai file dalla stessa cartella

#percorso del file

legend=["3-picco 5894","4-picco 5894","9-picco 5894","11-picchi 8183","12-picchi 8183","13-picchi 8183","14-picchi 8183"]
first_col_arrays = []
second_col_arrays = []
p0s=[[18*10*(-3),5894,0.5,9*10*(-3),5901,0.5],[18*10*(-3),5894,0.5,9*10*(-3),5901,0.5],[18*10*(-3),5894,0.5,9*10*(-3),5901,0.5],[3.8*10**(-4),8187.8,0.5,5.6*10**(-4),8198,0.5],[3.8*10**(-4),8187.8,0.5,5.6*10**(-4),8198,0.5],[3.8*10**(-4),8187.8,0.5,5.6*10**(-4),8198,0.5],[3.8*10**(-4),8187.8,0.5,5.6*10**(-4),8198,0.5]]

def load_data_from_files():
    folder_path='/home/s308251@DS.UNITS.IT/Desktop/storage/s308251/lab_condensata/Marta-Alessia/lamp_sodio'
    for file_name in legend:
        file_path = str(folder_path) + "/"+ str(file_name)
        data = np.loadtxt(str(file_path))
        first_col_arrays.append(data[:, 0])
        second_col_arrays.append(data[:, 1])
    return(first_col_arrays,second_col_arrays)


# Define the Gaussian function
def gaussian(x, amp, mu, sigma):
    return amp * np.exp(-(x - mu)**2 / (2 * sigma**2))

# Sum of two Gaussians
def double_gaussian(x, amp1, mu1, sigma1, amp2, mu2, sigma2):
    return gaussian(x, amp1, mu1, sigma1) + gaussian(x, amp2, mu2, sigma2)


# Define the Lorentzian function
def lorentzian(x, amp, mu, gamma):
    return amp * (gamma/2 / ((x - mu)**2 + (gamma/2)**2))

# Sum of two Lorentzians
def double_lorentzian(x, amp1, mu1, gamma1, amp2, mu2, gamma2):
    return lorentzian(x, amp1, mu1, gamma1) + lorentzian(x, amp2, mu2, gamma2)


# Voigt profile (convolution of Gaussian and Lorentzian)
def voigt(x, amp, mu, sigma, gamma):
    return amp * voigt_profile(x - mu, sigma, gamma)

# Sum of two Voigt profiles
def double_voigt(x, amp1, mu1, sigma1, gamma1, amp2, mu2, sigma2, gamma2):
    return voigt(x, amp1, mu1, sigma1, gamma1) + voigt(x, amp2, mu2, sigma2, gamma2)


# Carica i dati
first_col_arrays, second_col_arrays = load_data_from_files()


# Crea i grafici

for l in range(len(first_col_arrays)):
    plt.figure()
    #Dati
    x=np.array(first_col_arrays[l])
    y=np.array(second_col_arrays[l])
    plt.plot(x,y,'o-',color='blue',label="{}".format(legend[l]))
    plt.grid(True)
    

    #Fit gaussiano
    popt,pcov=curve_fit(double_gaussian,x,y,p0=p0s[l])
    amp1,cen1,wid1,amp2,cen2,wid2= popt
    y_fit=double_gaussian(x,amp1, cen1,wid1,amp2,cen2,wid2)
    plt.plot(x,y_fit,'o-',color='green',label="fit_gauss {}".format(legend[l]))
    plt.title("{}".format(legend[l]))
    plt.xlabel('Lunghezza onda [A]', fontstyle='italic')
    plt.ylabel('Tensione [V]', fontstyle='italic')
    plt.legend()
    plt.grid(True)
    

    #Fit lorentziano
    popt_2,pcov_2=curve_fit(double_lorentzian,x,y,p0=p0s[l])
    amp1,cen1,wid1,amp2,cen2,wid2= popt_2
    y_fit=double_lorentzian(x,amp1, cen1,wid1,amp2,cen2,wid2)
    plt.plot(x,y_fit,'o-',color='red',label="fit_lorentz {}".format(legend[l]))
    plt.title("{}".format(legend[l]))
    plt.xlabel('Lunghezza onda [A]', fontstyle='italic')
    plt.ylabel('Tensione [V]', fontstyle='italic')
    plt.legend()
    plt.grid(True)
    

plt.show()


