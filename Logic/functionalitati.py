from Domain.avion import getClasa, getCheckin, getPret, getNume

def mutare_la_clasa_superioara(nume, lista):
    lista_noua = []
    for avion in lista:
        if getNume(avion) == nume:
            if getClasa(avion) == "economy":
                avion[2] = "economy plus"
            elif getClasa(avion) == "economy plus":
                avion[2] = "business"
        lista_noua.append(avion)
    return lista_noua


def ieftinire_procentaj(percent, lista):
    percent_str = str(percent)
    if percent_str.isdigit() is False and percent < 0:
        raise ValueError("Nu ati introdus o valoare valida!")
    lista_noua = []
    for avion in lista:
        if getCheckin(avion) == "da":
            price = int(getPret(avion))
            price = int(price - int(percent) / 100 * price)
            avion[3] = price
        lista_noua.append(avion)
    return lista_noua


def cel_mai_mare_pret_pentru_clase(lista):
    rezultat = {}
    for avion in lista:
        clasa = getClasa(avion)
        pret = getPret(avion)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
             rezultat[clasa] = pret
    return rezultat

def ordonare_rezervari_descresc(lista):
    return sorted(lista, reverse=True, key=getPret)
def afis_sum_pret_dupa_nume(lista):
    nume = []
    for avion in lista:
        nume.append(getNume(avion))
    no_duplicates = []
    for i in nume:
        if i not in no_duplicates:
            no_duplicates.append(i)
    sume = []
    for x in no_duplicates:
        s = 0
        for avion in lista:
            if x == getNume(avion):
                s += getPret(avion)
        sume.append([x, s])
    return sume

def get_undo_list(lista, undoLista):
    undoLista.append(lista)
    return undoLista

