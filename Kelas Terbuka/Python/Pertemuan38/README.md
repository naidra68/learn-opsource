# Pertemuan38 - Dictionary (Python Tutorial)

Baiklah, sekarang kita akan membahas mengenai Dictionary pada python. Materi kali ini sangat penting karena dictionary ini sangat powerful dan digunakan di python.

Data list itu merupakan array yang ada di python, untuk mengakses data list kita memerlukan index. Setiap index menentukan data mana yang akan diambil. 

## dictionary

Dictionary merupakan associative array pada python dimana memerlukan key dan value. Jika data list memerlukan index, maka dictionary memerlukan key.

key ini dapat ditulis apapun, penulisan dictionary menggunakan kurung kurawal `{}`. Untuk membedakan antara key dan value, maka memerlukan tanda `:`. Berikut contoh penerapan-nya.

```python
data_dict = {
    'cp' : 'ucup',
    'tg' : 'otong',
    'dg' : 'dudung',
    'nmbr' : 100,
    'list' : data_list
}

print(data_dict['tg'])
print(data_dict['nmbr'])
print(data_dict['list'])
```

Kode diatas mengindikasikan bahwa dictionary dapat berisi apapun mulai dari string, number, boolean, data list, bahkan dictionary didalam dictionary pun bisa.