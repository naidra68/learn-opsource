# Pertemuan34 - Deep Copy Nested List (Python Tutorial)

Sekarang, kita akan membahas dan mencoba mengenai Deep Copy pada Nested List. Sebelumnya, kita lihat bahwa untuk mencopy nested list tidak bisa menggunakan `copy()` saja. 

Sebelum masuk ke deep copy, kita akan bahas terlebih dahulu mengapa kita perlu deep copy untuk nested list. Kita coba buat nested list dengan copy biasa.

```python
data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
```

Sekarang, kita telah mengcopy nested list yang telah kita buat diatas. Untuk mengambil data dari nested list, kita perlu perhatikan terlebih dahulu index-nya. Sebagai contoh, untuk mengambil nilai 1, maka kita perlu tau bahwa nilai 1 tersebut berada di index ke berapa dan didalam-nya itu juga index ke berapa. Untuk hal itu, kita bisa tuliskan index-nya 2x. Berikut contoh penerapan-nya.

```python
data = data_2D[0][0]
print(f"data = {data}")
```

Kode diatas akan menghasilkan nilai 1. Karena nilai 1 berada di index ke-0 pada `data_2D` dan index ke-0 juga pada `data_0`. Seperti itulah caranya.

Selanjutnya, kita akan melihat address pada nested list tersebut. Untuk mengetahui bagaimana bisa nested list jika dicopy biasa tetap berubah data-nya.

```python
print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")
```

Address dari masing-masing data asli dan copy terlihat berbeda bukan? Itu memang benar, namun tidak sebetul-nya benar. Karena yang berbeda hanyalah di permukaan-nya saja, namun untuk isi didalam-nya memiliki address yang sama. Kita coba lihat address dari index ke-1.

```python
print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")
```

Perhatikan, address dari index didalam-nya masing-masing adalah sama. Inilah mengapa copy biasa tidak dapat digunakan secara tepat pada nested list karena dia tidak bisa mengcopy secara mendalam.

Sekarang, kita coba praktek yaitu mengganti nilai didalam index nya. Berikut contoh penerapan-nya

```python
data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
```

Terlihat bahwa data asli dan copy pun tetap berubah semua-nya. Untuk mengatasi masalah ini, kita perlu menggunakan deepcopy. 

Untuk menggunakan deepcopy, kita perlu import library dari deepcopy ini didalam file python kita. Berikut contoh penerapan-nya.

```python
from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)
```

Sekarang, kita coba cek address-nya

```python
print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")
```

Untuk address nya masih sama seperti copy biasa yaitu berbeda. Namun apakah address dari data list didalam-nya berubah atau tetap sama? Kita coba lihat. Berikut contoh penerapan-nya.

```python
print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address deep = {hex(id(data_2D_deepcopy[0]))}")
```

Ternyata, address dari data list didalam nya juga ikut berubah. Inilah fungsi dari deepcopy, dia tidak hanya merubah permukaan saja namun juga didalam-nya.

Sekarang, kita coba komparasi antara data asli, data copy biasa, dan data deep copy. Kita coba ubah sedikit data-nya dan tambahkan sedikit nilai data-nya. Berikut contoh penerapan-nya.

```python
data_2D = [data_0,data_1, 10]

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")
```

Untuk data asli dan data copy biasa ikutan terganti juga sedangkan data deep copy tidak terganti. Kesimpulan-nya, gunakan deep copy jika berurusan dengan nested list.