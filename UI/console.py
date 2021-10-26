from Domain.avion import toString
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare


def printMenu():
    print("1. Adaugare rezervare bilet de avion")
    print("2. Stergere rezervare bilet de avion")
    print("3. Modificare rezervare bilet de avion")
    print("a. Afisare toate rezervarile")
    print("x. Iesire")


def ui_adaugare_rezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa: ")
    pret = input("Dati pretul: ")
    checkin = input("Dati checkin-ul: ")
    return adauga_rezervare(id, nume, clasa, pret, checkin, lista)

def uiStergeRezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    return sterge_rezervare(id, lista)

def uiModificaRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Dati noua clasa: ")
    pret = input("Dati noul pret: ")
    checkin = input("Dati noul checkin: ")
    return modifica_rezervare(id, nume, clasa, pret, checkin, lista)

def showAll(lista):
    for avion in lista:
        print(toString(avion))

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adaugare_rezervare(lista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")