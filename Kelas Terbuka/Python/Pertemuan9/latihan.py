# Latihan Konversi Temperatur Fahrenheit ke Kelvin

fahrenheit = float(input("Masukan suhu fahrenheit :"))
kelvin = (fahrenheit - 32) * 5/9 + 273.15

print('Suhu dalam kelvin adalah', kelvin, 'Kelvin')

# Latihan Konversi Temperatur Kelvin ke Fahrenheit

kelvin = float(input("Masukan suhu kelvin :"))
fahrenheit = (kelvin - 273.15) * 9/5 + 32

print('Suhu dalam fahrenheit adalah', fahrenheit, 'fahrenheit')