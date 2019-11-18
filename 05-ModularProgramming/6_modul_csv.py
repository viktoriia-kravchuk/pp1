import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    line=1
    for row in reader:
        print(f"{line}{(row}")
        line+=1