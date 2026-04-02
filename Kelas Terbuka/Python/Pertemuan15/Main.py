data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

"""
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote '...'
"""

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash

print("C:\\user\\ucup")

# tab

print("ucup\t\t\totong, semakin jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline

print("baris pertama.\nbaris kedua.") # LF -> line feed
print("baris pertama.\rbaris kedua.") # CR -> carriage return
print("baris pertama.\r\nbaris kedua.") #CRLF -> line feed carriage return

# 3. String literal atau raw

# hati-hati
print('C:\\nnew folder') # akan salah pathya

# menggunakan raw string

print(r'C:\new folder')

# Multiline literal string

print("""
Nama : ucup
Kelas : 3 SD
""")

# multiline literang string dan RAW

print("""
Nama : Ucup
Kelas : 3 SD
Website : www.ucup.com/newID
""")