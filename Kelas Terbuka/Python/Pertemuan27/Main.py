# Break

# angka = 0

# while angka < 5:
#     angka += 1
#     print(f"angka sekarang -> {angka}")

#     if angka == 3:
#         print("Nice!")
#         break
#     print("whassup!")

# print("Cukuup finish!")

data_int = int(input("Hitung angka sampai ke = ").replace("-", ""))

angka = 0

while True:
    angka += 1
    print(f"Count -> {angka}")
    print(f"angka sekarang -> {angka}")

    if angka == data_int:
        print("Nice!")
        break

print("Cukup Finish!")