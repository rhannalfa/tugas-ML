# Laporan Praktikum Eksplorasi & Visualisasi Data

---

## 🚀 Tugas 1: Visualisasi Dataset Contoh (`tips.csv`)

Pada tugas ini, dilakukan analisis terhadap dataset restoran untuk melihat persebaran jenis kelamin pelanggan dan total pendapatan harian.

### 📊 Hasil Visualisasi & Insight

**1. Persebaran Jenis Kelamin Pengunjung**
Grafik ini menunjukkan perbandingan jumlah pelanggan laki-laki (Male) dan perempuan (Female) yang datang ke restoran.

<img width="640" height="480" alt="gender_tips" src="https://github.com/user-attachments/assets/cfc91f03-f710-4417-a26f-069747a621bb" />

**2. Total Pendapatan per Hari Berdasarkan Jenis Kelamin**
Grafik ini membandingkan total tagihan (pendapatan) yang dihasilkan pada hari-hari tertentu, dipisahkan berdasarkan jenis kelamin pelanggan yang membayar tagihan.

<img width="640" height="504" alt="pendapatan_tips" src="https://github.com/user-attachments/assets/96b59b32-8234-4cbb-baa4-75157e58b8e6" />

---

## 🚀 Tugas 2: Eksplorasi Data Emosi Komentar (`data_train.csv`)

Sesuai instruksi tugas lanjutan, dilakukan analisis terhadap dataset lain untuk mencari *insight* baru. Dataset yang digunakan adalah `data_train.csv`, yang berisi kumpulan komentar netizen dengan label emosi (Natural Language Processing dataset).

### 🖥️ Implementasi Kode & Hasil Grafik

Berikut adalah cuplikan kode Python di VS Code beserta hasil visualisasi *Vertical Bar Chart* untuk dataset emosi.

<img width="645" height="554" alt="image" src="https://github.com/user-attachments/assets/fdca19c1-c1f3-45c9-adb8-7f2e7062d08d" />

### 💡 Insight (Wawasan) dari Data Emosi

Berdasarkan grafik batang vertical di atas, didapatkan informasi menarik sebagai berikut:

1. **Dominasi Emosi Negatif yang Masif:** Mayoritas netizen memberikan respons yang sangat negatif terhadap isu yang dibahas. Emosi **Disgust (Muak/Jijik)** mendominasi secara absolut dengan total **2.260 komentar**, jauh melampaui kategori lainnya. Diikuti oleh **Anger (Marah)** sebanyak **523 komentar**.
2. **Solidaritas/Sensitivitas Publik:** Isu ini sangat memicu emosi audiens, terlihat dari minimnya reaksi **Neutral** (239) dan **Sadness** (128). Hal ini menunjukkan adanya solidaritas negatif atau sensitivitas publik yang tinggi yang tidak menyisakan banyak ruang untuk sikap netral.
3. **Munculnya Kategori 'Fear':** Meskipun dalam jumlah yang sangat kecil (6 komentar), munculnya emosi **Fear (Takut)** menunjukkan adanya sedikit kekhawatiran dari segelintir netizen terhadap dampak dari kasus tersebut (misalnya dampak hukum atau gesekan sosial).

---

## 💻 Cara Menjalankan Proyek

1. Pastikan Python sudah terinstal di komputer.
2. Instal library yang dibutuhkan:
   ```bash
   pip install pandas matplotlib
