# notebooks/eda.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')

# Dynamically construct the path to the dataset
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_path = os.path.join(base_path, 'data', 'student-mat.csv')

# Load dataset
df = pd.read_csv(data_path, sep=';')
print("✅ Data loaded successfully")

# Show first few rows
print("\n📄 First 5 rows:")
print(df.head())

# Basic info
print("\n🔎 Dataset Info:")
print(df.info())

# Summary stats
print("\n📊 Summary Statistics:")
print(df.describe())

# Check for missing values
print("\n❓ Missing Values:")
print(df.isnull().sum())

# Identify non-numeric columns
non_numeric = df.select_dtypes(exclude='number').columns.tolist()
print("\n🧾 Non-numeric columns:", non_numeric)

# -----------------------------
# 🔍 Visualizations
# -----------------------------

# 1. Final grade distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['G3'], bins=20, kde=True, color='skyblue')
plt.title("Distribution of Final Grades (G3)")
plt.xlabel("Final Grade")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 2. Correlation heatmap (numeric features only)
numeric_df = df.select_dtypes(include='number')

plt.figure(figsize=(12, 10))
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap (Numeric Features Only)")
plt.tight_layout()
plt.show()

# 3. G1 vs G3 scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='G1', y='G3', color='orange')
plt.title("G1 (Term 1 Grade) vs G3 (Final Grade)")
plt.xlabel("G1")
plt.ylabel("G3")
plt.tight_layout()
plt.show()

# 4. Study time vs final grade (boxplot)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='studytime', y='G3', palette='Set2')
plt.title("Study Time vs Final Grade (G3)")
plt.xlabel("Study Time (1-4)")
plt.ylabel("Final Grade")
plt.tight_layout()
plt.show()

# 5. Failures count
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='failures', palette='pastel')
plt.title("Number of Past Failures")
plt.xlabel("Failures")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 6. Pairplot for select numeric features
selected_features = ['G1', 'G2', 'G3', 'studytime', 'failures']
sns.pairplot(df[selected_features])
plt.suptitle("Pairplot of Selected Features", y=1.02)
plt.tight_layout()
plt.show()
