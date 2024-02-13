import pandas as pd
import plotly.express as px

# Daten aus der CSV-Datei lesen
df = pd.read_csv('aufgeräumter_Datensatz.csv')

# Treemap erstellen
fig2 = px.treemap(df, path=['Land', 'Zeitschriftkürzel'], hover_data={'Zeitschriftkürzel': False, 'Zeitschrift': True}, color_discrete_sequence=px.colors.qualitative.G10)

# Layoutanpassungen
fig2.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    title="Proportionale Aufteilung des Raumes in Länder und Zeitschriften nach Anzahl der Artikel",
)

# Text in den Karten zentrieren
fig2.update_traces(textposition='middle center')

# Plot anzeigen
fig.show()


