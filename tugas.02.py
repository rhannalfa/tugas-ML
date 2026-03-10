import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_train.csv')

jumlah_emosi = df['Label_Emosi'].value_counts()

print("Jumlah masing-masing emosi pada Data Latih (Train):")
print(jumlah_emosi)

warna = ['crimson', 'orange', 'gray', 'royalblue', 'purple']
plt.barh(jumlah_emosi.index[::-1], jumlah_emosi.values[::-1], color=warna[::-1], edgecolor='black')

plt.title('Proporsi Emosi Netizen pada Data Latih (Train Data)')
plt.xlabel('Jumlah Komentar')
plt.ylabel('Kategori Emosi')

for index, value in enumerate(jumlah_emosi.values[::-1]):
    plt.text(value + 20, index, str(value), va='center', fontweight='bold')

plt.show()