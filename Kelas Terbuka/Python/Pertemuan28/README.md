# Pertemuan28 - Latihan Perulangan (Python Tutorial)

Sekarang, kita akan latihan perulangan dan membuat sesuatu yang menarik, contohnya. Kita akan membuat segitiga sama kaki atau segitiga siku-siku menggunakan perulangan while.

Kita buat menggunakan for terlebih dahulu. Berikut contoh penerapan-nya

```python
# dummy variable
print("awal for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for")
```

Sekarang, kita coba menggunakan while. Berikut contoh penerapan-nya

```python
print ("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir while")
```

Jika dilihat, memang lebih rumit menggunakan while daripada for. Ini hanya sebagai informasi bahwa membuat segitiga tidak hanya menggunakan for saja namun while juga bisa.

Sekarang, kita coba buat nilai-nya menjadi ganjil, segitiga-nya nanti akan ganjil seperti (1,3,5,dst). Berikut contoh penerapan-nya.

```python
print ("awal while")
count = 1
while True:
    if (count % 2):
        # Print jika ganjil
        print("*"*count)
        count += 1
    else:
    # akan kembali ke atas jika genap
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while")
```

<hr/>

Selanjutnya, kita coba buat segitiga sama kaki dengan kelipatan ganjil. Berikut contoh penerapan-nya

```python
print ("awal while")
count = 1
spasi = int(sisi/2)

while True:
    if (count % 2):
        # Print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
    # akan kembali ke atas jika genap
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break
```

Kodingan-nya sama seperti yang ganjil diatas, namun kita tambahkan sisi karena untuk membuat segitiga sama kaki, maka kita perlu sisi disebelah kiri-nya akan di isi spasi biar dia rada menjorok ke kanan. Coba jalankan kode diatas dan lihat hasilnya.

<hr/>

Oke, sekarang kita coba buat belah ketupat. Kodingan nya sama seperti yang atas untuk membuat bagian atas-nya, namun untuk membuat bagian bawah-nya kita perlu while lagi dan kita set terbalik dari atas-nya. Berikut contoh penerapan-nya

```python
print ("\nawal while")
count = 1
spasi = int(sisi/2)

while True:
    if (count % 2):
        # Print jika ganjil
        print("x"*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
    # akan kembali ke atas jika genap
        count += 1
        continue
    # akan break jika count melebihi sisi
    if count > sisi:
        break

count = count - 2
spasi = 1
while True:
    if (count % 2):
        print("x"*spasi,"+"*count)
        spasi += 1
        count -= 1
    else:
        count -= 1
    if count == 0:
        break
```