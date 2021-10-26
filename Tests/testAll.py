from Tests.testCRUD import test_adauga_rezervare
from Tests.testDomain import testRezervare


def runAllTests():
    testRezervare()
    test_adauga_rezervare()