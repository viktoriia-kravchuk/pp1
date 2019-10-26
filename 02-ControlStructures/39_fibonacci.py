ciag_f=[0,1]
for j in ciag_f:
    print (j,end=" ")
for i in range(50):
    a=ciag_f[-1]+ciag_f[-2]
    ciag_f.append(a)
    print(a,end=" ")