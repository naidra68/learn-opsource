# Pertemuan5 = Tipe Data (Python Tutorial)

Tipe data adalah macam-macam data yang ada di python dan bisa dimasukkan ke dalam variabel.

## Tipe data Integer

Tipe data integer adalah tipe data yang berisi deretan angka bulat.

```python
data_integer = 1
print("data :", data_integer)
print("- bertipe ", type(data_integer))
```

Untuk mengecek suatu variabel bertipe data apa pada python dapat menggunakan fungsi `type()`.

## Tipe data Float

Tipe data Float adalah tipe data yang berisi angka dengan koma.

```python
data_float = 1.5
print("data :", data_float)
print("- bertipe ", type(data_float))
```

## Tipe data String

Tipe data String adalah tipe data yang berisi karakter atau tulisan.

```python
data_string = "ucup"
print("data :", data_string)
print("- bertipe ", type(data_string))
```

## Tipe data Boolean

Tipe data Boolean adalah tupe data yang berisi dua kondisi saja yaitu True atau False.

```python
data_bool = True
print("data :", data_bool)
print("- bertipe ", type(data_bool))
```

## Tipe data Khusus

tipe data khusus hanya diperuntukkan pada bilangan kompleks seperti bilangan imajiner, tipe data dari bahasa C.

### bilangan kompleks

```python
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertipe ", type(data_complex))
```

### tipe data dari bahasa C

```python
from ctypes import c_double

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe ", type(data_c_double))
```

<br>

Segitu dulu untuk pembahasan mengenai tipe data pada python.
