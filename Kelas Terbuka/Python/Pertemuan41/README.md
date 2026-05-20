# Pertemuan41 - Copy & Pop Dictionary (Python Tutorial)

Oke, sekarang kita akan membahas dan mencoba mengenai Copy & Pop pada data dictionary. Kita harus buat dulu data teman-teman.

```python
teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}
```

Sebelum masuk ke copy, kita akan mencoba dulu menyalin data-nya secara normal dan melihat apa yang terjadi selanjutnya.

```python
friends = teman_teman

print(f" teman-teman : {teman_teman}\n")
print(f" friends: {friends}\n")
```

Lihat, datanya sama bukan? Sekarang kita akan mencoba mengubah data dictionary tersebut.

```python
teman_teman["cup"] = "ucup si kweren"
print(f" teman-teman : {teman_teman}\n")
print(f" friends: {friends}\n")
```

Ternyata, sama seperti list ketika kita mencoba menyalin tanpa menggunakan copy, maka data tersebut akan ganti semua-nya.

## copy dictionary

Sekarang, kita coba membuat code nya dengan menambahkan fungsi `copy()`.

```python
friends = teman_teman.copy()

print(f" teman-teman : {teman_teman}\n")
print(f" friends: {friends}\n")

teman_teman["cup"] = "ucup si kweren"
print(f" teman-teman : {teman_teman}\n")
print(f" friends: {friends}\n")
```

Terlihat bahwa, data cup akan terganti value-nya sedangkan data friends masih sama. Ini menandakan bahwa jika ingin menyalin kita harus menggunakan copy.

## pop dictionary

Sekarang kita akan mencoba pop dictionary. Pop ini sama seperti mengambil data dari dictionary dan memasukkannya ke dalam variabel baru. Data yang telah diambil akan menghilang dari dictionary.

```python
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")
```

Terlihat bahwa data sep pada dictionary friends akan menghilang dan masuk ke variabel dataAsep. Datanya berupa key dan value. Jadi datanya menjadi tuples.

Untuk mengambil data terakhir, kita bisa gunakan fungsi `popitem()`. Hal ini dapat digunakan ketika kita memiliki data yang banyak dan tidak tau dimana akhirnya, maka dari itu gunakanlah fungsi ini.

```python
dataTerakhir = friends.popitem()
print(f"data terakhir {dataTerakhir}\n")
print(f"friends = {friends}\n")
```