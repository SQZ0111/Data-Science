import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Quelle: https://lfu.brandenburg.de/cms/detail.php/bb1.c.523833.de
# Landesamt für Umwelt Brandenburg
palette = sns.color_palette("coolwarm", n_colors=6)

# Custom Palette
flatui = ["#527BAB", "#164278" , "#81DCDE", "#F7BC8D" , "#E67350", "#AB5A52"]
palette = sns.color_palette(flatui)

energy_sources = pd.Series(["Steinkohle", "Braunkohle", "Rohbraunkohle", "Benzin", "Kerosin", "Heizöl L / Diesel", "Erdgas"])
values = pd.Series([0.335, 0.364, 0.407, 0.259, 0.266, 0.266, 0.202])
values = values * 1000
# Einheit: g/kWh
df = pd.DataFrame({"Energieträger": energy_sources, "Werte": values})
df = df.sort_values(['Werte'], ascending = False).reset_index(drop=True)
print(df)

barplt = sns.barplot(x = "Energieträger", y = "Werte", data = df, palette=palette)
barplt.set(ylabel = "g CO_2 / kWh")
barplt.set_title("Wie viel CO2 emittieren ausgewählte Energieträger im Vergleich?")
barplt.set_xticklabels(barplt.get_xticklabels(), rotation=25)
plt.show()
