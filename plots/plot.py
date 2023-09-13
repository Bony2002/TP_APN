import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data_tiempo.csv")
df_sin_sdc = df[df['sdc'] == False]

# Initialize arrays
total_tiempos_02 = np.array([])
total_tiempos_04 = np.array([])
total_tiempos_06 = np.array([])

# Extract and concatenate data
for i in range(df_sin_sdc.shape[0]):
    prob_entrar = df_sin_sdc.iloc[i]['prob_entrar']
    total_tiempos = np.array(eval(df_sin_sdc.iloc[i]['total_tiempos']))
    
    if prob_entrar == 0.2:
        total_tiempos_02 = np.concatenate((total_tiempos_02, total_tiempos))
    elif prob_entrar == 0.4:
        total_tiempos_04 = np.concatenate((total_tiempos_04, total_tiempos))
    elif prob_entrar == 0.6:
        total_tiempos_06 = np.concatenate((total_tiempos_06, total_tiempos))

# Create histograms
plt.figure(figsize=(15, 5))

# Create subplots with shared y-axis
plt.subplot(1, 3, 1)
plt.hist(total_tiempos_02, bins=10, edgecolor='k', alpha=0.7)
plt.xlabel('Total Tiempos')
plt.ylabel('Frequency')
plt.title('Probability of Entering: 0.2')
plt.ylim([0, 8000])  # Set y-axis limit

plt.subplot(1, 3, 2, sharey=plt.gca())
plt.hist(total_tiempos_04, bins=10, edgecolor='k', alpha=0.7)
plt.xlabel('Total Tiempos')
plt.title('Probability of Entering: 0.4')
plt.ylim([0, 8000])  # Set y-axis limit

plt.subplot(1, 3, 3, sharey=plt.gca())
plt.hist(total_tiempos_06, bins=10, edgecolor='k', alpha=0.7)
plt.xlabel('Total Tiempos')
plt.title('Probability of Entering: 0.6')
plt.ylim([0, 8000])  # Set y-axis limit

plt.savefig('total_tiempos.png', dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()
