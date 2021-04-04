import random

def i():
    banner = """
    ***********************
    *** Decida por mim! ***
    ***********************
    """

    print(banner)


    recebendo = input("Digite aqui uma pergunta: ")

    while(recebendo):



        resp1 = "Sim, vai la"
        resp2 = "Tudo bem e voce?"
        resp3 = "Nao me faca essas perguntas, seu mal carater"
        resp4 = "Eu tenho 1 hora de nascido"
        resp5 = "Tambem gostaria de saber."
        resp6 = "Voce denovo?"
        resp7 = "Eu gosto de animes"
        resp8 = "Meu nome eh toto"
        resp9 = "Nao consigo te responder agora"
        resp10 = "Seu lindo, depois nos falamos, agora estou ocupado"
        lista = [resp1, resp2, resp3, resp4, resp5, resp6, resp7, resp8, resp9, resp10]
        resp = random.choice(lista)



        print(resp)

        print("Deseja perguntar novamente?")
        print("(1)Sim  (2)Nao")
        a = int(input("Digite: "))

        if(a == 1):
            i()
        elif(a == 2):
            break
        break

if(__name__, "__main__"):
    i()



