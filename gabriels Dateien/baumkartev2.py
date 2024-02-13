import pandas as pd
import matplotlib.pyplot as plt
import squarify
import matplotlib.patheffects as path_effects
from matplotlib.widgets import Button

# Daten einlesen
data = pd.read_csv("Baumkarte_Datensatz.csv")

check = 0

# Funktion für die Interaktion mit dem Diagramm
def on_click(event):
    global zeitschrift_titel_count, zeitschrift_namen, zeitschrift_farben, check
    
    if check == 0:
        # Überprüfe, ob der Mausklick innerhalb der Koordinaten von "Deutschland" liegt
        if 0 <= event.xdata <= 73 and 0 <= event.ydata <= 100:
            # Filtern der Daten für Zeitschriften aus Deutschland
            land_data = data[data['Land'] == 'Deutschland']
        
            zeitschrift_farben = ['blue']
        elif 73 < event.xdata <= 100 and 43 <= event.ydata <=100:
            # Filtern der Daten für Zeitschriften aus Deutschland
            land_data = data[data['Land'] == 'Österreich']
        
            zeitschrift_farben = ['red']    
        elif 73 < event.xdata <= 100 and 28 <= event.ydata < 43:
            # Filtern der Daten für Zeitschriften aus Deutschland
            land_data = data[data['Land'] == 'Schweiz']
        
            zeitschrift_farben = ['orange']    
        elif 73 < event.xdata <= 100 and 14 <= event.ydata < 28:
            # Filtern der Daten für Zeitschriften aus Deutschland
            land_data = data[data['Land'] == 'Niederlande']
        
            zeitschrift_farben = ['violet']    
        elif 73 < event.xdata <= 100 and 0 <= event.ydata < 14:
            # Filtern der Daten für Zeitschriften aus Deutschland
            land_data = data[data['Land'] == 'Liechtenstein']
        
            zeitschrift_farben = ['green']
                                  
        # Gruppieren nach Zeitschrift und Titel und Zählen 
        zeitschrift_titel_count = land_data.groupby('Zeitschrift')['Titel'].nunique()
        
        zeitschrift_namen = list(zeitschrift_titel_count.index) 
        
        check = 1   
        
        show_land_tree_map()    
         
# Button zum Zurückkehren zur Gesamt-Baumkarte hinzufügen
ax_back = plt.axes([0.01, 0.97, 0.2, 0.03])  # [left, bottom, width, height]
button_back = Button(ax_back, 'Zurück zur Länderkarte')
button_back.on_clicked(lambda _: show_total_tree_map())

def show_land_tree_map():
    plt.clf()  # Lösche den aktuellen Plot
    plt.title('Zeitschriften (Größe nach Artikeln)')
    squarify.plot(sizes=zeitschrift_titel_count.values, label=zeitschrift_namen, color=zeitschrift_farben, pad=2, text_kwargs={'color':'black', 'fontsize':10, 'weight':'bold', 'wrap':True})
    for label in plt.gca().texts:
        label.set_path_effects([path_effects.Stroke(linewidth=3, foreground='white'), path_effects.Normal()])
    plt.axis("off")
    plt.tight_layout()
    plt.draw()  # Aktualisiere die Visualisierung
    plt.show()

# Funktion zum Anzeigen der Gesamt-Baumkarte
def show_total_tree_map():
    global land_zeitschrift_count, land_namen, land_farben, check
    
    # Gruppieren nach Land und Zeitschrift und Zählen 
    land_zeitschrift_count = data.groupby('Land')['Zeitschrift'].nunique()

    # Die Namen der Länder und Zeitschriften in separaten Arrays speichern
    land_namen = list(land_zeitschrift_count.index)

    # Farben für die Länder und Zeitschriften festlegen
    land_farben = ['blue', 'green', 'violet', 'orange', 'red']

    plt.clf()  # Lösche den aktuellen Plot
    plt.title('Verteilung der Zeitschriften nach Ländern')
    squarify.plot(sizes=land_zeitschrift_count.values, label=land_namen, color=land_farben, pad=2, text_kwargs={'color':'black', 'fontsize':10, 'weight':'bold', 'wrap':True})
    for label in plt.gca().texts:
        label.set_path_effects([path_effects.Stroke(linewidth=3, foreground='white'), path_effects.Normal()])
    plt.axis("off")
    plt.tight_layout()
    plt.draw()  # Aktualisiere die Visualisierung
    plt.show()
    check = 0

# Ereignishandler für Mausklick hinzufügen
plt.gcf().canvas.mpl_connect('button_press_event', on_click)

# Die Gesamt-Baumkarte anzeigen
show_total_tree_map()

