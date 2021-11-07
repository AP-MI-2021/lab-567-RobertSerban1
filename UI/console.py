from Domain.avion import toString, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import ordonare_rezervari_descresc, cel_mai_mare_pret_pentru_clase, \
    mutare_la_clasa_superioara, ieftinire_procentaj, afis_sum_pret_dupa_nume


def printMenu():
    print("1. Adaugare rezervare bilet de avion")
    print("2. Stergere rezervare bilet de avion")
    print("3. Modificare rezervare bilet de avion")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("6. Determinarea prețului maxim pentru fiecare clasă.")
    print("7. Ordonarea rezervărilor descrescător după preț.")
    print("8. Afisarea sumelor preturilor pentru fiecare nume.")
    print("u. Undo")
    print("a. Afisare toate rezervarile")
    print("x. Iesire")


def ui_adaugare_rezervare(lista, undoList):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        checkin = input("Dati checkin-ul: ")
        if clasa != "economy" and clasa != "economy plus" and clasa != "business":
            print("Eroare: Nu ati introdus o clasa valida!")
            return lista
        if checkin != 'da' and checkin != 'nu':
            print("Eroare: Trebuie sa introduceti 'da'/'nu' ")
            return lista
        lista = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
        return lista
        rezultat = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista[:])
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def uiStergeRezervare(lista, undoList):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        lista = sterge_rezervare(id, lista)
        return lista
        rezultat = sterge_rezervare(id, lista)
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print ("Eroare : {}".format(ve))
        return lista
def uiModificaRezervare(lista, undoList):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input("Dati noul pret: "))
        checkin = input("Dati noul checkin: ")
        if clasa != "economy" and clasa != "economy plus" and clasa != "business":
            print("Eroare: Nu ati introdus o clasa valida!")
            return lista
        if checkin != 'da' and checkin != 'nu':
            print("Eroare: Trebuie sa introduceti 'da'/'nu' ")
            return lista
        lista = modifica_rezervare(id, nume, clasa, pret, checkin, lista)
        return lista
        lista = modifica_rezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def ui_mutare_la_clasa_superioara(lista, undoList):
    nume = input("Dati numele persoanei: ")
    lista = mutare_la_clasa_superioara(nume, lista)
    return lista
    undoList.append(lista)
    rezultat = mutare_la_clasa_superioara(nume, lista)
    return rezultat


def ui_ieftinire_procentaj(lista, undoList):
    try:
        procentaj = input("Dati procentul: ")
        if procentaj.count('%') != 1:
            print("Eroare: Nu ati introdus corect procentajul!")
            return lista
        i = 0
        string = [procentaj[i:i + len(procentaj) - 1] for i in range(0, len(procentaj), len(procentaj) - 1)]
        percent = float(string[0])
        lista = ieftinire_rezervari(percent, lista)
        return lista
        rezultat = ieftinire_rezervari(percent, lista)
        undoList.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def showAll(lista):
    for avion in lista:
        print(toString(avion))

def uiCelMaiMarePret(lista):
    preturi = cel_mai_mare_pret_pentru_clase(lista)
    print("Preturile maxime pentru clasele economy/economy plus/business sunt: ", preturi)

def uiOrdonareRezervari(lista, undoList):
    rezultat = ordonare_rezervari_descresc(lista)
    undoList.append(lista)
    return rezultat

def ui_afis_sum_pret_dupa_nume(lista):
    lista_sume = afis_sum_pret_dupa_nume(lista)
    for x in lista_sume:
        y = "nume: {}, suma: {}".format(x[0], x[1])
        print(y)
def runMenu(lista):
    undoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adaugare_rezervare(lista, undoList)
        elif optiune == "2":
            lista = uiStergeRezervare(lista, undoList)
        elif optiune == "3":
            lista = uiModificaRezervare(lista, undoList)
        elif optiune == "4":
            lista = ui_mutare_la_clasa_superioara(lista, undoList)
        elif optiune == "5":
            lista =  ui_ieftinire_procentaj(lista, undoList)
        elif optiune == "6":
            lista = uiCelMaiMarePret(lista)
        elif optiune == "7":
            lista = uiOrdonareRezervari(lista, undoList)
        elif optiune == "8":
            lista = ui_afis_sum_pret_dupa_nume(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                lista = undoList.pop()
            else:
                print("Nu se mai poate face undo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")