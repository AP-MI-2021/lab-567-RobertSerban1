from Logic.CRUD import adauga_rezervare, getbyId
from Logic.functionalitati import get_undo_list
from UI.console import ui_undo, ui_redo


def test_undo_redo():
    lista = []
    undoList = []
    redoList = []
    undoList = get_undo_list(lista, undoList)
    lista = adauga_rezervare("1", "a", "economy", 50, "da", lista)
    undoList = get_undo_list(lista, undoList)
    lista = adauga_rezervare("2", "b", "economy plus", 100, "da", lista)
    undoList = get_undo_list(lista, undoList)
    lista = adauga_rezervare("3", "c", "business", 150, "da", lista)
    assert len(lista) == 3
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is not None
    assert getbyId("3", lista) is not None
    lista = ui_undo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is not None
    assert getbyId("3", lista) is None
    lista = ui_undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    lista = ui_undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getbyId("1", lista) is None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    lista = ui_undo(lista, undoList, redoList)
    assert len(lista) == 0
    undoList = get_undo_list(lista, undoList)
    redoList.clear()
    lista = adauga_rezervare("1", "a", "economy", 50, "da", lista)
    undoList = get_undo_list(lista, undoList)
    redoList.clear()
    lista = adauga_rezervare("2", "b", "economy plus", 100, "da", lista)
    undoList = get_undo_list(lista, undoList)
    redoList.clear()
    lista = adauga_rezervare("3", "c", "business", 150, "da", lista)
    assert len(lista) == 3
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is not None
    assert getbyId("3", lista) is not None
    lista = ui_redo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is not None
    assert getbyId("3", lista) is not None
    lista = ui_undo(lista, undoList, redoList)
    lista = ui_undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    lista = ui_redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is not None
    assert getbyId("3", lista) is None
    lista = ui_redo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is not None
    assert getbyId("3", lista) is not None
    lista = ui_undo(lista, undoList, redoList)
    lista = ui_undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    undoList = get_undo_list(lista, undoList)
    redoList.clear()
    lista = adauga_rezervare("4", "d", "business", 150, "nu", lista)
    assert len(lista) == 2
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    assert getbyId("4", lista) is not None
    lista = ui_redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    assert getbyId("4", lista) is not None
    lista = ui_undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    assert getbyId("4", lista) is None
    lista = ui_undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getbyId("1", lista) is None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    assert getbyId("4", lista) is None
    lista = ui_redo(lista, undoList, redoList)
    lista = ui_redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    assert getbyId("4", lista) is not None
    lista = ui_redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getbyId("1", lista) is not None
    assert getbyId("2", lista) is None
    assert getbyId("3", lista) is None
    assert getbyId("4", lista) is not None