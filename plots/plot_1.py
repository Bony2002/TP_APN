import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data.csv")

df_04 = df[df['prob_entrar'] == 0.4]

df_filtro_sdc = df_04[df_04['horas'] == 7]

# Sin sdc
mean_normal_0 = np.array(eval(df_filtro_sdc["total_tiempos"][df_filtro_sdc.index[0]])).mean()
#mean_sdc_0 = np.array(eval(df_filtro_sdc["total_tiempos_sdc"][12])).mean()

# sdc 0.3
mean_normal_03 = np.array(eval(df_filtro_sdc["total_tiempos"][df_filtro_sdc.index[1]])).mean()
mean_sdc_03 = np.array(eval(df_filtro_sdc["total_tiempos_sdc"][df_filtro_sdc.index[1]])).mean()

# sdc 0.8
mean_normal_08 = np.array(eval(df_filtro_sdc["total_tiempos"][df_filtro_sdc.index[2]])).mean()
mean_sdc_08 = np.array(eval(df_filtro_sdc["total_tiempos_sdc"][df_filtro_sdc.index[2]])).mean()

# Assuming you've calculated the means as shown in your code

# Define the labels and values
labels = ['No SDC', 'SDC 0.3', 'SDC 0.8']
means_normal = [mean_normal_0, mean_normal_03, mean_normal_08]
means_sdc = [0, mean_sdc_03, mean_sdc_08]

# Set up the positions for the bars
x = np.arange(len(labels))

# Define the width of the bars
width = 0.35

# Create the bar plot with a larger figure size
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the width and height as needed
rects1 = ax.bar(x - width/2, means_normal, width, label='Normal')
rects2 = ax.bar(x + width/2, means_sdc, width, label='SDC')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_ylabel('Mean Value')
ax.set_title('Mean Values by SDC and No SDC in 7 hours of simulation with density 40%')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Add value labels on top of the bars
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5), textcoords='offset points',
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

# Save the plot
plt.savefig('mean_values_plot.png', dpi=300, bbox_inches='tight')

plt.show()


