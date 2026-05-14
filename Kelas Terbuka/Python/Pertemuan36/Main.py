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