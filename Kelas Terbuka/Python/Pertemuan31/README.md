# Pertemuan31 - Operasi List (Python Tutorial)

Pada pertemuan kali ini, kita akan mencoba mengenai operasi list. Apa saja yang ada pada operasi list akan kita coba dan kita praktekkan.

## Hitung Data

Untuk menghitung suatu data pada list, kita perlu fungsi `count()` pada sebuah data list. Sebagai contoh, kita buat terlebih dahulu data list number secara acak. Berikut contoh-nya.

```python
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
```

Setelah itu, kita langsung eksekusi dan hitung data-nya. Berikut contoh penerapan-nya.

```python
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")
```

## Ambil Posisi Data (Index)

Kita bisa mengambil posisi data index-nya dengan cara memasukkan isi data-nya. Nanti-nya data tersebut akan diketahui berada di index ke berapa. Berikut contoh penerapan-nya.

```python
data = ["Ucup","Otong","Dudung","Ujang"]

print(f"data = {data}")

index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"index si Dudung = {index_dudung}")
print(f"index si Ujang = {index_ujang}")
```

## Mengurutkan Data List

Ini merupakan sesuatu yang menarik karena kita akan mencoba mengurutkan posisi data list. Data kita sebelumnya merupakan angka yang tidak beraturan dan urut sesuai nomer. Kita bisa mengurutkan-nya menggunakan fungsi yang bernama `sort()`. Berikut contoh penerapan-nya.

```python
print(f"data angka sebelum sort = \n{data_angka}")

data_angka.sort()
print(f"data angka setelah sort = \n{data_angka}")
```

Selain data list angka, kita juga bisa mengurutkan data list string. Nantinya urutan data list string akan dilihat dari abjad nya. Berikut contoh penerapan-nya.

```python
print(f"data = {data}")
data.sort()
print(f"data sort = {data}")
```

## Membalikkan Data List

Untuk membalikkan sebuah data list, kita perlu sorting data-nya terlebih dahulu. Sebelum-nya kita telah sorting/mengurutkan data nya diatas. Sekarang kita perlu fungsi `reverse()` untuk membalikkan data list. Berikut contoh penerapan-nya.

```python
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")
```