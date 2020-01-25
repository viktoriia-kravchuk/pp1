import json
import string
result=dict.fromkeys(string.ascii_letters,0)
with open ("DontMakeMeWait.txt","r") as file:
    text=file.read()
for letter in result:
    result[letter]=text.count(letter)
with open('letters.json', 'w') as file:
    json.dump(result, file, indent=4)    