import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data.csv")

df_04 = df[df['prob_entrar'] == 0.6]

df_filtro_sdc = df_04[df_04['horas'] == 7]

# Sin sdc
choque_normal_0 = len(eval(df_filtro_sdc["datos_choques"][df_filtro_sdc.index[0]]))
print(choque_normal_0)

# sdc 0.3
choque_normal_03 = len(eval(df_filtro_sdc["datos_choques"][df_filtro_sdc.index[1]]))
choque_sdc_03 = len(eval(df_filtro_sdc["total_choques_sdc"][df_filtro_sdc.index[1]]))

# sdc 0.8
choque_normal_08 = len(eval(df_filtro_sdc["datos_choques"][df_filtro_sdc.index[2]]))
choque_sdc_08 = len(eval(df_filtro_sdc["total_choques_sdc"][df_filtro_sdc.index[2]]))

# Define the labels and values
labels = ['No SDC', 'SDC 0.3', 'SDC 0.8']
collision_counts_normal = [choque_normal_0, choque_normal_03, choque_normal_08]
collision_counts_sdc = [0, choque_sdc_03, choque_sdc_08]  # Assuming you want to include a bar for SDC 0.0 with value 0

# Set up the positions for the bars
x = range(len(labels))

# Define the width of the bars
width = 0.35

# Create the bar plot
fig, ax = plt.subplots()
rects1 = ax.bar(x, collision_counts_normal, width, label='Normal')
rects2 = ax.bar([p + width for p in x], collision_counts_sdc, width, label='SDC')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Collisions')
ax.set_title('Number of Collisions by Scenario in 7 hours of simulation and density 0.6')
ax.set_xticks([p + width/2 for p in x])
ax.set_xticklabels(labels)
ax.legend()

# Add value labels on top of the bars
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

plt.savefig('collisions_plot.png', dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()