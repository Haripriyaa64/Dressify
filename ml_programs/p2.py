import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.datasets import fetch_california_housing 
# Fetch the California Housing dataset 
california_housing = fetch_california_housing() 
data = pd.DataFrame(california_housing.data, columns=california_housing.feature_names) 
# Compute the correlation matrix 
correlation_matrix = data.corr() 
# Visualize the correlation matrix using a heatmap 
plt.figure(figsize=(10, 8)) 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5) 
plt.title('Correlation Matrix Heatmap - Haripriya') 
plt.show() 
# Create a pair plot to visualize pairwise relationships between features 
sns.pairplot(data) 
plt.suptitle('Pair Plot of California Housing Features - Haripriya ', y=1.02) 
plt.show() 