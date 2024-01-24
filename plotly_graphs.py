import pandas as pd

df = pd.read_csv('Baumkarte_Datensatz.csv')

grouped_df = df.groupby('Zeitschrift').agg({'Titel' : 'count', 'Land' : 'first', 'Zeitschriftkürzel' : 'first'}).reset_index()
grouped_df = grouped_df.rename(columns= {'Titel': 'Anzahl'})

print(grouped_df.head())

sorted_df = grouped_df.sort_values(by="Anzahl", ascending=False)

import plotly.express as px

fig = px.bar(
  sorted_df,
  x="Zeitschrift",
  y="Anzahl",
  color="Land",
  text="Zeitschriftkürzel",
  width=1000,
  height=800,
  hover_name= "Zeitschrift", 
  hover_data={
    'Zeitschriftkürzel': False,
    'Land': False,
    'Zeitschrift': False,
    'Anzahl': True
    })#category_values -> Länder sortieren?

fig.update_layout(
  title={
    'y':0.9,
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
  }
)
fig.show()