import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv('data/cleaned_data.csv')

# Plot delays by reason
sns.barplot(x='Reason', y='Delay (min)', data=df)
plt.title('Average Delay by Reason')
plt.show()

# Plot peak hour delays
sns.boxplot(x='is_peak_hour', y='Delay (min)', data=df)
plt.title('Delays During Peak and Non-Peak Hours')
plt.show()
