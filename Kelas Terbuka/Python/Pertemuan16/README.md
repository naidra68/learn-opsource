# Pertemuan16 - Operasi dan Manipulasi String Part 1 (Python Tutorial)

## 1. menyambung string (concatenate)

```python
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)
```

## 2. Menghitung panjang string

```python
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))
```

## 3. operator untuk string

### mengecek apakah ada komponen char atau string di string

```python
d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))
D = "D"
status = D in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))
d = "d"
status = d not in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))
```

### mengulang string

```python
print("wk"*10)
print(15*"wk")
```

#### indexing

```python
print("index ke-0 : " + nama_lengkap[0]) # u
print("index ke-1 : " + nama_lengkap[1]) # c
print("index ke-(-1) : " + nama_lengkap[-1]) # e
print("index ke-(-2) : " + nama_lengkap[-2]) # m
print("index ke-[0:3] : " + nama_lengkap[0:4]) # ucup
print("index ke-[3:7] : " + nama_lengkap[3:8]) # p D'F
print("index ke-[0,2,4,5,8,10] : " + nama_lengkap[0:11:2]) # uu 'ae
```

### item paling kecil

```python
print("paling kecil : " + min(nama_lengkap))
```

### item paling besar
```python
print("paling besar : " + max(nama_lengkap))
```

```python
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))
```