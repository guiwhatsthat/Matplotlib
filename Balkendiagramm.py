import matplotlib.pyplot as plt

# Liste der Kategorien und Werte
kategorien = ['A', 'B', 'C', 'D', 'E']
werte = [23, 45, 12, 67, 34]

# Erstelle ein Balkendiagramm
plt.bar(kategorien, werte)
plt.xlabel('Kategorien')
plt.ylabel('Werte')
plt.title('Balkendiagramm')
plt.show()
