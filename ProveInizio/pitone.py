def Menu():
 x=1  #metodo menu dove vengono mostrate le opzioni disonibili
 scelta=2
 while scelta >1:
    print("======Menu=======")
    for x ,opzione in enumerate( listaopzioni,start=1):
          print(f"[{x}] {opzione} ")#Stampa opzioni
    scelta=int(input("->"))
    Scelta(scelta)#La scelta viene inviata al suo metodo

def Scelta( scelta):#metodo scelta
    if scelta==1:
        InserisciPersona()#se scelta =1 inserimento
        return 1
    if scelta ==2:
        
        Visualizza()#se scelta =2 visualizza
        return 1
    if scelta== 3:
        RimuoviPersona()#se scelta =3 rimuovi persona
        return 1
    else:
        return 0 #altrimenti ritorna 0 e  torna direttamante a Menu
def InserisciPersona():#metodo inserimento
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    eta = int(input("Inserisci l'eta: "))#chiedo nome cognome eta
    persona = Persona(nome, eta, cognome)
    listaPersone.append(persona)# e aggiungo alla lista la persona

def Visualizza():#metodo visualizza
    for i in listaPersone:#stampa nome cognome ed età
        print("nome:",i.nome,"cognome:",i.cognome,"eta:",i.eta)
    
def RimuoviPersona():#metodo rimozione
    nome=input("Inserisci il nome della persona che vuoi rimuovere:")
    cognome=input("Inserisci il cognome della persona che vuoi rimuovere:")
    eta=int(input("Inserisci l'età della persona da rimuovere:"))#Chiedo i dari della persona da rimuovere
    for x in listaPersone:
        if x.nome==nome and x.cognome==cognome and x.eta==eta:#controllo che tutti e i 3 campi siano uguali
            listaPersone.remove(x)
            break

class Persona:#dichiaro la classe persona
    nome=""
    cognome=""# attributi nome,cognome ed età
    eta=""
    def __init__(self, nome, eta,cognome):#costruttore
     self.nome = nome
     self.eta = eta
     self.cognome=cognome

listaopzioni=["Inserisci","Visualizza","Rimuovi","Esci"]#dichiaro la lista che contiene le opzioni
listaPersone=[Persona]
scelta=""
Menu()#chiamo il metodo menu

         