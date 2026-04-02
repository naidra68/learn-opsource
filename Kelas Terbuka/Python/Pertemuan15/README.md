# Pertemuan15 - Pengenalan String (Python Tutorial)

String merupakan sekumpulan karakter yang dapat di masukkan ke dalam program python.

berikut contoh-nya

```python
data = "ini adalah string"
print(data)
```

Sekarang kita coba lihat tipe data dari string ini seperti apa.

```python
data = "ini adalah string"
print(type(data))
```

Jika dijalankan akan menghasilkan `<class 'str'>`. Kalau sudah belajar OOP maka hasil tersebut akan menjelaskan bahwa itu merupakan object class.


Ada 2 cara untuk membuat string pada Python, yaitu dengan Single Quote dan Double Quote.

Berikut contoh single quote

```python
data = 'Menggunakan single quote'
print(data)
```

Berikut contoh double quote

```python
data = "Menggunakan double quote"
print(data)
```

Kita juga bisa memakai single dan double atau digabung menjadi satu.

berikut contoh-nya

```python
print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
```

Ketika dijalankan, maka seperti kalimat baca. Kita coba contoh lain

```python
print("ini adalah hari jum'at")
```

## Backslash

Kita juga bisa membuat sebuah tanda kutip menjadi string, misalnya kita akan print kalimat jum'at tapi menggunakan tanda kutip satu.

Sekilat dilihat itu akan error karena pada kalimat <b>jum'at</b> terdapat kutip satu. Namun kita bisa mengakali-nya dengan tanda backslash `\`.

berikut contoh-nya

```python
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')
```

Jika dijalankan, tidak akan menampilkan error.

## backlash

Agar backlash bisa diprint maka tambahin lagi backlash.

```python
print("C:\\user\\ucup")
```

## tab

berikut untuk membuat tab

```python
print("ucup\t\t\totong, semakin jauhan")
```

## backspace

berikut untuk membuat backspace

```python
print("ucup \botong, jadi deketan")
```

## newline

berikut untuk membuat newline

```python
print("baris pertama.\nbaris kedua.") # LF -> line feed
print("baris pertama.\rbaris kedua.") # CR -> carriage return
print("baris pertama.\r\nbaris kedua.") #CRLF -> line feed carriage return
```

## String Literal atau Raw

```python
print('C:\\nnew folder') # akan salah pathya
```

Solusi, menggunakan raw string

```python
print(r'C:\new folder')
```

## Multiline literal string

```python
print("""
Nama : ucup
Kelas : 3 SD
""")
```

## multiline literang string dan RAW

```python
print("""
Nama : Ucup
Kelas : 3 SD
Website : www.ucup.com/newID
""")
```