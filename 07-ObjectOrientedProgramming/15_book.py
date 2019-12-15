class Book():
    def __init__(self,author,title):
        self.author=author
        self.title=title
        self.is_open=False
        self.current_page=0    
    def open(self):
        self.is_open=True
    def close(self):
        self.is_open=False    
class Paper_book(Book):
    def __init__(self,author,title,pages):  
        self.pages=pages
        super().__init__(author,title) 
    def read_paper(self):
        if self.is_open:
            if self.current_page<self.pages:
                self.current_page+=1      
        else:
            print("\nKsiążka jest zamknięta, otwórz książkę żeby zacząć czytać")       
    def show_status(self):
        print(f"\nAutor:{self.author}\nTytuł: {self.title}\nLiczba stron: {self.pages}\nJesteś na stronie nr {self.current_page}") 
class E_book(Book):
    def __init__(self,author,title,file):  
        self.file=file
        super().__init__(author,title)
    def read_e(self):
        if self.is_open:
            print("Otworzyłeś plik do czytania książki")        
        else:
            print("\nKsiążka jest zamknięta, otwórz książkę żeby zacząć czytać")            
    def show_status(self):
        print(f"\nAutor:{self.author}\nTytuł: {self.title}\nNazwa pliku: {self.file}")  
book1=Paper_book("George R. R. Martin","Game of Thrones",694) 
book1.open()
book1.read_paper()
book1.read_paper()
book1.show_status()    
book2=E_book("George R. R. Martin","Game of Thrones","book.epub") 
book2.open()
book2.show_status()                      