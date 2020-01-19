file=open("students.csv","r")
for i in file:
    info=i.split(',')
    assert len(info)==4,"Informacja o studencie nie jest pełna"
    for element in info:
        assert element!='',"Pusty element"
        print(element, end=" ,")
    print("\n")   
file.close()    
