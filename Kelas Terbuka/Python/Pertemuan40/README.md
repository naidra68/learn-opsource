# Pertemuan40 - Looping Dictionary (Python Tutorial)

Sekarang, kita akan belajar dan mencoba looping dictionary. Sebelum itu, kita buat dulu data dictionary. Kita buat data teman_teman dengan berbagai macam nama.

```python
teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}
```

Selanjutnya, kita akan mencoba looping dictionary nya pertama kali. Kita buat seperti looping seperti sebelumnya dan melihat apa yang terjadi setelahnya.

```python
for teman in teman_teman:
    print(teman)
```

Hasil menunjukan bahwa yang keluar adalah key. Jika looping seperti itu kan kita tidak mengerti apakah data tersebut dictionary atau tidak. 

Maka dari itu, kita bisa gunakan operator item atau iterables. Fungsinya adalah untuk melihat dan memahami bahwa data tersebut merupakan looping-an dictionary.

# key

Untuk mengambil key. Kita bisa langsung gunakan `keys()`.

```python
keys = teman_teman.keys()
print(keys)
```

Nah, untuk mengambil value menggunakan key ini bisa langsung di looping saja menggunakan `get()`.

```python
for key in teman_teman.keys():
    print(teman_teman.get(key))
```

# value

Bagaimana untuk mengambil data dictionary valuenya? Kita bisa gunakan `values()`.

```python
values = teman_teman.values()
print(values)
```

Sekarang, kita bisa langsung looping value-nya sama seperti tadi.

```python
for value in teman_teman.values():
    print(value)
```

# item

Apabila kita ingin melihat dua-duanya yaitu key dan value. Kita bisa gunakan `items()`

```python
items = teman_teman.items()
print(items)
```

Jika menggunakan item, data yang ditampilkan akan mencakup semua, mulai dari key beserta value-nya. Sekarang kita bisa looping data tersebut.

```python
for item in teman_teman.items():
    print(item)
```

# testing

Bagaimaan kalau kita buat seperti enumerate dan seperti kodingan dibawah ini, apakah hasilnya sesuai harapan.

```python
for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")
```

Hasilnya sesuai harapan, terlihat lebih rapi dan enak untuk dibaca.