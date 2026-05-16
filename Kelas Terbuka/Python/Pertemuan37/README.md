# Pertemuan37 - Tuples dan Set (Python Tutorial)

Sekarang, kita akan membahas sedikit serta mencoba Tuples dan Set. Sebelum itu, kita coba dulu membuat data list seperti biasa.

```python
data_list = [10,2,4,3,2] 
print(data_list)
```

Seperti yang telah kita pelajari, untuk membuat data list. Maka kita memerlukan kurung siku. Untuk membuat tuples sama seperti data list, namun menggunakan kurung.

## tuples

Tuples merupakan data list yang bersifat konstant, yang berarti data yang berada pada list tersebut tidak dapat diubah atau diganti. Berikut contoh pembuatan-nya.

```python
data_tuples = (7,8,9,10)
print(data_tuples)
print(data_tuples[1])
```

Kita coba, apabila kita ganti index ke-1 maka akan muncul pesan error. Bahkan fungsi append pun tidak ada jika data tersebut bersifat tuples. Berikut contoh penerapan-nya.

```python
data_tuples [1] = "ucup"
data_tuples.append(1)
```

Kode diatas jika dijalankan menyebabkan error, pastikan untuk kasih komentar untuk menonaktifkan kodingan tersebut.

Jadi fungsi untuk tuples ini apa? Fungsinya bisa memberikan data yang tetap dan tidak bisa diubah, ini penting ketika kita membuat sebuah data di aplikasi kita sendiri lalu kita kirim ke aplikasi lain yang notabene data tersebut tidak bisa diubah.

## sets

sets merupakan data list yang tidak memiliki index, anggap saja data list ini seperti himpunan data. Apabila kita mencoba menampilkan index-nya, maka akan terjadi error.

```python
data_sets = {10,4,3,2,4,7,6,5}
print(data_sets)
```

Selain tidak memiliki index, data list ini sama fungsinya seperti data list pada umumnya.