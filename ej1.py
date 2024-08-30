import numpy as np
import matplotlib.pyplot as plt

# Spreading Factor (SF)
SF = 10

# Generar múltiples secuencias de bits para crear el histograma
num_samples = 10000
bit_sequences = np.random.randint(0, 2, (num_samples, SF))

# Contar la cantidad de ceros y unos
bit_values = bit_sequences.flatten()

# Crear el histograma de los bits
plt.hist(bit_values, bins=2, edgecolor='black')
plt.xticks([0, 1])
plt.title('Histograma de Probabilidad de los Bits (0 y 1)')
plt.xlabel('Bit')
plt.ylabel('Frecuencia')
plt.show()

# 2) Histograma de los simbolos
# Función para calcular el símbolo s(nT_s) según la ecuación (1)
def compute_symbol(w_nTs):
    return np.sum([w_nTs[h] * 2**h for h in range(len(w_nTs))])

# Generar símbolos a partir de las secuencias de bits
symbols = np.array([compute_symbol(seq) for seq in bit_sequences])

# Crear el histograma de los símbolos
plt.hist(symbols, bins='auto', edgecolor='black')
plt.title('Histograma de los Símbolos s(nT_s)')
plt.xlabel('Símbolo')
plt.ylabel('Frecuencia')
plt.show()
