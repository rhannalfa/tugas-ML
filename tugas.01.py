import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')

pendapatan = df.groupby(['day', 'sex'])['total_bill'].sum().unstack()

print("Total Pendapatan per Hari berdasarkan Gender:")
print(pendapatan)

pendapatan.plot(kind='bar', color=['lightpink', 'skyblue'], edgecolor='black', width=0.7)

plt.title('Total Pendapatan per Hari Berdasarkan Jenis Kelamin')
plt.xlabel('Hari')
plt.ylabel('Total Pendapatan ($)')
plt.legend(title='Jenis Kelamin')
plt.xticks(rotation=0) # Agar teks nama hari di sumbu X tidak miring

plt.show()