login="marek"
haslo="m-123"
login_podany=input("Podaj login: ")
haslo_podane=input("Podaj hasło: ")
if login_podany==login and haslo_podane==haslo:
    print("Podane dane są prawidłowe")
else:
    print("Podane dane są nieprawidłowe")