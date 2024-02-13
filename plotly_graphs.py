import pandas as pd
import plotly.express as px
from jinja2 import Template

df = pd.read_csv('aufgeräumter_Datensatz.csv')

grouped_df = df.groupby('Zeitschrift').agg({'Titel' : 'count', 'Land' : 'first', 'Zeitschriftkürzel' : 'first'}).reset_index()
grouped_df = grouped_df.rename(columns= {'Titel': 'Anzahl'})

sorted_df = grouped_df.sort_values(by="Anzahl", ascending=False)

print(sorted_df.head())

import plotly.express as px

fig1 = px.bar(
  sorted_df,
  orientation='h',
  x="Anzahl",
  y="Zeitschriftkürzel",
  labels=dict(Anzahl="Anzahl veröffentlichter Artikel", Zeitschriftkürzel="Kürzel der Zeitschriften"),
  color="Land",
  title="Anzahl der veröffentlichten Artikel pro Zeitschrift, absteigend nach Anzahl sortiert und nach Veröffentlichungsland gruppiert.",
  width=1500,
  height=700,
  hover_name= "Zeitschrift", 
  hover_data={
    'Zeitschriftkürzel': False,
    'Land': False,
    'Zeitschrift': False,
    'Anzahl': True
    },
  color_discrete_sequence=px.colors.qualitative.G10)  #category_values -> Länder sortieren?

fig1.update_traces(width=1)

fig1.update_layout(
  title={
    'text': "Anzahl der veröffentlichten Artikel pro Zeitschrift, absteigend nach Anzahl sortiert und nach Veröffentlichungsland gruppiert.",
    'font': {
      'size': 20
    },
    'automargin': True,
    'yref': 'container',
    'y': 0.9,
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
  },
  xaxis={
  },
  yaxis=dict(autorange="reversed"),
  paper_bgcolor = "#dadada",
)

#fig1.show()


# Daten aus der CSV-Datei lesen
df = pd.read_csv('aufgeräumter_Datensatz.csv')

# Treemap erstellen
fig2 = px.treemap(
  df, 
  path=['Land', 'Zeitschriftkürzel'],
  hover_data={'Zeitschriftkürzel': False, 'Zeitschrift': True}, 
  color_discrete_sequence=px.colors.qualitative.G10,
  width=1500,
  height=700,
  )

# Layoutanpassungen
fig2.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    title={
      'text': "Proportionale Aufteilung des Raumes in Länder und Zeitschriften nach Anzahl der Artikel",
      'font': {
        'size': 20
      },
      'automargin': True,
      'yref': 'container',
      'y': 0.9,
      'x': 0.5,
      'xanchor': 'center',
      'yanchor': 'top'
      },
    paper_bgcolor = "#dadada",
)

# Text in den Karten zentrieren
fig2.update_traces(textposition='middle center')


# export to html



output_html_path = r"index.html"
input_template_path = r"template.html"

plotly_jinja_data = { "fig1":fig1.to_html(full_html=False),
                      "fig2":fig2.to_html(full_html=False)}


with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_template_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))
