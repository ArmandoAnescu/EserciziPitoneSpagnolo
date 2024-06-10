def Menu():
 x=1
 scelta=2
 while scelta >1:
    print("======Menu=======")
    for x ,opzione in enumerate( listaopzioni,start=1):
          print(f"[{x}] {opzione} ")
    scelta=int(input("->"))
    Scelta(scelta)

def Scelta( scelta):
    if scelta==1:
        InserisciPersona()
        return 1
    if scelta ==2:
        RimuoviPersona()
        return 1
    if scelta== 3:
        Visualizza()
        return 1
    else:
        return 0
def InserisciPersona():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    eta = int(input("Inserisci l'eta: "))
    persona = Persona(nome, eta, cognome)
    listaPersone.append(persona)

def Visualizza():
    for i in listaPersone:
        print("nome:",i.nome,"cognome:",i.cognome,"eta:",i.eta)
    
def RimuoviPersona():
    nome=input("Inserisci il nome della persona che vuoi rimuovere:")
    cognome=input("Inserisci il cognome della persona che vuoi rimuovere:")
    eta=int(input("Inserisci l'età della persona da rimuovere:"))
    for x in listaPersone:
        if x.nome==nome and x.cognome==cognome and x.eta==eta:
            listaPersone.remove(x)
            break

class Persona:
    nome=""
    cognome=""
    eta=""
    def __init__(self, nome, eta,cognome):
     self.nome = nome
     self.eta = eta
     self.cognome=cognome

listaopzioni=["Inserisci","Rimuovi","Visualizza","Esci"]
listaPersone=[Persona]
scelta=""
Menu()

         