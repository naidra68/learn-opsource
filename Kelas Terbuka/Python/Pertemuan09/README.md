# Pertemuan9 = Konversi Temperature (Python Tutorial)

Pada Pertemuan kali ini, kita akan mencoba untuk konversi temperature. Jadi untuk konversi kita mulai dulu dari Celcius ke Temperatur lain seperti Reamur, Fahrenheit, dan Kelvin.

Karena kita telah mempelajari mengenai variabel, tipe data, operasi aritmatika, dan input. Maka dengan menggabungkan semua hal tersebut akan bisa membuat mini program sederhana yaitu konversi temperatur.

```python
# program konvresi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR CELCIUS \n")

celcius = float(input('Masukan suhu dalam celcius :'))
print("Suhu adalah", celcius, "Celcius")

# reamur

reamur = (4 / 5) * celcius
print("Suhu dalam reamur adalah", reamur, "reamur")

# fahrenheit

fahrenheit = ((9 / 5) * celcius) + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah", kelvin, "kelvin")
```


## Latihan

Sekarang kita akan latihan untuk mengubah temperatur dari fahrenheit ke kelvin dan kelvin ke fahrenheit.

```python
# Latihan Konversi Temperatur Fahrenheit ke Kelvin

fahrenheit = float(input("Masukan suhu fahrenheit :"))
kelvin = (fahrenheit - 32) * 5/9 + 273.15

print('Suhu dalam kelvin adalah', kelvin, 'Kelvin')

# Latihan Konversi Temperatur Kelvin ke Fahrenheit

kelvin = float(input("Masukan suhu kelvin :"))
fahrenheit = (kelvin - 273.15) * 9/5 + 32

print('Suhu dalam fahrenheit adalah', fahrenheit, 'fahrenheit')
```