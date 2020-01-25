import json
with open ("euro.json") as file:
    data=json.load(file)
print("NBP – 10 ostatnich notowań EURO")   
print("{}{:>15}{:>12}".format("Data","Kupno","Sprzedaż"))
print("="*31)
kurs=data["rates"]
for i in kurs:
    date=i["effectiveDate"]
    kupno=i["bid"]
    sprzedaz=i["ask"]
    print("{}{:>10}{:>10}".format(date,kupno,sprzedaz))


