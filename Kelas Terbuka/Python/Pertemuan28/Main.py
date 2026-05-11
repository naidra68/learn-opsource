# Latihan perulangan membuat segitiga

sisi = 10

# menggunakan for

# dummy variable
print("awal for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for")

# 2. Menggunakan while

print ("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir while")

# 3. Mhanya ganjil saja

print ("awal while")
count = 1
while True:
    if (count % 2):
        # Print jika ganjil
        print("*"*count)
        count += 1
    else:
    # akan kembali ke atas jika genap
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while")

# 4. segitiga sama kaki

print ("awal while")
count = 1
spasi = int(sisi/2)

while True:
    if (count % 2):
        # Print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
    # akan kembali ke atas jika genap
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

# 5. belah ketupat

print ("\nawal while")
count = 1
spasi = int(sisi/2)

while True:
    if (count % 2):
        # Print jika ganjil
        print("x"*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
    # akan kembali ke atas jika genap
        count += 1
        continue
    # akan break jika count melebihi sisi
    if count > sisi:
        break

count = count - 2
spasi = 1
while True:
    if (count % 2):
        print("x"*spasi,"+"*count)
        spasi += 1
        count -= 1
    else:
        count -= 1
    if count == 0:
        break



