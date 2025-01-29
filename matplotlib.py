import pandas as pd

# Load the dataset
try:
    # Replace 'iris.csv' with the path to your dataset
    df = pd.read_csv('iris.csv')
    
    # Display the first few rows of the dataset
    print(df.head())
    
    # Check the structure of the dataset (data types and missing values)
    print(df.info())
    print(df.isnull().sum())
    
    # Handle missing values: Drop rows with missing data (or fill them)
    df_cleaned = df.dropna()  # Alternatively: df.fillna(df.mean()) for numeric columns
    print(df_cleaned.info())
except FileNotFoundError:
    print("Error: The dataset file was not found.")


# Basic statistics of numerical columns
print(df_cleaned.describe())

# Group by a categorical column (e.g., 'species') and compute the mean of 'sepal_length'
grouped = df_cleaned.groupby('species')['sepal_length'].mean()
print(grouped)

import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# 1. Line chart (Assume dataset has a 'date' column for time-series analysis)
# plt.title("Sales Trends Over Time")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.show()

# 2. Bar chart (e.g., average petal length per species)
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=df_cleaned)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (e.g., distribution of sepal length)
plt.figure(figsize=(8, 6))
sns.histplot(df_cleaned['sepal_length'], kde=True, color='blue')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (e.g., sepal length vs. petal length)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', data=df_cleaned)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
