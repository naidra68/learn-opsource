# Pertemuan3 - Cara Kerja Program dan Bytecode (Python Tutorial)

Cara menjalankan sebuah program python dapat dilakukan dengan menekan simbol play di pojok kanan atas VS Code.

![Gambar Simbol Play](run.jpg)

Karena kita sudah menginstall python intepreter nya maka kita telah memanggil python itu sendiri. Untuk menjalankan program python nya tanpa menggunakan simbol play VS code bisa dengan cara mengetikkan perintah `python Main.py` pada terminal yang berada di VS Code.

## Mengapa bisa seperti itu?

Jadi Python itu bahasa pemrograman intepreted, maksud dari intepreted sendiri adalah ketika source code dimasukkan ke intepreter (Penerjemah) yaitu program python itu sendiri akan dijalankan ke Terminal (Command Prompt). Interpreter dilakukan baris per baris, selain intepreter terdapat juga istilah compile.

Cara kerja compile adalah source code akan masuk ke compiled dan setelah selesai akan menghasilkan executable. Hal itu bisa dilakukan oleh bahasa pemrograman lain seperti C++. Sedangkan untuk python sendiri menggunakan intepreter, jadi tidak perlu di compile.

Perintah untuk menampilkan teks pada python bisa menggunakan `print()`. Perlu diperhatikan bahwa, di python tidak ada titik koma `;` yang biasanya sebagai penutup pada program bahasa lain.

Perintah untuk menampilkan comment yang tidak akan ditampilkan bisa gunakan `#`. Selain itu, ada comment multiline yang bisa dipakai untuk mengetik beberapa baris komentar menggunakan `"""`.

Berikut contoh penerapan-nya

```python
print("Hello World")
print("Hello")
print("Apa Kabar my Friend")

# Ini adalah Comment

""" Ini merupakan baris komentar multiline """
```

Semua hal itu dieksekusi berdasarkan urutan, semisal kita ubah perintah sebagai berikut :

```python
print("Hello")
print("Hello World")
```

Maka hasilnya yang berada di atas adalah tulisan <b>Hello</b>.

Atau bisa juga seperti ini, perhatikan code dibawah ini.

```python
print(a)
a = 10
```

Apabila dijalankan, akan menampilkan pesan error karena `nilai a` belum ada dan sudah ditampilkan. Seharusnya kita perlu mengisi `nilai a` terlebih dahulu sebelum ditampilkan, karena python berjalan secara intepreter maka hal ini menyebabkan error.

## Compile Python menjadi bytecodes 

Python dijalankan secara intepreted, jadi bisakah python di compile? jawaban-nya bisa dengan cara compile python menjadi bytecode. Jadi bytecode sama seperti `.exe`.

caranya sebagai berikut :

Ketikkan perintah `python -m py_compile Main.py` dan jalankan. 

- `-m` adalah tipe mode.
- `py_compile` adalah library python untuk compile.

Setelah menjalankan perintah tersebut, terdapat folder baru bernama `__pycache__` yang didalamnya ada file berekstensi `pyc` yang berarti python sudah berhasil di compile. Btw, `C` dalam `pyc` itu adalah bahasa pemrograman `C`.

Cara menjalankan file python yang telah di compile dengan cara masuk ke folder `__pycache__` terlebih dahulu dengan cara ketikkan perintah `cd __pycache__` lalu ketikkan nama file-nya. berikut contoh perintah-nya.

```bash
cd __pycache__
```

```bash
python Main.cpython-313.pyc
```

Ingat bahwa sesuaikan nama file-nya, biasanya nama file akan berbeda satu sama lain.

<br>

Jadi apa fungsinya dengan compile python ini? jika menampilkan hasil yang sama tanpa di compile pun? Jawaban-nya adalah pada waktu eksekusi-nya.

Cara melihat perbedaan waktu-nya, kita akan menambahkan library waktu. berikut contoh penerapan-nya.

```python
import time
start_time = time.time()

print(time.time()) - start_time, "detik"
```

Apabila dijalankan, nanti terdapat sebuah itungan detik, jika dilihat python compile akan membuat score lebih sedikit daripada python intepreted. Hal ini bisa butuhkan ketika kode program yang dibuat sudah banyak dan berat, efisiensi waktu proses akan menjadi prioritas utama.

Sekarang kita tes dengan menambahkan fungsi for untuk mencetak beberapa tulisan sekaligus sekalian meiihat waktu yang dibutuhkan program untuk di eksekusi.

```python
for i in range (1,1000):
    a = 10
```

<br>

Kesimpulan dari pembahasan ini, alur program python akan di eksekusi secara berurutan, komen tidak akan di eksekusi, komen multiline dengan menggunakan `"""`.