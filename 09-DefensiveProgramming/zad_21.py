def iloczyn_zbiorow(z1, z2):
    try:
        if type(z1)!=set or type(z2)==set:
            print("Jeden lub dwa elementy nie są zbiorami ")
    except TypeError:
        print(TypeError)  
        return False  
    print(f"Zbiór 1: {z1}\nZbiór 2: {z2}\nIloczyn zbiorów: {z1.intersection(z2)}")        
set1=set([1,2,3,4,5,6,7,8,9])    
set2=set([2,4,6,8])
set3=set(['qwerty'])
iloczyn_zbiorow(set1,set2)
iloczyn_zbiorow(set2,set3)
