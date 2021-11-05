from Tests.testAll import runAllTests
from UI.command_line_console import command_line
from UI.console import runMenu


def main():
    lista = []
    runAllTests()
    print("Apasati '1' pentru a accesa primul meniu, iar '2' pentru ce-l de-al doilea meniu")
    p = input("Alegeti meniul: ")
    if p == '1':
        command_line(lista)
    elif p == '2':
        runMenu(lista)

main()