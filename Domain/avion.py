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
    return {
        "id" : id,
        "nume" : nume,
        "clasa" : clasa,
        "pret" : pret,
        "checkin" :checkin
    }
def getId(avion):
    """
    ia id-ul rezervarii biletului de avion
    :param avion: un dictionar de tip avion
    :return: id-ul rezervarii - string
    """
    return avion["id"]

def getNume(avion):
    return avion["nume"]

def getClasa(avion):
    return avion["clasa"]

def getPret(avion):
    return avion["pret"]

def getCheckin(avion):
    return avion["checkin"]

def toString(avion):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin:{}".format(
        getId(avion),
        getNume(avion),
        getClasa(avion),
        getPret(avion),
        getCheckin(avion)
    )
def toString(avion):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(avion),
        getNume(avion),
        getClasa(avion),
        getPret(avion),
        getCheckin(avion)
    )
