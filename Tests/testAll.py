from Tests.testCRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare, test_getbyId
from Tests.testDomain import testRezervare


def runAllTests():
    testRezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_getbyId()