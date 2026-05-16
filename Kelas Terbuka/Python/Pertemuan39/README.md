# Pertemuan39 - Operasi Dictionary (Python Tutorial)

Okeh, kita akan membahas mengenai operasi dictionary. Apa saja yang bisa kita lakukan pada dictionary. Pertama, kita buat terlebih dahulu data dictionary-nya.

```python
data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung"
}
```

Kita telah membuat data dictionary yang berisi 3 data key yaitu cup,tong,dung.


## panjang dictionary

Sekarang, kita coba cek panjang dari data dictionary ini menggunakan fungsi `len`.

```python
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")
```

Kita buat variabel lendict menjadi besar supaya terhindar dari fungsi. Terkadang di python terdapat fungsi yang nama-nya serupa. Untuk menghhindari ini, kita bisa buat variabel tersebut menjadi uppercase. Untuk melihat apakah nama sebuah variabel merupakan fungsi bisa gunakan extension pylint.

# cek key exist

Kita bisa mengecek apakah key tersebut ada atau tidak. Ini memungkinkan jika data dictionary kita banyak dan kita mencoba mengecek key-nya apakah sudah ada atau belum sebelum menambah data baru pada dictionary tersebut.

Untuk mengecek-nya simple saja, kita bisa gunakan `in`. Berikut contoh penerapan-nya.

```python
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")
```

# akses value dengan get

Apabila kita ingin melihat value, kita bisa langsung ketikan kode berikut :

```python
print(data_dict["cup"])
```

Memang, terlihat normal dan tidak masalah. Namun, hal ini justru masalah apabila kita akses value yang tidak ada di dalam dictionary. Berikut contoh-nya

```python
print(data_dict["kis"])
```

Apabila dijalankan, terlihat bahwa kis tidak ditemukan dan error. Untuk mengatasi hal ini, kita bisa gunakan fungsi `get()`. Ketika data yang diakses tidak ada, dia akan menampilkan hasil none dan tidak error.

```python
print(data_dict.get("cup"))

print(data_dict.get("kis","key tidak ditemukan"))
```

Untuk parameter ke 2 itu adalah tulisan pesan yang bisa kita ubah. Jika tidak ditulis, maka hasilnya akan none.

# update data

Untuk update data cukup simpel, kita bisa langsung tulis saja key dan value-nya.

```python
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
```

# tambah data

Untuk tambah data juga sama seperti update, kita bisa langsung tulis key dan value-nya.

```python
data_dict["sep"] = "asep si kasyep"
print(data_dict)
```

Ada satu cara menarik untuk menambah data dictionary sekaligus update data jika data tersebut sudah ada. Caranya tinggal kita kasih fungsi `update()`.

```python
data_dict.update({"cup": "ucup surucup"})
print(data_dict)

data_dict.update({"faqih":"faqihza si keren"})
print(data_dict)
```

Jika menggunakan update, kita bisa merubah datanya jika data tersebut sudah ada dan kita bisa menambah datanya jika data tersebut belum ada.

## hapus data

Untuk menghapus data, kita bisa gunakan del.

```python
del data_dict["faqih"]
print(data_dict)
```