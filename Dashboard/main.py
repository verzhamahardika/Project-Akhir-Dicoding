import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Pastikan dataset sudah ada, misalnya dataset.csv
dataset = pd.read_csv('day.csv')  # Gantilah dengan path dataset Anda

# Menampilkan title di dashboard
st.title("Dashboard Pemakaian Sepeda")

# Menampilkan visualisasi boxplot Distribusi Total Pemakaian Sepeda Berdasarkan Musim
st.subheader('Distribusi Total Pemakaian Sepeda Berdasarkan Musim')
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.boxplot(x='season', y='cnt', data=dataset, hue='season', palette='coolwarm', legend=False, ax=ax1)
ax1.set_title('Distribusi Total Pemakaian Sepeda Berdasarkan Musim')
ax1.set_xlabel('Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin)')
ax1.set_ylabel('Total Pemakaian Sepeda')
st.pyplot(fig1)

# Menampilkan visualisasi boxplot Pengaruh Hari Kerja terhadap Total Pemakaian Sepeda
st.subheader('Pengaruh Hari Kerja terhadap Total Pemakaian Sepeda')
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.boxplot(x='workingday', y='cnt', data=dataset, palette='Set3', ax=ax2)
ax2.set_title('Pengaruh Hari Kerja terhadap Total Pemakaian Sepeda')
ax2.set_xlabel('Hari Kerja (0: Tidak, 1: Ya)')
ax2.set_ylabel('Total Pemakaian Sepeda (cnt)')
st.pyplot(fig2)

# Menampilkan visualisasi Korelasi antara Suhu dan Total Pemakaian Sepeda
st.subheader('Korelasi antara Suhu dan Total Pemakaian Sepeda')
fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='temp', y='cnt', data=dataset, alpha=0.7, color='blue', ax=ax3)
sns.regplot(x='temp', y='cnt', data=dataset, scatter=False, color='red', line_kws={'label': 'Trend Line'}, ax=ax3)
ax3.set_title('Korelasi antara Suhu dan Total Pemakaian Sepeda')
ax3.set_xlabel('Suhu (temp)')
ax3.set_ylabel('Total Pemakaian Sepeda (cnt)')
ax3.legend()
st.pyplot(fig3)

# Menampilkan visualisasi Tren Rata-rata Pemakaian Sepeda per Bulan
st.subheader('Tren Rata-rata Pemakaian Sepeda per Bulan')
fig4, ax4 = plt.subplots(figsize=(10, 6))
monthly_avg = dataset.groupby('mnth')['cnt'].mean().reset_index()
sns.lineplot(x='mnth', y='cnt', data=monthly_avg, marker='o', color='green', ax=ax4)
ax4.set_title('Tren Rata-rata Pemakaian Sepeda per Bulan')
ax4.set_xlabel('Bulan (1-12)')
ax4.set_ylabel('Rata-rata Total Pemakaian Sepeda (cnt)')
ax4.set_xticks(range(1, 13))

# Menambahkan label pada setiap titik
for i in range(len(monthly_avg)):
    ax4.text(monthly_avg['mnth'][i], monthly_avg['cnt'][i], f"{monthly_avg['cnt'][i]:.0f}",
             color='black', ha='center', fontsize=10)

ax4.grid(True)
st.pyplot(fig4)
