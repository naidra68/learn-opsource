# Soal Pertama

inputUser = float(input("Masukkan angka lebih dari 0 dan kurang dari 5 \natau\n lebih dari 8 dan kurang dari 11 :"))

isCondition1 = inputUser > 0 and inputUser < 5
isCondition2 = inputUser > 8 and inputUser < 11
isCorrect = isCondition1 or isCondition2

print("Angka yang anda masukkan = ", isCorrect)


# Soal Kedua

inputUser = float(input("Masukkan angka kurang dari 0 atau lebih dari 5 \ndan\n kurang dari 8 atau lebih dari 11 :"))

isCondition1 = inputUser < 0 or inputUser > 5
print(isCondition1)
isCondition2 = inputUser < 8 or inputUser > 11
print(isCondition2)
isCorrect = isCondition1 and isCondition2

print("Angka yang anda masukkan = ", isCorrect)