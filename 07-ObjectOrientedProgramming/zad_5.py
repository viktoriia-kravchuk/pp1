class Utwor():
    def __init__(self,author,title,album,year):
        self.author=author
        self.title=title
        self.album=album
        self.year=year
    def __str__(self):
         return ('Wykonawca: {:>20}\nUtwór: {:>19}\nAlbum: {:>25}\nRok: {:>15}\n'.format(self.author,self.title,self.album,self.year))
song=Utwor('Dawid Podsiadło','Nie ma fal','Małomiasteczkowy','2018')
print(song)       
song2=Utwor('Metallica','Nothing Else Matters','Metallica','1991')
print(song)                 
song=Utwor('Dawid Podsiadło','Nie ma fal','Małomiasteczkowy','2018')
print(song)                 




