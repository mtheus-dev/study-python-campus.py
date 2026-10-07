def exemplo_1():

    esseDicionario = {
        "marca": "FORDE",
        "modelo": "Mustang",
        "ano": 1964}

    print(esseDicionario)

    esseDicionario["modelo"] = "Pedro"
    esseDicionario["marca"] = "Juan"
    esseDicionario["ano"] = 67
    x = esseDicionario["modelo"]

    print(x)

    print(esseDicionario)


def exemplo_2():
    Palestras = {"1":"Django","2":"Java","3":"React","4": "Docker", "5": "PHP" }

    print(list(Palestras.keys()))
    print(list(Palestras.values()))
    print(list(Palestras.items()))

def exemplo_3():
    filme_que_eu_vi = {
        "nome":"The Quintessential Quintuplets: O Filme",
        "ano":"2022",
        "diretor":"Masato Jinbo",
        "nota": 8.2}

    print(filme_que_eu_vi)

    filme_que_eu_vi.update (
        {   "nome":"The Quintessential Quintuplets: O Filme",
            "ano":"2022",
            "diretor":"Masato Jinbo",
            "nota": 8.2,
            "Genero principal": "trauma psicologico"})

    print(filme_que_eu_vi)

