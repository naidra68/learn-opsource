# Pertemuan18 - Format String (Python Tutorial)

Sekarang, kita akan mempelajari cara memformat string agar kode python kita rapi dan gampang di gunakan.


## normal string

Sebelumnya, jika kita membuat sebuah string biasa, seperti contoh berikut :

```python
nama = "marlene"
format_str = "hello " + nama
print(format_str)
``` 
Maka, menuliskan string ditambah nama variabel-nya, bukan? Cara seperti itu memang tidaklah salah, namun ada cara yang lebih bagus dan enak di lihat yaitu dengan cara format string. Bagaimana cara melakukan format string?

## format string

Caranya cukup menambahkan kata `f` di depan isi variabel-nya. Berikut contoh penerapan-nya

```python
# contoh generic
#string
nama = "marlene"
format_str = f"hello {nama}"

print(format_str)
```

Hal tersebut membuat kode kita lebih mudah dipahami dan terlihat rapi karena kita bisa menuliskan variabel didalam string itu sendiri. Untuk penulisan variabel di dalam string harus menggunakan tanda `{}`.

## boolean, angka, bilangan bulat

Cara penulisan ini juga dapat dilakukan pada variabel angka, boolean dan juga bilangan bulat. Berikut contohnya

```python
# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)
```

Untuk memastikan sebuah variabel bernilai bilangan bulat, maka kita perlu menambahkan `:d` setelah nama variabel-nya sesuai code diatas. Hal tersebut menekankan bahwa variabel harus bernilai bulat. Jika kita mencoba mengubahnya ke float maka akan error.
<hr/>

## ordo ribuan/jutaan

Terdapat cara menulis bilangan ribuan dengan koma, caranya cukup gampang yaitu dengan menambahkkan `:,` setelah nama variabel. Selain ribuan, hal tersebut berlaku juga pada penulisan bilangan jutaan karna akan di set secara otomatis. Berikut contoh penerapan-nya.

```python
# bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan dengan ordo jutaan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)
```

<hr/>

## desimal

Untuk bilangan desimal dengan angka koma yang banyak, maka kita perlu menambahkan `:.angkaf`. Maksud dari angka adalah nilai yang berada setelah koma akan di set atau ditampilkan berapa. Berikut contoh penerapan-nya

```python
# bilangan desimal

angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)
```

Karna nilai angka-nya adalah `2005.54321` angka setelah titik ada 5 maka kita perlu mengatur-nya. Code diatas kita mengaturnya menjadi `:.3f` berarti angka yang ditampilkan hanya `2005.543` karna kita mengaturnya hanya 3.

<hr/>

## leading zero

Kita juga bisa menambahkan angka leading zero. Maksudnya adalah angka awalan kita bisa tampilkan angka nol. Berikut contoh penerapan-nya

```python
# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)
```

Karena total angka pada nilai tersebut adalah 9. Kenapa 9? coba saja hitung nilai-nya. Maka kita perlu mengaturnya melebihi 9 yaitu kita atur menjadi 10. Setelah itu kita tambahkan angka 0 didepan-nya. Jadi code nya adalah `:010.3f`.

<hr/>

## menampilkan plus dan minus

Kita juga bisa menampilkan tanda `+` pada bilangan normal. Maksudnya gini, jika kita membuat bilangan minus kan ada tuh tanda `-` didepan angka-nya bukan? Nah, kita juga bisa menambahkan tanda `+` tersebut. Berikut contoh penerapan-nya

```python
# menampilkan tanda + atau -
angka_minus = -10
angka_plus  = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)
```

<hr/>

## persentase

Kita juga bisa memformat nilai persen jika suatu nilai persen tersebut terdapat angka 0 didepan-nya. Maksudnya gimana? Berikut contoh code-nya

```python
# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"

print(format_persen)
```

Terdapat nilai nol ada 2 di dalam nilai variabel tersebut. Maka kita perlu mengaturnya menggunakan code `.2%`. Angka 2 tersebut tergantung nilai 0 yang terdapat pada nilai variabel.

<hr/>

## operasi aritmatika placeholder

Nah, kita juga bisa melakukan operasi aritmatika pada placeholder. Berikut contoh code-nya

```python
# melakukan operasi aritmatika di dalam placeholder

harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)
```

Jadi, kita bisa langsung lakukan operasi aritmatika disitu, code `:,` hanya untuk menampilkan koma pada angka nol agar terlihat seperti angka ribuan atau ratusan atau bahkan jutaan.

<hr/>

## format angka lain

Kita juga bisa memformat angka bilangan lain seperti biner, octal, dan hexadecimal dengan memanggil fungsi masing-masing bilangan tersebut. Berikut contoh penerapan-nya

```python
# format angka lain (binary, octal, hexadecimal )

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
```