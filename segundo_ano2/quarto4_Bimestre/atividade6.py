class excecaoNumeroMuitoGrande (Exception):
    pass

class excecaoNumeroNegativo (Exception):
    pass

while True:

    try:

        nota = int(input("Digite uma nota de 0 a 100: "))

        if nota > 100:

            raise excecaoNumeroMuitoGrande

        elif nota < 0:

            raise excecaoNumeroNegativo
    
        else:

            print(f"Sua nota é: {nota}")

            break
            
    except excecaoNumeroMuitoGrande:
        print("Você digitou um número maior 100. Tente novamente")

    except excecaoNumeroNegativo:
        print("Você digitou um número menor que 0. Tente novamente")

    except ValueError:
        print("ESCREVA UM NÚMERO SEU ANIMAL!!!!!")