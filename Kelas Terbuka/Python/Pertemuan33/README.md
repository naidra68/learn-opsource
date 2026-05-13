# Pertemuan33 - Nested List/List Bersarang (Python Tutorial)

Sekarang, kita akan mencoba mengenai Nested List atau list bersarang. Jadi, kita akan membuat list didalam list nanti-nya. Itulah yang dinamakan list bersarang.

Kita coba komparasi list bersarang dengan list biasa, berikut contoh penerapan-nya.

```python
data_0 = [1,2]
data_1 = [3,4,5]
data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1, 6,7]

print(f"list 2D = {list_2D}")
```

Bisa dilihat bahwa `data_list_biasa` merupakan list biasa sedangkan `list_2D` merupakan list bersarang karena isi data list tersebut gabungan dari `data_0` dan `data_1`. Simpel-nya, untuk menandakan list bersarang itu di hasilnya ada kurung didalam kurung.

## Contoh Penggunaan

Oke, sekarang kita akan mencoba penggunaan dari list bersarang ini untuk kasus seperti apa dan bagaimana. Anggap saja kita mempunyai data nama,umur dan jenis kelamin. Berikut contoh data-nya.

```python
peserta_0 = ["ucup", 25,"Laki-laki"]
peserta_1 = ["otong",10,"Laki-laki"]
peserta_2 = ["dedeh",50,"Wanita"]
```

Sekarang, kita coba buat list bersarangnya.

```python
list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"peserta = {list_peserta}")
```

Setelah itu, kita akan urutkan sesuai nama, umur, dan jenis kelamin-nya menggunakan index dengan cara memanfaatkan for looping. Berikut contoh penerapan-nya.

```python
for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"kelamin\t: {peserta[2]}\n")
```

Kode diatas akan menghasilkan data yang rapi dan sesuai urutan-nya. Inilah fungsi sebenarnya dari nested list.

<hr/>

Ada satu hal yang harus kita perhatikan dan hati-hati jika menggunakan nested list ketika ingin mencopy-nya. Kita telah mempelajari copy data list di materi sebelumnya, namun untuk kasus nested list. Itu akan sedikit berbeda. Kita coba terlebih dahulu.

Sekarang, kita akan mencoba copy `list_peserta` dan coba ubah salah satu nama dari data di dalam `list_peserta` tersebut. Berikut contoh penerapan-nya.

```python
list_copy = list_peserta.copy()
print(f"peserta = {list_copy}")

peserta_0[0] = "michael"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")
```

Lihat, jika kita mengganti nama pada index ke-0. Maka `list_peserta` akan ikut terganti. Mengapa hal ini bisa terjadi?

Jawaban-nya adalah karena kita mengcopy data luarnya saja. sedangkan data yang ada di dalam yaitu `peserta_0`, `peserta_1`, dan `peserta_2` tidak tercopy secara benar.

Untuk mengatasi masalah ini, kita akan mencoba membahasnya dipertemuan selanjutnya.