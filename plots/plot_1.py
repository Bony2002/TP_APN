import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data_sdc.csv")

# Sin sdc
df_00 = df[df['prop_sdc'] == 0]
tiempo_normal_00 = 0
for i in range(df_00.shape[0]):
    tiempo_normal_00 += np.array(eval(df_00["total_tiempos"][df_00.index[i]])).mean()
mean_tiempo_normal_00 = tiempo_normal_00/df_00.shape[0]

# sdc 0.3
tiempo_normal_03 = 0
tiempo_sdc_03 = 0
df_03 = df[df['prop_sdc'] == 0.3]
for i in range(df_03.shape[0]):
    tiempo_normal_03 += np.array(eval(df_03["total_tiempos"][df_03.index[i]])).mean()
    tiempo_sdc_03 += np.array(eval(df_03["total_tiempos_sdc"][df_03.index[i]])).mean()
mean_tiempo_normal_03 = tiempo_normal_03/df_03.shape[0]
mean_tiempo_sdc_03 = tiempo_sdc_03/df_03.shape[0]

# sdc 0.8
tiempo_normal_08 = 0
tiempo_sdc_08 = 0
df_08 = df[df['prop_sdc'] == 0.8]
for i in range(df_08.shape[0]):
    tiempo_normal_08 += np.array(eval(df_08["total_tiempos"][df_08.index[i]])).mean()
    tiempo_sdc_08 += np.array(eval(df_08["total_tiempos_sdc"][df_08.index[i]])).mean()
mean_tiempo_normal_08 = tiempo_normal_08/df_08.shape[0]
mean_tiempo_sdc_08 = tiempo_sdc_08/df_08.shape[0]

# Assuming you've calculated the means as shown in your code

# Define the labels and values
labels = ['No SDC', 'SDC 0.3', 'SDC 0.8']
means_normal = [mean_tiempo_normal_00, mean_tiempo_normal_03, mean_tiempo_normal_08]
means_sdc = [0, mean_tiempo_sdc_03, mean_tiempo_sdc_08]

# Set up the positions for the bars
x = np.arange(len(labels))

# Define the width of the bars
width = 0.35

# Create the bar plot with a larger figure size
fig, ax = plt.subplots(figsize=(12, 10))  # Adjust the width and height as needed
rects1 = ax.bar(x - width/2, means_normal, width, label='Normal')
rects2 = ax.bar(x + width/2, means_sdc, width, label='SDC')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_ylabel('Mean Value')
ax.set_title('Mean Values by SDC and No SDC in 3 Hours simulation with density 40%')
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


