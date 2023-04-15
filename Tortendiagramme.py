import matplotlib.pyplot as plt

# Liste der Beschriftungen und Anteile
labels = ['A', 'B', 'C', 'D', 'E']
anteile = [23, 45, 12, 67, 34]

# Erstelle ein Tortendiagramm
plt.pie(anteile, labels=labels, autopct='%1.1f%%')
plt.title('Tortendiagramm')
plt.axis('equal')
plt.show()
