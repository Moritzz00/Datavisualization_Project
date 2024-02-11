import matplotlib.pyplot as plt
import squarify
import pandas as pd
import base64
from io import BytesIO

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

plt.figure(figsize=(10, 6))  # Define the size of the figure
plt.title('Verteilung der Zeitschriften nach Ländern')

# Den Kasten für das Land zeichnen
squarify.plot(sizes=land_zeitschrift_sum.values, label=land_namen, color=land_farben, pad=1)

plt.axis("off")
plt.show()


#^
#^# Convert plot to a base64-encoded image
#^buffer = BytesIO()
#^plt.savefig(buffer, format='png')
#^buffer.seek(0)
#^image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
#^
#^# Generate HTML code with the embedded image
#^html_code = f'<img src="data:image/png;base64,{image_base64}" alt="Squarify Plot">'
#^
#^# Write the HTML code to a file
#^output_html_path = "index.html"
#^with open(output_html_path, "w") as output_file:
#^    output_file.write(html_code)
