suhu_celcius = float(input("Input   : "))

suhu_fahrenheit = (suhu_celcius * 9/5) + 32
suhu_kelvin = suhu_celcius + 273.15

# Menggunakan format :.2f untuk 2 angka desimal
print(f"Output  : {suhu_fahrenheit:.2f} F dan {suhu_kelvin:.2f} K")
