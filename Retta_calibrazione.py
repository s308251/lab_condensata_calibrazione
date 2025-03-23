import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def retta(x, m, q):
        return m*x+q

# Lunghezze d'onda misurate (esempio)
A1=np.sum([589.5644201385938,589.4433224606806,589.4006606090827,589.4055668927026])/4
A2=np.sum([590.1367315096594,590.0150331503668,589.9864470967204,589.9625808371536])/4
A3=np.sum([818.7394037593795,818.7738783873174,818.6945545774086,818.6799370139972])/4
A4=np.sum([819.7673407790379,819.8143128805298,819.760397254208,819.7502756525663])/4

sigma1=(589.5644201385938-589.4055668927026)/2
sigma2=(590.1367315096594-589.9625808371536)/2
sigma3=(818.7738783873174-818.6799370139972)/2
sigma4=(819.8143128805298-819.7502756525663)/2


measured_peaks = np.array([A1, A2,A3, A4])  # in nm

# Lunghezze d'onda di riferimento
reference_peaks = np.array([588.9950, 589.5924, 818.3256, 819.4824])  # in nm

A1=round(A1,2)
A2=round(A2,2)
A3=round(A3,2)
A4=round(A4,2)
sigma1=round(sigma1,3)
sigm2=round(sigma2,3)
sigma3=round(sigma3,3)
sigma4=round(sigma4,3)


#Grafico della retta di calibrazione
plt.figure(figsize=(8, 6))
# Fit della funzione voigt
params, covariance = curve_fit(retta,reference_peaks,measured_peaks,p0=[1,0])
m,q= params
error = np.sqrt(np.diag(covariance))
measured_fit=retta(reference_peaks,m,q)
plt.plot( reference_peaks,measured_peaks,'o', color='red', label=f'posizioni dei picchi\n $\\lambda_1$= {A1:.2f}+/-{sigma1:.2f} nm,\n$\\lambda_2$= {A2:.2f}+/-{sigma2:.2f} nm,\n$\\lambda_3$= {A3:.2f}+/-{sigma3:.2f} nm,\n$\\lambda_4$= {A4:.2f}+/-{sigma4:.2f} nm')
plt.plot(reference_peaks,measured_fit,'--', color='grey', label=f'retta di calibrazione\n  y={m:.2f}x+{q:.2f}')
plt.title('Retta di Calibrazione', fontsize=14)
plt.title('Retta di Calibrazione', fontsize=14)
plt.xlabel('$\\lambda$ misurata[nm]', fontsize=12)
plt.ylabel('$\\lambda$ teorica[nm]', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

