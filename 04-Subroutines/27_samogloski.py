import re
tekst="Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
a=re.findall("A|a",tekst)
la=len(a)
e=re.findall("E|e",tekst)
le=len(e)
y=re.findall("Y|y",tekst)
ly=len(y)
i=re.findall("I|i",tekst)
li=len(i)
o=re.findall("O|o",tekst)
lo=len(o)
an=re.findall("Ą|ą",tekst)
lan=len(an)
en=re.findall("Ę|ę",tekst)
leno=len(en)
print(f" 'a' występuje {la} razy\n 'e' występuje {le} razy\n 'y' występuje {ly} razy\n 'i' występuje {li} razy\n 'o' występuje {lo} razy\n 'ą' występuje {lan} razy\n 'ę' występuje {leno} razy")

