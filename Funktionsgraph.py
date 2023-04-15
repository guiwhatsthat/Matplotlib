import numpy as np
import matplotlib.pyplot as plt

# Erzeuge x-Werte von -10 bis 10 in 100 Schritten
x = np.linspace(-10, 10, 100)
# Berechne y-Werte als Quadrat der x-Werte
y = x**2

# Erstelle einen Funktionsgraphen für die Funktion y = x^2
plt.plot(x, y)
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('Funktionsgraph: y = x^2')
plt.grid(True)
plt.show()