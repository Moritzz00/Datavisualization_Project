import pandas as pd
import matplotlib.pyplot as plt

# Beispiel-Datensatz (ersetze dies durch den Pfad zu deiner CSV-Datei)
data = pd.read_csv('aufgeräumter_Datensatz.csv')

# DataFrame erstellen
df = pd.DataFrame(data)

# Gruppieren nach Land und Zeitschrift und Zählen der Anzahl von Artikeln
grouped = df.groupby(['Land', 'Zeitschrift']).size().reset_index(name='Anzahl')

# Baumkarte erstellen
fig, ax = plt.subplots()

for i, (land, df_land) in enumerate(grouped.groupby('Land')):
    sizes = df_land['Anzahl']
    labels = df_land['Zeitschrift']
    explode = [0.1] * len(sizes)  # Um die einzelnen Sektoren hervorzuheben

    ax.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%',
           shadow=True, startangle=90 + i * 360 / len(grouped['Land'].unique()))
    ax.set_title(land)
    ax.axis('equal')  # Sorgt dafür, dass das Diagramm kreisförmig ist

plt.tight_layout()
plt.show()
