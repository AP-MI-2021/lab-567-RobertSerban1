from Tests.testCRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare, test_getbyId
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import test_ordonare_rezervari_descresc, test_mutare_la_clasa_superioara, \
    test_ieftinire_procentaj, test_cel_mai_mare_pret_pentru_clase


def runAllTests():
    testRezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_getbyId()
    test_ordonare_rezervari_descresc()
    test_mutare_la_clasa_superioara()
    test_ieftinire_procentaj()
    test_cel_mai_mare_pret_pentru_clase()