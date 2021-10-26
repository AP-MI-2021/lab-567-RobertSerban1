from Domain.avion import creeaza_zbor_avion, getId, getNume, getClasa, getPret, getCheckin


def testRezervare():
    avion = creeaza_zbor_avion("1", "Ionescu", "economy", 100, "da")

    assert getId(avion) == "1"
    assert getNume(avion) == "Ionescu"
    assert getClasa(avion) == "economy"
    assert getPret(avion) == 100
    assert getCheckin(avion) == "da"
