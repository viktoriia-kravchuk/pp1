#Obliczanie wskaźnika masy ciała BMI
#wczytujemy dane z klawiatury
wzrost=int(input("Podaj wzrost w cm: "))
waga=int(input("Podaj wagę w kg: "))
#obliczanie bmi
bmi=round(waga/((wzrost/100)**2),2) 
#wysietlanie rezultaty i sprawdzenie bmi
if(bmi<18.5):
    print("Wskaźnik BMI: {} (niedowaga)". format(bmi))
elif (bmi<=24.9):
    print("Wskaźnik BMI: {} (waga prawidłowa)". format(bmi))
elif (bmi<=29.9):
    print("Wskaźnik BMI: {} (nadwaga)". format(bmi))
else:
    print("Wskaźnik BMI: {} (otyłość)". format(bmi))