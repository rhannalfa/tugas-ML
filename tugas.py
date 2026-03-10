import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')

gender_counts = df['sex'].value_counts()

print(gender_counts)

plt.bar(gender_counts.index, gender_counts.values, color=['skyblue', 'lightpink'])

plt.title('Persebaran Jenis Kelamin pada Dataset Tips')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Jumlah Pengunjung')

plt.show()