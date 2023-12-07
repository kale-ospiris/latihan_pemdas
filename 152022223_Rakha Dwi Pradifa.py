import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
df_peningkatan_gaji=pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
peningkatan_gaji=0.05
for index, row in df_peningkatan_gaji.iterrows():
    lambdas=lambda x:row['Gaji']+peningkatan_gaji*row['Gaji']
    df_peningkatan_gaji.at[index, 'Peningkatan gaji']=lambdas(0)
print("\nPertanyaan 1:")
print(df_peningkatan_gaji)

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("\nPertanyaan 2:")
print(df_peningkatan_gaji)

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
peningkatan_gaji_tambahan = 0.02
for index, row in df_peningkatan_gaji.iterrows():
    if row['Usia']>30:
        lambdas_tambahan=lambda x:x+peningkatan_gaji_tambahan*x
        df_peningkatan_gaji.at[index, 'Peningkatan gaji']=lambdas_tambahan(row['Peningkatan gaji'])
    else:
        df_peningkatan_gaji.at[index, 'Peningkatan gaji']
print("\nPertanyaan 3:") 
print(df_peningkatan_gaji)

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("\nPertanyaan 4:")
print(df_peningkatan_gaji)

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://gitlab.com/itenas/tugas_pemdas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.