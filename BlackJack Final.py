import random
import time

j1 = input("Digite o nome do Jogador1: ")
j2 = input("Digite o nome do Jogador2 (Dealer): ")
iniciar = input("Digite 'S' para iniciar o jogo: ")

s1 = 0
s2 = 0
n1 = True
n2 = False
start = True 


def DistribuicaoDeCartas():
        print("Cartas sendo distribuídas.")
        time.sleep(1)
        print("Cartas sendo distribuídas..")
        time.sleep(1)
        print("Cartas sendo distribuídas...")
        time.sleep(1)
        print("Cartas sendo distribuídas....")
        time.sleep(1)
        print("Cartas sendo distribuídas.....")
        return

def VerificarVencedor():
    if (s1 == s2):
        print("Jogo empatado!")
        n1=False
        n2=False
        start = False
    elif (s1 > s2):
        print("Jogador ",j1," venceu!!!", "O resultado foi de ","(",s1 , ")", " do jogador e ","(",s2 , ")", " do Dealer")
        n1=False
        n2=False
        start =False
    elif (s2 > s1):
        print("Dealer ",j2," venceu!!!", "O resultado foi de ","(",s1 , ")", " do jogador e ","(",s2 , ")", " do Dealer")
        n1=False
        n2=False
        start =False
    return
    
if (iniciar == "s" or iniciar == "S"):
    start =True
    print("Tudo pronto para o grande jogo entre ", j1, " e o Delaer ", j2,". Que vença o melhor!")

while (start):  
    DistribuicaoDeCartas()
    s1 = random.randrange(1,10)
    print("Jogador", j1," recebeu uma carta, no valor", "(",s1 , ")")
    time.sleep(2)
    s1 += random.randrange(1,10)
    print("Jogador", j1," recebeu mais uma carta, totalizando", "(",s1 , ")")
    time.sleep(2)
    s2 = random.randrange(1,10)
    print("Jogador", j2," (Dealer) recebeu uma carta, totalizando", "(" ,s2 , ")")
    time.sleep(2)


    while(n1 == True):
        nCarta1 = input("Jogador 1 deseja uma nova carta? Digite 'S' para sim e 'N' para não.")
    
        if (nCarta1 == "s" or nCarta1 == "S"):
            s1 += random.randrange(1,10)
            print("Jogador", j1, " recebeu mais uma carta, totalizando", "(",s1 , ")")
            if (s1 > 21):
                n1=False
                start=False
                print("Jogador", j1, " perdeu!!! O somatório das cartas recebida foi de ", "(",s1 , ")"," Tente outra vez!")

        elif (nCarta1 == "n" or nCarta1 == "N"):
            n2=True

        while(n2 == True):
            nCarta2 = input("O Dealer deseja uma nova carta? Digite 'S' para sim e 'N' para não.")

            if (nCarta2 == "s" or nCarta2 == "S"):
                s2 += random.randrange(1,10)
                print("Jogador", j2, " recebeu mais uma carta, totalizando", "(",s2 , ")")
                if (s2 > 21):
                    n1=False
                    n2=False
                    start=False
                    print("Dealer ", j2, " perdeu!!! O somatório das cartas recebida foi de ", "(",s2 , ")"," Parabéns ", j1, "!!!!!!")

            elif (nCarta2 == "n" or nCarta2 == "N" ):
                VerificarVencedor()
                n1=False
                n2=False
                start =False
                
