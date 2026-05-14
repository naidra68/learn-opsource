# Pertemuan36 - Latihan List (Python Tutorial)


Oke, setelah kita mempelajari data list. Sekarang kita akan praktek membuat program kecil-kecilan yaitu program data list buku beserta pencipta-nya.

Jadi sistemnya simple, nanti kita bisa input data buku nya terlebih dahulu terdiri dari nama buku dan nama penulis. Setelah itu, kita bisa berikan perintah apakah ingin lanjut input data buku atau tidak. Jika lanjut maka dia akan balik ke awal yaitu input data buku lagi, jika tidak maka program selesai.

Pertama-tama, kita buat dulu variabel list_buku dengan data list kosongan. Variabel kosong ini digunakan sebagai data list yang akan di isi macam-macam buku dan nama penulis-nya.

```python
# program list buku

list_buku = []
```

Setelah itu, kita buat dulu while nya, pastikan while nya `TRUE`, maka dari itu kita langsung buat saja while true. Selanjutnya, kita buat judul dan penulis buku dengan input.

```python
while True:
    print(10*"="+" Masukkan data buku " + "="*10)
    judul = input("Judul Buku\t: ")
    penulis = input("Nama penulis\t: ")
```

Masih didalam while, kita buat variabel buku_baru dimana isinya adalah data list dari judul dan penulis. Setelah itu, kita gunakan fungsi `append` pada variabel kosong tadi dan masukkan buku_baru-nya.

```python
    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
```

Masih didalam while, kita tampilkan data list buku dan penulis-nya menggunakan for enumerate supaya kita dapat melihat index dan data-nya secara langsung, index-nya kita anggap sebagai no urut data. Agar index tidak mulai dari nol, kita bisa `+1` pada print-nya, untuk index yang akan ditampilkan berarti ada 2 yaitu :

- buku[0] = Judul Buku
- buku[1] = Nama Pencipta

```python
    print("\n\n","="*10,"Data Buku","="*10)
    print("No.| Judul| Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
```

Setelah kita selesai membuat data list-nya, sekarang kita buat kondisi dimana input akan dilanjutkan atau tidak. Kita gunakan if pekondisian disitu.

Jadi sistemnya simple, apabila tidak dilanjutkan, maka kita langsung break saja dan langsung print program selesai.

```python
    print("\n\n","="*20)
    isLanjut = input("Apakah dilanjutkan? (y/n) : ")

    if isLanjut == "n":
        break

print("PROGRAM SELESAI")
```

<hr/>


Berikut ini codingan full program-nya

```python
# program list buku

list_buku = []
while True:
    print(10*"="+" Masukkan data buku " + "="*10)
    judul = input("Judul Buku\t: ")
    penulis = input("Nama penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10,"Data Buku","="*10)
    print("No.| Judul| Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    print("\n\n","="*20)
    isLanjut = input("Apakah dilanjutkan? (y/n) : ")

    if isLanjut == "n":
        break

print("PROGRAM SELESAI")
```