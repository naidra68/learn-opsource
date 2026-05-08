# Date and time (latihan)

import datetime as dt

# hari_ini = dt.date.today()

# print(hari_ini)
# print(f"hari ini adalah hari = {hari_ini:%A}")

# tanggal = dt.date(2005,10,10)
# print(tanggal)
# print(f"hari ini adalah hari = {tanggal:%A}")

# print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
# tanggal = int(input("Tanggal \t:"))
# bulan = int(input("Bulan \t\t:"))
# tahun = int(input("Tahun \t\t:"))

# tanggal_lahir = dt.date(tahun,bulan,tanggal)
# print(f"tanggal lahir anda adalah : {tanggal_lahir}")

# hari_ini = dt.date.today()
# print(f"hari ini tanggal: {hari_ini}")
# umur_hari = hari_ini - tanggal_lahir
# umur_tahun = umur_hari.days // 365
# umur_bulan_sisa = (umur_hari.days % 365) // 30
# print(f"hari nya adalah : {tanggal_lahir:%A}")
# print(f"umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")

print(10*"="+" Aplikasi Data Diri "+10*"=")

nama = input("Masukkan nama anda :")
tempat_tinggal = input("Masukkan tempat tinggal anda :")
hobi = input("Masukkan hobi anda :")
tanggal = int(input("Masukkan Tanggal lahir anda :"))
bulan = int(input("Masukkan Bulan lahir anda :"))
tahun = int(input("Masukkan Tahun lahir anda :"))

print(5*"="+" Data Diri "+5*"=")
print(f"Nama : {nama}")
print(f"Tempat Tinggal : {tempat_tinggal}")
print(f"Hobi : {hobi}")

today = dt.date.today()
tbt = dt.date(tahun,bulan,tanggal)
umur_hari = today - tbt
umur_hari_ini = umur_hari.days
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
umur_menit = umur_hari.days * 24 * 60
print(f"TBT anda : {tbt}")
print(f"Anda lahir pada hari : {tbt:%A}")
print(f"Umur anda sekarang : {umur_tahun} Tahun")
print(f"Anda sudah hidup selama : {umur_tahun} Tahun, {umur_bulan} Bulan, {umur_hari_ini} Hari, {umur_menit} Menit")