def erro_1():
    "Silvio está tentando converter uma string em um número inteiro. Crie um programa em Python que solicite uma string, tente convertê-la e utilize try/except/else/finally para lidar com exceções como ValueError."


    while True:

        numero_str = input("Digite o número que gostaria de converter: ")

        try:

            print(f"eu acho que isso {int(numero_str)}👍 realmente é um número")
            break

        except ValueError:
            print(" UM NÚMERO!!!!!")

        finally:
            print("deu certo")

def erro_2():
    while True:

        try:

            nota = int(input("Digite sua nota sua nota: "))

            if nota < 0 or nota > 10:
                raise Exception 

            print(f"Sua nota é: {nota}")
            break

        except ValueError:
            print("Coloque um número")

        except Exception:
            print("Só aceitamos notas de 0 a 10")

erro_2()