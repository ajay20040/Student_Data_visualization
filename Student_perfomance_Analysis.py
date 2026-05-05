import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("student_data_modified (1).csv")

print(df.head())



# Bar Chart → Marks per StudentID

plt.figure()
plt.bar(df['StudentID'], df['Marks'])
plt.title("Marks of Students")
plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.show()



# Line Chart → Marks trend
#
plt.figure()
plt.plot(df['StudentID'], df['Marks'], marker='o')
plt.title("Marks Trend")
plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.show()



# Pie Chart → Pass vs Fail

df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

result_counts = df['Result'].value_counts()

plt.figure()
plt.pie(result_counts, labels=result_counts.index, autopct='%1.1f%%')
plt.title("Pass vs Fail")
plt.show()