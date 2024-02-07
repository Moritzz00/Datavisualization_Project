
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Daten aus der CSV-Datei lesen
data = pd.read_csv("./aufgeräumter_Datensatz.csv")

# Gruppieren nach Land und Zeitschrift und Zählen der Artikel
land_zeitschrift_count = data.groupby(['Land', 'Zeitschrift']).size().reset_index(name='Artikel')

# Gruppieren nach Land und Summieren der Artikel pro Zeitschrift
land_zeitschrift_sum = land_zeitschrift_count.groupby('Land')['Artikel'].sum()

# Die Namen der Länder in einem separaten Array speichern
land_namen = list(land_zeitschrift_sum.index)
land_namen[1] = "L-Stein"
land_namen[2] = "NL"
land_namen_index = pd.Index(land_namen)

land_farben = ['pink', 'cyan', 'lawngreen', 'yellow', 'orange']

plt.title('Verteilung der Zeitschriften nach Ländern')

# Den Kasten für das Land zeichnen
squarify.plot(sizes=land_zeitschrift_sum.values, label=land_namen, color=land_farben, pad=1)

plt.axis("off")
plt.show()

