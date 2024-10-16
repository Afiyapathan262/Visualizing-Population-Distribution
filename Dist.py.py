import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Reading CSV with low_memory=False to avoid dtype warning
df = pd.read_csv('C:\\Users\\Afiya\\Downloads\\archive\\ED.csv', low_memory=False)

# Plotting histogram for Age (continuous variable)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Plotting bar chart for Gender (categorical variable)
plt.subplot(1, 2, 2)
sns.countplot(x='Gender', data=df, palette='Set2')
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
