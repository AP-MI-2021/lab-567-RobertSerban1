from Domain.avion import getId, getClasa
from Logic.CRUD import adauga_rezervare, getbyId
from Logic.functionalitati import ordonare_rezervari_descresc, mutare_la_clasa_superioara


def test_mutare_la_clasa_superioara():
    lista = []
    lista = adauga_rezervare("1", "Robert", "economy ", 100, "da", lista)
    lista = adauga_rezervare("2", "Robert", "economy plus", 450, "nu", lista)
    lista = adauga_rezervare("3", "Robert", "business", 600, "da", lista)
    rezultat = mutare_la_clasa_superioara("Robert", lista)
    assert getClasa(getbyId("1", rezultat)) == "economy plus"
    assert getClasa(getbId("1", rezultat)) == "business"
    assert getClasa(getbyId("3", rezultat)) == "business"

def test_ieftinire_procentaj():
    lista = []
    lista = adauga_rezervare("1", "Robert", "economy", 100, "da", lista)
    lista = adauga_rezervare("2", "Robert", "economy plus", 400, "nu", lista)
    lista = adauga_rezervare("3", "Robert", "business", 600, "da", lista)
    rezultat = ieftinire_procentaj(50, lista)
    assert getPret(getbyId("1", rezultat)) == 50
    assert getPret(getbyId("2", rezultat)) == 200
    assert getPret(getbyId("3", rezultat)) == 300

def test_ordonare_rezervari_descresc():
    lista = []
    lista = adauga_rezervare("1", "Ionescu", "economy", 200, "da", lista)
    lista = adauga_rezervare("2", "Popescu", "business", 300, "nu", lista)
    rezultat = ordonare_rezervari_descresc(lista)
    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "1"

def test_cel_mai_mare_pret_pentru_clase():
    lista = []
    lista = adauga_rezervare("1", "Ion", "economy", 500, "da", lista)
    lista = adauga_rezervare("2", "George", "economy", 400, "da", lista)
    lista = adauga_rezervare("3", "Ionut", "economy plus ", 600, "nu", lista)
    rezultat = cel_mai_mare_pret_pentru_clase(lista)
    assert rezultat["economy"] == 500
    assert rezultat["economy plus"] == 600