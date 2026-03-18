import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.datasets import fetch_california_housing 
# Fetch the California Housing dataset 
california_housing = fetch_california_housing(as_frame=True) 
data = california_housing.frame 
# Display the first few rows of the dataset 
print(data.head()) 
# Create histograms for all numerical features 
def create_histograms(data): 
    data.hist(bins=30, figsize=(20, 15)) 
    plt.suptitle('Histograms of Numerical Features - priya ', fontsize=20) 
    plt.show() 
# Create box plots for all numerical features 
def create_box_plots(data): 
    plt.figure(figsize=(20, 15)) 
    for i, column in enumerate(data.columns): 
      plt.subplot(3, 3, i + 1) 
      sns.boxplot(y=data[column]) 
      plt.title(f'Box Plot of {column}') 
      plt.suptitle('Box Plots of Numerical Features - priya ', fontsize=20) 
      plt.tight_layout(rect=[0, 0.03, 1, 0.95])
      plt.show() 
# Analyze the distribution and identify outliers 
def analyze_distribution(data): 
    for column in data.columns: 
        print (f'\nAnalyzing {column}:') 
        print(data[column].describe()) 
        q1 = data[column].quantile(0.25) 
        q3 = data[column].quantile(0.75) 
        iqr = q3 - q1 
        lower_bound = q1 - 1.5 * iqr 
        upper_bound = q3 + 1.5 * iqr 
        outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)] 
        print(f'Number of outliers in {column}: {len(outliers)}') 
# Execute the functions 
create_histograms(data) 
create_box_plots(data) 
analyze_distribution(data) 