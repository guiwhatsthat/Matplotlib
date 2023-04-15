import numpy as np
import matplotlib.pyplot as plt

# Definiere die x-Werte
x = np.linspace(0, 2 * np.pi, 100)

# Berechne die y-Werte für die verschiedenen Funktionen
y1 = np.sin(x)
y2 = np.cos(x)

# Zeichne die Funktionsgraphen
plt.plot(x, y1, label='sin(x)')  # Sinus-Funktion
plt.plot(x, y2, label='cos(x)')  # Kosinus-Funktion

# Füge Legende, Achsenbeschriftungen und Titel hinzu
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Mehrere Funktionsgraphen in der selben Graphik')

# Zeige die Graphik an
plt.show()
