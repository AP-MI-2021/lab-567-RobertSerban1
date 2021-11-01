def creeaza_zbor_avion(id, nume, clasa, pret, checkin):
    """
    creeaza un dictionar ce retine datele despre o rezervare a unui bilet de avion
    :param id: id avion - string
    :param nume: numele personal - string
    :param clasa: clasa avionului - string
    :param pret: pretul biletului - float
    :param checkin: verificare checkin - string
    :return: un dictionar ce retine datele despre o rezervare a unui bilet de avion
    """
    return [id, nume, clasa, pret, checkin]
def getId(avion):
    """
    ia id-ul rezervarii biletului de avion
    :param avion: un dictionar de tip avion
    :return: id-ul rezervarii - string
    """
    return avion[0]

def getNume(avion):
    return avion[1]

def getClasa(avion):
    return avion[2]

def getPret(avion):
    return avion[3]

def getCheckin(avion):
    return avion[4]

def toString(avion):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        getId(avion),
        getNume(avion),
        getClasa(avion),
        getPret(avion),
        getCheckin(avion),
    )
