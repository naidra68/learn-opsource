# Pertemuan35 - Looping List dan Enumerate (Python Tutorial)

Sekarang, kita akan mencoba looping list dan enumerate. Dimana data list akan kita looping untuk mendapatkan data list yang enak dilihat dan rapi juga.

## for loop

Pertama, kita coba dulu dengan menggunakan for loop. Berikut contoh penerapan-nya.

```python
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")
```

Sekarang, kita coba gunakan data list nama.

```python
peserta  = ["ucup","otong","dadang","diding","dudung"]

for nama in peserta:
    print(f"nama = {nama}")
```

## for loop and range

Sekarang, kita coba for loop lagi namun dengan menggunakan range. Berikut contoh penerapan-nya.

```python
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")
```

Untuk for loop dan range, kita harus membuat panjang data list-nya terlebih dahulu menggunakan fungsi `len()`. Setelah itu kita bisa masukkan ke for dan kita tampilkan menggunakan `{kumpulan_angka[i]}`.

## while loop

Jika menggunakan while loop, ini akan sedikit lebih banyak daripada for loop. Kita akan mencobanya. Berikut contoh penerapan-nya.

```python
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
```

Masih sama seperti for loop dan range, kita perlu gunakan panjang data list nya, lalu kita definisikan `i = 0`. Kita lihat, apakah i kurang dari panjang, jika true maka dia akan ditampilkan. Lalu terakhir kita kasih increment `i += 1`.

## list comprehension

Ada cara lebih mudah,simple, dan sedikit yaitu menggunakan list comprehension. Berikut contoh penerapan-nya.

```python
data = ["ucup",1,2,3,"otong"]

[print(f"data = {i}") for i in data]
```

Hasilnya sama seperti cara pembuatan diatas. Kita perlu menambahkan kurung didepan print karena ini untuk menampung for nya dan print didalam untuk menampilkan hasilnya. Cukup simple kan.

Sekarang, kita coba sesuatu yang menarik menggunakan list comprehension ini yaitu membuat angka kuadrat. Berikut contoh penerapan-nya.

```python
angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)
```

jadi, kita bisa membuat list baru yang telah di kuadratkan.

## enumerate

Cara terakhir untuk membuat looping list adalah enumerate. Berikut contoh penerapan-nya.

```python
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
```

Dengan enumerate, kita bisa langsung tampilkan index dan data-nya secara langsung. Hal ini cukup berguna untuk mengetahui masing-masing data dan indexnya.