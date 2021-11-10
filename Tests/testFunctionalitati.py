from Domain.avion import getId, getClasa, getPret
from Logic.CRUD import adauga_rezervare, getbyId
from Logic.functionalitati import ordonare_rezervari_descresc, mutare_la_clasa_superioara, ieftinire_procentaj, \
    cel_mai_mare_pret_pentru_clase, afis_sum_pret_dupa_nume


def test_mutare_la_clasa_superioara():
    lista = []
    lista = adauga_rezervare("1", "Robert", "economy", 100, "da", lista)
    lista = adauga_rezervare("2", "Robert", "economy plus", 450, "nu", lista)
    lista = adauga_rezervare("3", "Robert", "business", 600, "da", lista)
    rezultat = mutare_la_clasa_superioara("Robert", lista)
    assert getClasa(getbyId("1", rezultat)) == "economy plus"
    assert getClasa(getbyId("2", rezultat)) == "business"
    assert getClasa(getbyId("3", rezultat)) == "business"

def test_ieftinire_procentaj():
    lista = []
    lista = adauga_rezervare("1", "Albert", "economy", 40.0, "da", lista)
    lista = adauga_rezervare("2", "Robert", "economy plus", 45.0, "nu", lista)
    lista = adauga_rezervare("3", "Andrei", "business", 60.0, "da", lista)
    lista = adauga_rezervare("4", "Cristian", "business", 60.0, "nu", lista)
    lista_noua = ieftinire_procentaj(20, lista)
    assert getPret(getbyId("1", lista_noua)) == 32.0
    assert getPret(getbyId("2", lista_noua)) == 45.0
    assert getPret(getbyId("3", lista_noua)) == 48.0
    assert getPret(getbyId("4", lista_noua)) == 60.0
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
    lista = adauga_rezervare("3", "Ionut", "economy plus", 600, "nu", lista)
    rezultat = cel_mai_mare_pret_pentru_clase(lista)
    assert rezultat["economy"] == 500
    assert rezultat["economy plus"] == 600

def test_afis_sum_pret_dupa_nume():
    lista = []
    lista = adauga_rezervare("1", "a", "economy", 30.0, "da", lista)
    lista = adauga_rezervare("2", "b", "economy", 45.0, "da", lista)
    lista = adauga_rezervare("3", "b", "economy", 20.2, "da", lista)
    lista = adauga_rezervare("4", "a", "economy plus", 60.0, "da", lista)
    lista = adauga_rezervare("5", "c", "economy plus", 70.0, "da", lista)
    lista = adauga_rezervare("6", "d", "business", 80.0, "da", lista)
    lista = adauga_rezervare("7", "c", "business", 90.0, "nu", lista)
    lista_sume = afis_sum_pret_dupa_nume(lista)
    assert len(lista_sume) == 4
    assert lista_sume[0] == ["a", 90.0]
    assert lista_sume[1] == ["b", 65.2]
    assert lista_sume[2] == ["c", 160.0]
    assert lista_sume[3] == ["d", 80.0]