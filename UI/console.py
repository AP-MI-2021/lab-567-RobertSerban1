from Domain.avion import toString
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import ordonare_rezervari_descresc, cel_mai_mare_pret_pentru_clase, \
    mutare_la_clasa_superioara


def printMenu():
    print("1. Adaugare rezervare bilet de avion")
    print("2. Stergere rezervare bilet de avion")
    print("3. Modificare rezervare bilet de avion")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("6. Determinarea prețului maxim pentru fiecare clasă.")
    print("7. Ordonarea rezervărilor descrescător după preț.")
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

def ui_mutare_la_clasa_superioara(lista):
    nume = input("Dati numele persoanei: ")
    lista = mutare_la_clasa_superioara(nume, lista)
    return lista


def ui_ieftinire_procentaj(lista):
    procentaj = input("Dati procentul: ")
    i = 0
    string = [procentaj[i:i+len(procentaj)-1] for i in range(0, len(procentaj), len(procentaj)-1)]
    percent = int(string[0])
    lista = ieftinire_procentaj(percent, lista)
    return lista

def showAll(lista):
    for avion in lista:
        print(toString(avion))

def uiCelMaiMarePret(lista):
    rezultat = cel_mai_mare_pret_pentru_clase(lista)
    for i in rezultat:
        print("Pentru clasa {}, pretul maxim este{}".format(i, rezultat[i]))

def uiOrdonareRezervari(lista):
    showAll(ordonare_rezervari_descresc(lista))

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
        elif optiune == "4":
            lista = ui_mutare_la_clasa_superioara(lista)
        elif optiune == "5":
            lista =  ui_ieftinire_procentaj(lista)
        elif optiune == "6":
            lista = uiCelMaiMarePret(lista)
        elif optiune == "7":
            lista = uiOrdonareRezervari(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")