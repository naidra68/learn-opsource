# Pertemuan32 - Copy List (Python Tutorial)

Kita akan mencoba mengenai Copy List. Sebelumnya, kita mungkin berpikir untuk copy sebuah list itu cukup mudah. tinggal buat list baru dengan variabel list lama. Berikut contoh-nya.

```python
a = ["Ucup","Otong","Dudung"]

print(f"a = {a}")

b = a
print(f"b = {b}")
```

Jika dilihat, memang tidak ada masalah mengenai hal itu. Terlihat oke dan normal saja. Namun, ada sesuatu yang harus kita ketahui bahwa cara diatas tidak di sarankan, karena jika kita berhubungan dengan list untuk mengambil, mengubah, dan menghapus, maka kita perlu bener-bener mengcopy-nya.

Sebelum itu, kita coba dulu ubah data pada list diatas. Berikut contoh-nya.

```python
a = ["Ucup","Otong","Dudung"]

b = a

a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")
```

Kodingan diatas, terlihat bahwa setiap kita ubah salah satu data-nya. Maka semua data tersebut akan berubah, baik di data a maupun data b. Mengapa hal tersebut bisa terjadi?

Jawabannya adalah address. Sekarang, kita coba cek address masing-masing data list tersebut. Berikut contoh-nya.

```python
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
```

Terlihat bahwa address dari kedua data tersebut ternyata sama. Jadi sistem-nya gini. Ketika kita membuat data baru dan mengambil data lain, maka dia akan mengambil data tersebut tanpa membuatnya dari awal. Jadi jika data awalnya diubah, maka data baru tersebut ikutan berubah.

Solusi untuk masalah ini adalah dengan menggunakan copy list. Kita hanya tambahkan fungsi `copy()` untuk salin data-nya dan membedakan address. Berikut contoh penerapan-nya.

```python
print("membuat list c dengan a.copy()")

c = a.copy()

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address b = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 0")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 1")
c[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
```