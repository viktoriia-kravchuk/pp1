class book():
    def __init__(self,autor,tytul,strony):
        self.author=autor
        self.title=tytul
        self.pages=strony
        self.current_page=0
        self.is_open=False
    def show_status(self):
        print(f"\nAutor:{self.author}\nTytuł: {self.title}\nIlość stron: {self.pages}\nJesteś na stronie nr {self.current_page}")    
    def open(self):
        self.is_open=True
    def close(self):
        self.is_open=False    
    def read(self):
        if self.is_open:
            if self.current_page<self.pages:
                self.current_page+=1
        else:
            print("\nKsiążka jest zamknięta, otwórz książkę żeby zacząć czytać")        

            
