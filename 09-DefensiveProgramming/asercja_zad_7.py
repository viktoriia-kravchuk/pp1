height=int(input("Podaj swój wzrost w cm: "))
weight=float(input("Podaj swoją wagę: "))
assert type(height)==int and height<=220 and height>=150 and type(weight)==float and weight>=40.0 and weight<=150.0,'Podałeś błędne wartości'
height_m=height/100
bmi=round(weight/(height_m**2),3)
print(f"Twój BMI to: {bmi}")