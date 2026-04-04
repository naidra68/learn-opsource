# Pertemuan16 - Operasi dan Manipulasi String Part 2 (Python Tutorial)

Kita bisa membuat operator untuk memanipulasi string dalam bentuk method. Semua method ini tersedia pada python.

## merubah semua ke upper case

```python
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)
```

Mengubah suatu string ke huruf besar.

## merubah semua ke lower case

```python
alay = "aKu KeCe AbieezZzZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)
```

Mengubah suatu string ke huruf kecil.

<hr>

Kita juga bisa menggunakan method isX untuk pengecekan suatu string.

##  contoh pengecekan lower case

```python
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))
```

Semua pengecekan akan menghasilkan nilai bool True atau False.

## isalpha()

```python
alpha = "akurajakaubudak".isalpha()
print("akurajakaubudak is alpha = " + str(alpha))

alpha = "akunomer1".isalpha()
print("akunomer1 is alpha = " + str(alpha))
```

Method untuk mengecek semua huruf

## isalnum()

```python
num = "1234567890".isalnum()
print("1234567890 is num = " + str(num))

num = "bukanangka".isalnum()
print("bukanangka is num = " + str(num))
```

Method untuk mengecek huruf dan angka

## isdecimal()

```python
decimal = "1234567890".isdecimal()
print("1234567890 is decimal = " + str(decimal))

decimal = "bukanangka".isdecimal()
print("bukanangka is decimal = " + str(decimal))
```

Untuk mengecek hanya angka

## isspace()

```python
space = " ".isspace()
print(" is space = " + str(space))
```

Untuk mengecek spasi,tab,newline.

## istitle()

```python
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " + str(cek_judul))
```

Untuk mengecek apakah semua kata dimulai dari huruf besar atau tidak.

## ngecek komponen

Terdapat dua method

- startswith()
- endswith()

```python
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))
```

startwith digunakan untuk mengecek awalan string dan endswith digunakan untuk mengecek akhiran string.

## Penggabungan komponen

Terdapat dua method

- join()
- split()

```python
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))
```

Method join digunakan untuk menggabungkan list string menjadi satu, sedangkan split digunakan untuk memisahkan string menjadi list.

## alokasi karakter

Terdapat 3 method

- rjust()
- ljust()
- center()

```python
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")
```

## kebalikannya

kita bisa gunakan strip untuk kebalikan dari 3 method diatas

```python
tengah = tengah.strip(":") # menghilangkan tanda :
print("'"+tengah+"'")
```
