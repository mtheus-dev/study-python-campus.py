import re

"Caminho da mensagem --> Computador A → Switch → Roteador 1 → Roteador 2 → Computador B"

def menu():
    '''SIMULADOR DO MODELO TCP/IP
        1 - Transmissão normal
        2 - Segmentos fora de ordem
        3 - TTL insuficiente
        4 - Encerrar'''
    
    def opcoes(opcao):
        if opcao == 1:
            pass
            #frase = input("Digite sua frase: ")
            #for i in range (len(frase)):
        elif opcao == 2:
            frase = input("Digite sua frase: ")
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        else:
            pass
            
    while True:

        try:
            resposta = int(input("Escolha uma das opções acima: "))

            if resposta >= 1 or resposta <= 4:

                print("O trabalho foi enviado com sucesso")
                
                return resposta

            else:
                print("Esse número não está presente no menu. Tente novamente")

        except :
            print("Só aceitamos entradas númericas. Tente novamente")



numero = "98490238409324"

variavel = re.findall(f"{.3}", numero)

print(variavel)
    


