# Pertemuan24 - Perulangan/Looping (Python Tutorial)


Sekarang kita akan mempelajari mengenai perulangan atau dalam bahasa inggris disebut sebagai looping.

## Fungsi Looping?

Fungsi looping sangatlah banyak, salah satu-nya ialah untuk mencetak suatu string atau tulisan sebanyak ratusan,ribuan atau bahkan jutaan.

Tanpa menggunakan looping, kita perlu menulis string tersebut satu per satu. Contoh realnya seperti Halaman Login. Kalau nilai-nya `true` atau benar maka program akan jalan dan masuk ke selanjutnya bukan? Sedangkan jika nilai-nya `false` maka dia akan berhenti di halaman login terus menerus.

Sebelum mengenal mengenai isi looping yang terdapat `range()`. Kita perlu membuat contoh menggunakan list. Berikut contoh penerapan-nya.

```python
angka_list = [0,2,4,8,10] # ini adalah list
print(angka_list)

for i in angka_list:
    print(f"i sekarang -> {i}")

print("akhir dari program \n")
```

Jika dijalankan, akan menampilkan `i` sesuai angka pada variabel `angka_list`. Bagaimana jika angka tersebut diubah?Hasilnya tetap akan mengikuti-nya.

Selanjutnya, kita coba menggunakan `range()`. Berikut contoh penerapan-nya

```python
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang -> {i}")

print("akhir dari program 2 \n")
```

Hasilnya akan menampilkan angka secara berurutan. Namun kenapa angka 5 tidak muncul? Padahal kita telah menuliskan `range(5)`?

Simple, karna looping dimulai dari index ke-0. Jadi, mulai-nya dari 0 lalu lanjut ke angka selanjutnya.

Bagaimana jika ingin memulai-nya dari index ke=1? atau langsung aja ke angka 1 tanpa membuat angka 0? Berikut contoh penerapan-nya

```python
angka2_range = range(1,10)

for i in angka2_range:
    print(f"i sekarang -> {i}")

print("akhir dari program 3 \n")
```

Kita hanya perlu menambahkan koma pada range tersebut. Perlu diingat, `range(1,10)` bukanlah seperti list diatas yang nanti tampilnya 1 dan 10 saja, namun ini sebagai penanda awal nilai dan akhir nilai.

<hr/>

Selain itu, kita juga bisa looping string, berikut contoh penerapan-nya

```python
data_str = "Saya ganteng abiees"

for huruf in data_str:
    print(huruf)

print("akhir dari program 4")
```