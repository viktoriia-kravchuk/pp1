import re
tekst="To be, or not to be, that is the question"
samogloski=re.findall('[aeyiou]',tekst)
l=len(samogloski)
print(f"Liczba samogłosek w tekście: {l}")