import json
with open("notowania.json",encoding="utf-8") as file:
    data=json.load(file)
    print("NBP – kursy walut")   
    print("{:<20}{:<10}{:<10}{:<10}".format("Waluta","Symbol","Kupno","Sprzedaż"))
    print("="*48)
    kurs=data[0]["rates"]
    for elem in kurs:
        print("{:<20}{:<10}{:<10}{:<10}".format(elem["currency"],elem["code"],elem["bid"],elem["ask"]))
