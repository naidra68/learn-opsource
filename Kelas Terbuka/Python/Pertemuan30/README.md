# Pertemuan30 - Manipulasi List (Python Tutorial)

Sekarang, kita akan mencoba Manipulasi List agar dapat kita ubah data list-nya atau bisa kita otak-atik list-nya.

Perlu diperhatikan, list memiliki index pada masing-masing isi data-nya. Index tersebut dimulai dari index ke-0. Berikut contoh-nya.

```python
# index 0(-3)     1(-2)       2(-1)
data = ["Ucup","Otong","Dudung"]
```

Untuk kebalikan-nya, maka kita hanya perlu menulis -1,-2, dan -3. Karena untuk mengambil suatu data kita perlu index. Maka hal ini perlu diperhatikan dan dipahami.

## Ambil Data

Sekarang, kita akan mencoba mengambil data pada list. Untuk mengambil data, kita perlu mengatahui index ke berapa yang akan kita ambil data-nya. Seperti contoh, kita ingin mengambil data pada index ke-0, maka kita tulis saja `data[0]`. Berikut contoh penerapan-nya.

```python
data = ["Ucup","Otong","Dudung"]

data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")
```

Untuk mengambil data terakhir, kita bisa memanfaatkan nilai minus. Anggaplah, data kita itu banyak dan kita ingin mengambil data terakhir, namun index-nya sudah terlalu banyak.Kita hanya perlu mengetik `data[-1]`. Secara otomatis dia akan mengambil data terakhir. Berikut contoh penerapan-nya

```python
data = ["Ucup","Otong","Dudung"]

data_terakhir = data[-1]
print(f"data terakhir adalh = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")
```

## Jumlah Data

Kita bisa melihat berapa banyak data pada list dengan menggunakan fungsi `len()`. Berikut contoh penerapan-nya.

```python
panjang_data = len(data)
print(f"panjang data = {panjang_data}")
```

<hr/>

Sekarang, kita akan memasuki materi manipulasi data list. Dimana kita dapat melakukan apapun kepada data list-nya.

## Tambah Data Sesuai Posisi

Kita bisa menambahkan data pada list sesuai posisi yang kita inginkan. Sebagai contoh, kita ingin menambahkan data lagi setelah index ke-1. Maka itu bisa dilakukan dengan mudah menggunakan fungsi `insert()`. Berikut contoh penerapan-nya.

```python
print(f"data sebelum ditambah = \n{data}")
data.insert(1,"Asep")
print(f"data sesudah ditambah = \n{data}")
```

## Tambah Data Akhir Posisi

Kita juga bisa menambahkan data pada akhir posisi dengan menggunakan fungsi `append()`. Berikut contoh penerapan-nya.

```python
data.append("Jajang")
print(f"data ditambah lagi = \n{data}")
```

## Menggabungkan List

Kita bisa menggabungkan dari list satu ke list yang lain. Caranya gampang, kita perlu fungsi `extend()` untuk melakukan hal itu. Berikut contoh penerapan-nya.

```python
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n {data}")
```

## Ubah Data

Sekarang, kita akan mencoba mengubah data pada list. Sebagai contoh, kita ingin mengubah data index ke-2 menjadi Michael. Berikut contoh penerapan-nya.

```python
data[2] = "Michael"
print(f"data rubah = {data}")
```

## Hapus Data

Untuk menghapus data, kita perlu menggunakan fungsi `remove()`. Kita tulis saja nama data-nya untuk dihapus. Berikut contoh penerapan-nya.

```python
data.remove("Ujang")
print(f"data hapus = {data}")
```

Selain itu, kita juga dapat menghapus data akhir. Gunakan fungsi `pop()` untuk menghapus data terakhir. Tidak perlu ditulis argumen didalam fungsi tersebut karena secara otomatis data yang dihapus adalah data terakhir, mau sepanjang apapun data tersebut. Berikut contoh penerapan-nya.

```python
data.pop()
print(f"data akhir = \n{data}")
```