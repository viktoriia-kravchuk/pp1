import csv
import statistics
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    line=0
    wiek=[]
    tab=list(reader)
    for row in tab:
        if line==0:
            print("{:^2}{:^12}{:^12}{:^12}{:^12}".format("#","NAME ","SURNAME ","AGE ","EMAIL "))
            print("="*65)
        else:
            print("{:^2}{:^12}{:^12}{:^12}{:^12}".format(line,row[0],row[1],row[2],row[3]))
            wiek.append(int(row[2]))
        line+=1
    print(f"Średnia arytmetyczna wieku pracowników wynosi: {statistics.mean(wiek)}")    
