tab=["PN","WT","SR","CZ","PT","SB","ND"]
for i in tab:
    print (f"| {i} ",end="")
print()
d=1
for k in range(5):
    for j in range(7):
        nr_dnia_t=j
        if k==0:
            if nr_dnia_t>=2:
                print(f"| {d}",end=" ")
                d+=1
                
            else:
                print("|   ",end=" ")
        else:
            print(f"| {d}",end=" ")
            if d!=30:d+=1
            else:break
            
    print()

            
            
    
    
    
    
        
        
    
        
        