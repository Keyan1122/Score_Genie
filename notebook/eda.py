# notebooks/eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/student-mat.csv")

# Display first few rows
print("First 5 rows:")
print(df.head())

# Basic info about dataset
print("\nDataframe Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values per Column:")
print(df.isnull().sum())

# Distribution of final grades (G3)
plt.figure(figsize=(8, 5))
sns.histplot(df['G3'], bins=20, kde=True)
plt.title("Distribution of Final Grades (G3)")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Frequency")
plt.show()

# Correlation heatmap between numeric features
plt.figure(figsize=(12, 10))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Scatter plot of G1 vs G3 (Term 1 vs Final Grade)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='G1', y='G3', data=df)
plt.title("G1 (Term 1 Grade) vs G3 (Final Grade)")
plt.xlabel("G1")
plt.ylabel("G3")
plt.show()

# Box plot of studytime vs final grade
plt.figure(figsize=(8, 5))
sns.boxplot(x='studytime', y='G3', data=df)
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time (hours)")
plt.ylabel("Final Grade (G3)")
plt.show()

# Count plot for failures (how many students had past failures)
plt.figure(figsize=(6, 4))
sns.countplot(x='failures', data=df)
plt.title("Number of Past Failures")
plt.xlabel("Failures")
plt.ylabel("Count")
plt.show()

# Pairplot for selected numeric features to see relationships
sns.pairplot(df[['G1', 'G2', 'G3', 'studytime', 'failures']])
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()
