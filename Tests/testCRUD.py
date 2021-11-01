from Domain.avion import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adauga_rezervare, sterge_rezervare, getbyId, modifica_rezervare


def test_adauga_rezervare():
    lista = adauga_rezervare("1", "Ionescu", "economy", 100, "da", [])

    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert getNume(lista[0]) == "Ionescu"
    assert getClasa(lista[0]) == "economy"
    assert getPret(lista[0]) == 100
    assert getCheckin(lista[0]) == "da"

def test_sterge_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Ionescu", "economy", 100, "da", lista)
    lista = adauga_rezervare("2", "Popescu", "business", 300, "nu", lista)
    lista = sterge_rezervare("1", lista)

    assert len(lista) == 1
    assert getbyId("1", lista) is None

def test_modifica_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Ionescu", "economy", 100, "da", lista)
    lista = adauga_rezervare("2", "Popescu", "business", 300, "nu", lista)
    lista = modifica_rezervare("1", "Iliescu", "business", 150, "nu", lista)

    rezervare_update = getbyId("1", lista)
    assert getId(rezervare_update) == "1"
    assert getNume(rezervare_update) == "Iliescu"
    assert getClasa(rezervare_update) == "business"
    assert getPret(rezervare_update) == 150
    assert getCheckin(rezervare_update) == "nu"

def test_getbyId():
    lista = []
    lista = adauga_rezervare("1", "Ionescu", "economy", 100, "da", lista)
    lista = adauga_rezervare("2", "Popescu", "business", 300, "nu", lista)

    assert getNume(getbyId("1", lista)) == "Ionescu"