from Domain.avion import creeaza_zbor_avion, getId


def adauga_rezervare(id, nume, clasa, pret, checkin, lista):
    """
    adauga o rezervare intr-o lista
    :param id: id-ul biletului
    :param nume: numele de pe rezervare
    :param clasa: clasa biletului
    :param pret: pretul biletului
    :param checkin: confirmarea checkin-ului
    :param lista: o noua lista
    :return: o lista continand vechea lista + noua rezervare de bilet de avion
    """
    if getbyId(id, lista) is not None:
        raise ValueError("Id-ul introdus exista deja.")
    avion = creeaza_zbor_avion(id, nume, clasa, pret, checkin)
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ.")
    return lista + [avion]

def getbyId(id, lista):
    """
    ia rezervarea cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de rezervari
    :return: rezervarea cu id-ul dat sau None in caz ca nu exista
    """
    for avion in lista:
        if getId(avion) == id:
            return avion
    return None

def sterge_rezervare(id, lista):
    """
    sterge o rezervare din lista
    :param id: string
    :param lista: lista cu rezervari
    :return: o lista noua fara cea stearsa
    """
    if getbyId(id, lista) is None:
        raise ValueError("Id-ul introdus exista deja.")
    return [avion for avion in lista if getId(avion) != id]

def modifica_rezervare(id, nume, clasa, pret, checkin, lista):
    """
    modifica o rezervare
    :param id: id-ul dupa care se face modificarea
    :param nume: noul nume
    :param clasa: noua clasa
    :param pret: noul pret
    :param checkin: noul checkin
    :param lista: noua lista
    :return: rezervarea modificata
    """
    if getbyId(id, lista) is None:
        raise ValueError("Id-ul introdus exista deja.")
    listaNoua = []
    for avion in lista:
        if getId(avion) == id:
            rezervareNoua = creeaza_zbor_avion(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(avion)
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ.")
    return listaNoua




