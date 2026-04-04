# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case

alay = "aKu KeCe AbieezZzZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
alpha = "akurajakaubudak".isalpha()
print("akurajakaubudak is alpha = " + str(alpha))

alpha = "akunomer1".isalpha()
print("akunomer1 is alpha = " + str(alpha))

# isalnum() <-- huruf dan angka
num = "1234567890".isalnum()
print("1234567890 is num = " + str(num))

num = "bukanangka".isalnum()
print("bukanangka is num = " + str(num))

# isdecimal() <-- angka saja
decimal = "1234567890".isdecimal()
print("1234567890 is decimal = " + str(decimal))

decimal = "bukanangka".isdecimal()
print("bukanangka is decimal = " + str(decimal))

# isspace() <-- spasi, tab, newline

space = " ".isspace()
print(" is space = " + str(space))

# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## Penggabungan komponen join() split()

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

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'"+tengah+"'")