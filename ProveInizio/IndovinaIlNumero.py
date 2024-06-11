def GeneraNum():
    import random
    return random.randint(1,20)
nTurni=0
nPunti=0
print("Hey benvenuto a Indovina il Numero, quanto turni vuoi fare?")
nTurni=int(input())
if nTurni<0 or nTurni==0:
    exit
while nTurni>0:
    num=GeneraNum()
    numUtente=int(input("Inserisci il tuo numero-->"))
    if numUtente==num:
        print("Congratulazioni hai indovinato")
        nPunti+=1
    else:
        print("Mi dispiace, il numero era",num)
        nTurni-=1
print("Grazie per aver giocato, hai fatto",nPunti)