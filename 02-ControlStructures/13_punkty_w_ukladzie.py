x=10
y=-5
if x>0 and y>0:
    print(f"Punkt ({x},{y}) znajduje się w pierwszej ćwiartce układu współrzędnych")
elif x>0 and y<0:
    print (f"Punkt ({x},{y}) znajduje się w drugiej ćwiartce układu współrzędnych")
elif x<0 and y<0:
   print (f"Punkt ({x},{y}) znajduje się w trzeciej ćwiartce układu współrzędnych")
elif x<0 and y>0:
    print (f"Punkt ({x},{y}) znajduje się w czwartej ćwiartce układu współrzędnych")
elif x==0 and y!=0:
    print (f"Punkt ({x},{y}) znajduje się na osi Y układu współrzędnych")
elif y==0 and x!=0:
    print (f"Punkt ({x},{y}) znajduje się na osi X układu współrzędnych")
else:
    print (f"Punkt ({x},{y}) znajduje się na początku układu współrzędnych")