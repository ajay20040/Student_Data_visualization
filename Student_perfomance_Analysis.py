import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("student_data_modified (1).csv")

print(df.head())


# 1. HISTOGRAM - Distribution of Marks
plt.figure(figsize=(8, 5))
plt.hist(df['Marks'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram - Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.show()


# 2. COLUMN CHART - Marks per Student
plt.figure(figsize=(10, 5))
plt.bar(df['StudentID'], df['Marks'], color='orange', edgecolor='black')
plt.title("Column Chart - Marks Per Student")
plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.grid(axis='y', alpha=0.3)
plt.show()


# 3. SCATTER PLOT - Study Hours vs Marks
plt.figure(figsize=(8, 5))
plt.scatter(df['StudyHours'], df['Marks'], color='green', s=100, alpha=0.6)
plt.title("Scatter Plot - Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(alpha=0.3)
plt.show()