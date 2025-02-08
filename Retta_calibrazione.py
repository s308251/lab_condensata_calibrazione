import numpy as np
import matplotlib.pyplot as plt



def linear_regression(X,y):
    X_b=np.c_[np.ones((len(X),1)),X] #colonna di bias
    model=np.linalg.inv(X_b.T @ X_b) @X_b.T @y #calcola coefficienti
    return model

# Lunghezze d'onda misurate (esempio)
measured_peaks = np.array([5895, 5901, 8188, 8198])  # in A
measured_peaks=measured_peaks.reshape(-1,1)
# Lunghezze d'onda di riferimento (esempio)
reference_peaks = np.array([5889, 5895, 8183, 8194])  # in A
reference_peaks=reference_peaks.reshape(-1,1)


# Creazione del modello di regressione lineare
model= linear_regression(measured_peaks,reference_peaks)

# Coefficiente angolare e intercetta della retta di calibrazione
slope = model[1][0]
intercept = model[0][0]

#predizione dei valori calibrati
X_new=np.array([[np.min(measured_peaks)],[np.max(measured_peaks)]]).reshape(-1,1)
X_new_b=np.c_[np.ones((2,1)),X_new]
calibrated_peaks= X_new_b @ model

#Grafico della retta di calibrazione
plt.figure(figsize=(8, 6))
plt.scatter(measured_peaks, reference_peaks, color='red', label='Dati misurati', zorder=3)
plt.plot(X_new, calibrated_peaks, color='blue', label=f'Retta di calibrazione\ny = {slope:.4f}x + {intercept:.4f}', zorder=2)
plt.plot([0, max(measured_peaks)], [0, max(reference_peaks)], color='green', linestyle='--', label='Retta ideale (y = x)', zorder=1)

plt.title('Retta di Calibrazione', fontsize=14)
plt.xlabel('Lunghezza d\'onda misurata (A)', fontsize=12)
plt.ylabel('Lunghezza d\'onda di riferimento (A)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

