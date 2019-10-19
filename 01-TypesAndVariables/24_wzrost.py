cm=170
m=cm/100
stopy_float=m*3.2808
stopy=int(stopy_float)
cale=int(round((stopy_float-stopy)*12,0))
print("Mój wzrost to: {}cm, tj. {} stóp i {} cali".format(cm,stopy,cale))
