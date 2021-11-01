from Logic.CRUD import adauga_rezervare
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []

    runMenu(lista)
main()