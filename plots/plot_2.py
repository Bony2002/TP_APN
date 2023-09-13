import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data_tiempo.csv")

# Sin sdc
df_00 = df[df['prob_entrar'] == 0.2]
choque_normal_00 = 0
for i in range(df_00.shape[0]):
    for choque in eval(df_00["datos_choques"][df_00.index[i]]):
        max_velocity = max(choque[4],choque[1])
        if max_velocity > 8:
            if (choque[2]!="SDC" and choque[1]==max_velocity) or (choque[6]!="SDC" and choque[4]==max_velocity) :
                choque_normal_00+=1
mean_choque_normal_00 = choque_normal_00/df_00.shape[0]

# sdc 0.3
choque_normal_03 = 0
#choque_sdc_03 = 0
df_03 = df[df['prob_entrar'] == 0.4]
for i in range(df_03.shape[0]):
    for choque in eval(df_03["datos_choques"][df_03.index[i]]):
        max_velocity = max(choque[4],choque[1])
        if max_velocity > 8:
            if (choque[2]!="SDC" and choque[1]==max_velocity) or (choque[6]!="SDC" and choque[4]==max_velocity) :
                choque_normal_03+=1
    # for choque in eval(df_03["total_choques_sdc"][df_03.index[i]]):
    #     max_velocity = max(choque[4],choque[1])
    #     if max_velocity > 8:
    #         if (choque[2]=="SDC" and choque[1]==max_velocity) or (choque[6]=="SDC" and choque[4]==max_velocity) :
    #             choque_sdc_03+=1
mean_choque_normal_03 = choque_normal_03/df_03.shape[0]
#mean_choque_sdc_03 = choque_sdc_03/df_03.shape[0]

# sdc 0.8
choque_normal_08 = 0
#choque_sdc_08 = 0
df_08 = df[df['prob_entrar'] == 0.6]
for i in range(df_08.shape[0]):
    for choque in eval(df_08["datos_choques"][df_08.index[i]]):
        max_velocity = max(choque[4],choque[1])
        if max_velocity > 8:
            if (choque[2]!="SDC" and choque[1]==max_velocity) or (choque[6]!="SDC" and choque[4]==max_velocity) :
                choque_normal_08+=1
    # for choque in eval(df_08["total_choques_sdc"][df_08.index[i]]):
    #     max_velocity = max(choque[4],choque[1])
    #     if max_velocity > 8:
    #         if (choque[2]=="SDC" and choque[1]==max_velocity) or (choque[6]=="SDC" and choque[4]==max_velocity) :
    #             choque_sdc_08+=1
mean_choque_normal_08 = choque_normal_08/df_08.shape[0]
# mean_choque_sdc_08 = choque_sdc_08/df_08.shape[0]


# Assuming you've calculated the collision counts as shown in your code

# Define the labels and values
labels = ['No SDC', 'SDC 0.3', 'SDC 0.8']
collision_counts_normal = [mean_choque_normal_00, mean_choque_normal_03, mean_choque_normal_08]
# collision_counts_sdc = [0, mean_choque_sdc_03, mean_choque_sdc_08]  # Assuming you want to include a bar for SDC 0.0 with value 0

# Set up the positions for the bars
x = range(len(labels))

# Define the width of the bars
width = 0.35

# Create the bar plot
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x, collision_counts_normal, width, label='Normal')
#rects2 = ax.bar([p + width for p in x], collision_counts_sdc, width, label='SDC')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Collisions')
ax.set_title('Mean Number of Collisions in 3 Hours with Density 40%')
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
#add_labels(rects2)

plt.text(0.5, 0.9, 'The colllisions shown happen at velocity > 8', horizontalalignment='center', fontsize=10, transform=ax.transAxes)

plt.savefig('mean_choques_plot_normal.png', dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()
