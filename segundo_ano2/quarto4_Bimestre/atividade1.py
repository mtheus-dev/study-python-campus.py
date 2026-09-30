def tupla():

    contatos = ("Emilly","Mãe","chefe/Vitor","CCOM","2ºB Infor")

    print("__"*20)

    if "Mãe" in contatos:
        print("Sim, eu amo a minha Mãe de todo meu coração")

    print("__"*20)

    print("Por quem o matheus é apaixonado?")
    print("Resposta: ",contatos[0])

    print("__"*20)

    print("O Matheus e de qual classe?")
    print("Resposta: ",contatos[-1])

def lista():

    lista_de_amigos = ["Deus","juan","Deivid","Julian","Amanda"]

    print("__"*20)

    print("LISTA DE AMIGOS")
    print(lista_de_amigos)

    print("__"*20)

    print(f"O {lista_de_amigos[1]} é uma amigo?")

    print("__"*20)

    print("Quem é o professor do Matheus?")
    print(f"Resposta: {lista_de_amigos[2]}")

    print("__"*20)

    print("Pedro foi adicionado na lista de amigos")
    lista_de_amigos.append("Pedro")

    print("__"*20)

    print("LISTA DE AMIGOS")
    print(lista_de_amigos)

    print("__"*20)

    print(f"Por quem o juan é PERDIDAMENTE apaixonado?")
    print(f"Resposta: {lista_de_amigos[-1]}")

    print("__"*20)

    lista_de_amigos.remove("juan")
    print("juan foi saiu da lista de amigos por ter sido rejeitado pelo Pedro.")

    print("__"*20)    

    print("LISTA DE AMIGOS")
    print(lista_de_amigos)
    
    print("__"*20)

    lista_de_amigos.insert(1,"Pato")
    print("Pato foi adicionado na listada de amigos. ")

    print("__"*20)

    print("LISTA DE AMIGOS")
    print(lista_de_amigos)

    print("__"*20)

    lista_de_amigos.pop(5)
    print("Pedro saiu do grupo para ir atraz do juan, porque percerbeu que ama ele também. ")

    print("__"*20)

    print("LISTA DE AMIGOS")
    print(lista_de_amigos)

    print("__"*20)

lista()