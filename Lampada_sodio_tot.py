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

#p0s=[[18,589.5,0.25,12,590,0.25],[18,589,0.25,12,590,0.25],[0.42,589,0.25,0.28,590,0.25],[0.9,589.5,0.25,0.6,590,0.25],[0.38,819,0.2,0.52,820,0.2],[0.41,819,0.25,0.57,820,0.25],[0.45,819,0.25,0.63,820,0.25],[0.86,819,0.25,1.2,820,0.25]]
p0s=[[18,589,0.25,12,590,0.25],[0.45,819,0.25,0.63,820,0.25]]
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
'''
# Sum of four Gaussians
def four_gaussian(x, amp1, mu1, sigma1, amp2, mu2, sigma2, amp3, mu3, sigma3, amp4, mu4, sigma4):
    return gaussian(x, amp1, mu1, sigma1) + gaussian(x, amp2, mu2, sigma2) + gaussian(x, amp3, mu3, sigma3) + gaussian(x, amp4, mu4, sigma4)
'''
# Sum of two Gaussians
def two_gaussian(x, amp1, mu1, sigma1, amp2, mu2, sigma2):
    return gaussian(x, amp1, mu1, sigma1) + gaussian(x, amp2, mu2, sigma2) 

# Define the Lorentzian function
def lorentzian(x, amp, mu, gamma):
    return amp * ((gamma)**2 / ((x - mu)**2 + (gamma)**2))

# Sum of two Lorentian
def two_lorentzian(x, amp1, mu1, gamma1, amp2, mu2, gamma2):
    return lorentzian(x, amp1, mu1, gamma1) + lorentzian(x, amp2, mu2, gamma2) 
    
'''
# Sum of four Lorentzians
def four_lorentzian(x, amp1, mu1, gamma1, amp2, mu2, gamma2, amp3, mu3, gamma3, amp4, mu4, gamma4):
    return lorentzian(x, amp1, mu1, gamma1) + lorentzian(x, amp2, mu2, gamma2)+ lorentzian(x, amp3, mu3, gamma3)+ lorentzian(x, amp4, mu4, gamma4)


# Voigt profile (convolution of Gaussian and Lorentzian)
def voigt(x, amp, mu, sigma, gamma):
    return amp * voigt_profile(x - mu, sigma, gamma)

# Sum of two Voigt profiles
def four_voigt(x, amp1, mu1, sigma1, gamma1, amp2, mu2, sigma2, gamma2, amp3, mu3, sigma3, gamma3, amp4, mu4, sigma4, gamma4):
    return voigt(x, amp1, mu1, sigma1, gamma1) + voigt(x, amp2, mu2, sigma2, gamma2) + voigt(x, amp3, mu3, sigma3, gamma3) + voigt(x, amp4, mu4, sigma4, gamma4)
'''


# Carica i dati
first_col_arrays, second_col_arrays = load_data_from_files() #in A,V


# Crea i grafici

for l in range(len(first_col_arrays)):
    plt.figure()
    #Dati
    x=np.array(first_col_arrays[l]/10) #in nm
    y=np.array(second_col_arrays[l]*1000) #in mV
    plt.plot(x,y,'-',color='gray',label="{}".format(parametri[l]))
    

    #Fit gaussiano
    popt,pcov=curve_fit(two_gaussian,x,y,p0=p0s[l])
    amp1,cen1,wid1,amp2,cen2,wid2=popt
    y_fit=two_gaussian(x,amp1,cen1,wid1,amp2,cen2,wid2)
    #amp1,cen1,wid1,amp2,cen2,wid2,amp3,cen3,wid3,amp4,cen4,wid4= popt
    #y_fit=four_gaussian(x,amp1,cen1,wid1,amp2,cen2,wid2,amp3,cen3,wid3,amp4,cen4,wid4)
    minori_gauss=y_fit-y
    plt.plot(x,y_fit,'o',color='green',label=f'Fit Gaussiano\nAmpiezza_1 = {amp1:.2f} mV, Centro_1 = {cen1:.2f} nm, $\\sigma$ = {wid1:.2f},Ampiezza_2 = {amp2:.2f} mV, Centro_2 = {cen2:.2f} nm, $\\sigma$ = {wid2:.2f}')
    #plt.plot(x,y_fit,'o',color='green',label="{}".format(parametri[l+2])
    plt.title("{}".format(title[l]))
    plt.xlabel('Lunghezza onda [nm]', fontstyle='italic')
    plt.ylabel('Tensione [mV]', fontstyle='italic')
    plt.legend()
    plt.grid(True)
    
'''

    
    #Fit lorentziano
    popt_2,pcov_2=curve_fit(two_lorentzian,x,y,p0=p0s[l])
    amp1, mu1, gamma1, amp2, mu2, gamma2 =popt_2
    y_fit=two_lorentzian(x, amp1, mu1, gamma1, amp2, mu2, gamma2)
    #x, amp1, mu1, gamma1, amp2, mu2, gamma2, amp3, mu3, gamma3, amp4, mu4, gamma4= popt_2
    #y_fit=four_lorentzian(x,x, amp1, mu1, gamma1, amp2, mu2, gamma2, amp3, mu3, gamma3, amp4, mu4, gamma4)
    minori_lorentz=np.array(y_fit-y)
    plt.plot(x,y_fit,'o',color='red',label="fit_lorentz {}".format(legend[l]))
    plt.title("{}".format(legend[l]))
    plt.xlabel('Lunghezza onda [nm]', fontstyle='italic')
    plt.ylabel('Tensione [mV]', fontstyle='italic')
    plt.legend()
    plt.grid(True)
    
       
    plt.figure()
    plt.plot(x,minori_gauss,color='green', label='M_Gauss')
    plt.plot(x,minori_lorentz,color='red', label='M_Lorentz')
    plt.title("Minori {}".format(legend[l]))
    plt.xlabel('Lunghezza onda [nm]', fontstyle='italic')
    plt.ylabel('Tensione [mV]', fontstyle='italic')
    plt.grid()
    plt.legend()
'''
    

plt.show()

