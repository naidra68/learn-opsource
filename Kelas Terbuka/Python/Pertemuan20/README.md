# Pertemuan20 - Latihan Date and Time (Python Tutorial)

Sekarang, kita akan mencoba latihan senderhana dengan date and time.

Untuk menggunakan date and time, pertama kita perlu mengimport nya terlebih dahulu dari library python dengan cara sebagai berikut :

```python
import datetime as dt
```

Maksud dari kode tersebut adalah import datetime (dari library python) sebagai dt (ini adalah variabel untuk menampung import datetime tadi).

Untuk membuat Tanggal, bulan, dan Tahun sekarang ini, cukup menambahkan kode sederhana sebagai berikut :

```python
import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"hari ini adalah hari = {hari_ini:%A}")
```

Kite perlu menambahkan `:%A` untuk menampilkan tulisan hari ini. Kita juga dapat melakukan pengisian tanggal,bulan dan tahun pada kode tersebut. Berikut contoh penerapannya :

```python
import datetime as dt

tanggal = dt.date(2005,10,10)
print(tanggal)
print(f"hari ini adalah hari = {tanggal:%A}")
```

Terdapat perbedaan yang cukup terlihat dimana jika kita mencoba mengetahui date and time sekarang maka kita perlu menambahkan `today()`, namun jika kita ingin memasukkan date and time kita sendiri maka cukup menggunakan `date` dan di isi parameter-nya.

Sekarang perhatikan kode berikut :

```python
import datetime as dt

print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"hari nya adalah : {tanggal_lahir:%A}")
print(f"umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
```

Kode diatas adalah untuk membuat tanggal,bulan, dan tahun dapat diketahui secara detail.

Sekarang, kita bedah satu persatu maksud dari kode diatas

```python
print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))
```

Pertama, kita buat terlebih dahulu input yang dapat user ketikkan tentang tanggal, bulan dan tahun-nya. Jangan lupa gunakan `int()` agar tidak terdapat string didalam-nya.

<hr/>

```python
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
```

Sekarang, kita satukan semua input menjadi satu yaitu dimulai dari tahun,bulan dan tanggal. 

<hr/>

```python
hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"hari nya adalah : {tanggal_lahir:%A}")
print(f"umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
```

Kode terakhir ini adalah untuk mencari umur hari, bulan dan tahun-nya. Kita buat dulu variabel hari ini karena data nya nanti akan berpatokan pada waktu yang sekarang.

Untuk menentukan hari-nya maka kita perlu mengurangi data inputan tadi dengan data waktu sekarang. Maka dari itu kita perlu `umur_hari = hari_ini - tanggal_lahir`. Setelah itu, untuk menghitung tahun, kita perlu membagi umur hari dengan tahunan yang dijadikan harian yaitu 365 hari.

Untuk menghitung bulan, kita perlu umur hari dimodulus 365 hari lalu dibagi dengan 30 (1 bulan dalam bentuk hari).

<hr/>

Kode berikut ini merupakan hasil dari latihan membuat data diri sendiri. Bisa dipelajari

```python
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
```