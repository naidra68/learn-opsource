# Pertemuan19 - String Width and Alignment (Python Tutorial)

Kali ini kita akan mencoba mengenai String Width and Alignment yaitu mengatur lebar string agar data bisa tampil lebih rapi dan enak dilihat.

Kita buat terlebih dahulu data-nya

```python
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44
```

Sekarang kita coba buat string normal dan masukkan semua data tersebut ke dalam string dan pisahkan menggunakan koma. Berikut contoh penerapan-nya.

```python
# string
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)
```

<hr/>

Agar data tersebut berjejer kebawah dan terlihat lebih rapi, kita bisa gunakan `\n` disetiap string nama-nya. Berikut contoh penerapan-nya

```python
# String multiline (dengan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
```

<hr/>

Kita juga bisa gunakan String multiline dengan triple kutip. Dimana cara membuatnya cukup menggunakan 3x petik dua. `"""code here"""`. Berikut contoh penerapan-nya

```python
# String multiline (kutip triplets)

data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
```

Jika kita menggunakan triplets, maka apapun yang kita ketik didalam itu akan ditampilkan apa ada-nya, maksudnya sesuai jika ada enter, newline, dan tab. Lebih mudah bukan?

<hr/>

Kita juga bisa mengatur lebar string nya, dengan menggunakan `:>angka` dimana angka ini akan merujuk pada seberapa luas lebar string-nya. Berikut contoh penerapan lengkap-nya.

```python
# mengatur lebar
data_nama = "Ucup Surucup"
data_tinggi = 105.17
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
```