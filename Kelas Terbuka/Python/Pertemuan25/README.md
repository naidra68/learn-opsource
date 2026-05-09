# Pertemuan24 - While Loop (Python Tutorial)

Oke, sekarang kita akan mencoba While Loop. Apa bedanya dengan for loop? Beda-nya terletak pada syntax penulisan.

While Loop agak tricky di gunakan karena jika kita salah memberikan nilai atau salah logika maka hasilnya akan terus menerus ada atau looping permanent.

Maksudnya? Cobain kode dibawah ini dan jalankan

```python
angka = 10

while angka > 5
    print(f"angka sekarang -> {angka}")

print("Cukup")
```

Untuk mematikan looping permanent bisa pencet `CTRL + C` pada keyboard. Mengapa bisa terjadi looping terus-menerus? Karena angka nya bernilai True.

apakah 10 > 5? akan true dan terus looping atau cetak secara brutal. 

<hr/>

Sekarang, kita coba buat angka awal menjadi 0 dan kita buat `angka < 5`. Berikut contoh penerapan-nya

```python
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    print("otong ganteng maxsyimaal!")

print("Cukuuup")
```

Semua tulisan didalam while akan ditampilkan sebanyak 5x. Fungsi dari `angka +=1` digunakan untuk menambahkan nilai pada `angka < 5`. Dimana jika bernilai `true` akan dijalankan program-nya. Begitu terus sampai terakhir angka ke-5 baru bernilai `false`, jika `false` maka akan berhenti.