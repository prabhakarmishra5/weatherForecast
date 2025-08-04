import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
df = pd.read_csv('weather_forcast_20250804.csv');
print(df.head());  # First 5 rows
print(df.info());  # Summary of the DataFrame
print(df.describe());  # Statistical summary
print(df.values[0,0]);

# Compute correlation for all columns
#correlation_matrix = df.corr()
#print(correlation_matrix)