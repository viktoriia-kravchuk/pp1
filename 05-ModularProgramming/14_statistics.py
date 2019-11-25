import statistics
with open("employees.csv","r") as file:
    tab=[]
    for i in file:
        x=i.split(",")
        if x[2].isdigit():
            tab.append(int(x[2]))  
    srednia=statistics.mean(tab)     
    print(f"Średnia wieku pracowników wynosi : {srednia}")
    tab.sort()
    mediana=statistics.median(tab)
    print(f"Mediana wynosi: {mediana}")
    odchylenie=statistics.pstdev(tab)
    print(f"Odchylenie standardowe to: {odchylenie}")

