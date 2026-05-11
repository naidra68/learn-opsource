# Pertemuan29 - List (Python Tutorial)

Pada kesempatan kali ini, kita akan membahas mengenai List pada Python. List ini sama seperti array pada bahasa pemrograman lain.

List merupakan sekumpulan data yang dijadikan 1 dalam variabel. Berikut contoh pembuatan list sederhana.

```python
# Kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)
```

Kode diatas merupakan list yang berisi kumpulan data numbers. 

Selain data numbers, kita juga bisa buat list data string, berikut contoh penerapan-nya

```python
# Kumpulan data string

data_string = ["ucup","otong","odah"]
print(data_string)
```

Bagaimana dengan boolean? Kita juga bisa membuatnya pada list, hasilnya akan menjadi True dan False, bukan number 0 atau 1. Berikut contoh penerapan-nya

```python
# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)
```

Okeh, sekarang kita coba membuat list yang berisi campuran, terdapat number,string, dan boolean. Berikut contoh penerapan-nya.

```python
# Kumpulan campuran
data_campuran = [1,"bala-bala",2,"cireng","ucup",True,"otong",False]
print(data_campuran)
```

Selain pembuatan list seperti diatas, kita bisa cara alternatif juga untuk membuat list. Masih ingat dengan `range()` bukan?

Sekarang, kita akan buat list menggunakan range. Berikut contoh penerapan-nya

```python
## cara alternatif membuat list

data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)
```

Perhatikan pada `range(0,10,2)`.

- angka 0 adalah nilai awal range
- angka 10 adalah nilai tujuan range
- angka 2 adalah nilai kelipatan range

Maksud dari kelipatan? Lihat saja kode diatas dan jalankan. Nanti akan terlihat bahwa setiap nilai-nya dilipatkan 2.

<hr/>

Kita juga bisa membuat list comprehension, dimana list tersebut dibuat dengan for loop. Berikut contoh penerapan-nya

```python
data_list_for = [i for i in range(0,10)]
print(data_list_for)
```

Penjelasan mengenai kode diatas, kita coba perhatikan. Maksud dari `i for i in range()` adalah buat i pada i didalam range tersebut. Jadi i awalan itu digunakan untuk memasukkan setiap nilai i ke dalam sebuah list.

Sekarang, apakah kita bisa membuat jadi kelipatan 2? Jawabannya bisa. Tambahkan `**2` setelah i awalan. Berikut contoh penerapan-nya.

```python
data_list_for = [i**2 for i in range(0,10)]
print(data_list_for)
```

<hr/>

Oke, kali ini kita coba sesuatu yang menarik seperti membuat list pake for dan if. Kita coba kasus sederhana seperti ganjil dan genap. Berikut contoh penerapan-nya

```python
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

# Genap
list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

#Ganjil
list_pake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)
```