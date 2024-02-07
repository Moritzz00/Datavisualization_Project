import pandas as pd
import matplotlib.pyplot as plt
import squarify

csv_datei = "aufgeräumter_Datensatz.csv"

df = pd.read_csv(csv_datei)

# nach Ländern grupiieren und die Summe der Zeitschriften ermitteln
land_zs_summe = df.groupby('Land')['Zeitschrift'].sum()

# Farben für die Treemap festlegen
farben = plt.cm.Paired.colors

# Treemap erstellen (Länderebene)
plt.figure(figsize=(10, 8))
squarify.plot(sizes=land_zs_summe.values, label=land_zs_summe.index, color=farben, alpha=0.8)

# Länder-Ebene beschriften
plt.title('Zeitschriften')

# In die Länder-Boxen verschachtelte Treemap für Artikel erstellen
for index, (land, zs_summe) in enumerate(land_zs_summe.items()):
    # Daten für die verschachtelte Treemap auf Artikel-Ebene
    artikel_data = df[df['Land'] == land]
    artikel_counts = artikel_data.groupby('Zeitschrift')['Artikel'].sum()

    # Treemap für Artikel erstellen
    ax = plt.gca()
    x, y, dx, dy = squarify.get_squarify_axes(0.1, 0.1, 0.8, 0.8, land_counts.values[index], aspect_ratio=1)
    squarify.plot(sizes=artikel_counts.values, x=x, y=y, dx=dx, dy=dy, label=artikel_counts.index, color=farben, alpha=0.8, ax=ax)

# Diagramm anzeigen
plt.axis('off')
plt.show()

