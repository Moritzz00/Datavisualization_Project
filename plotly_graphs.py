import pandas as pd
from jinja2 import Template

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

output_html_path = r"index.html"
input_template_path = r"template.html"

plotly_jinja_data = {"fig":fig.to_html(full_html=False)}

with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_template_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))


#fig.show()