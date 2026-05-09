# Pertemuan23 - Latihan Percabangan (Kalkulator Sederhana) (Python Tutorial)

Setelah kita mempelajari mengenai percabangan `if` dan `elif`, selanjutnya kita akan latihan membuat progrmam yang sangat sederhana yaitu kalkulator.

Kalkulator yang akan kita buat kali ini sangatlah sederhana karena cuma mengandalkan percabangan saja. Jika ekspetasi seperti kalkulator canggih lainnya maka itu dibuat sangat kompleks.

## Kenapa kita harus buat?

Kita membuat program sederhana ini sebagai latihan kepada diri kita sendiri, apakah kita sudah paham terhadap materi yang disampaikan atau belum.

## Kode kalkulator sederhana

Berikut ini merupakan kode hasil latihan pembuatan kalkulator sederhana dengan metode percabangan.

```python
# Kalkulator Sederhana

print(10*"=")
print("Kalkulator Sederhana")
print(10*"=" + "\n")

angka_1 = float(input("Masukkan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("Masukkan angka 2 = "))

# percabangannya

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("masukan yang bener dong!, aku pusying")
    
print("Akhir dari program, terima gajihh!")

```