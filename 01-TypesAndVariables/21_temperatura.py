#Temperatura
celsjusz=float(input("Podaj temperaturę w stopniach Celsjusza: "))
fahrenheit=celsjusz*1.8+32
kelvin=celsjusz+273.15
print("Dla wczytanej wartości temperatury {}C, temperatura w stopniach Fahrenheita wynosi: {}F,\na temperatura w stopniach "
"Kelvina jest równa: {}K". format(celsjusz,fahrenheit,kelvin)) 