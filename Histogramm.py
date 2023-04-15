import numpy as np
import matplotlib.pyplot as plt

# Erzeuge 1000 zufällige Datenpunkte aus einer Normalverteilung
data = np.random.randn(1000)

# Erstelle ein Histogramm mit 30 Bins
plt.hist(data, bins=30)
plt.xlabel('Werte')
plt.ylabel('Häufigkeit')
plt.title('Histogramm')
plt.grid(True)
plt.show()
