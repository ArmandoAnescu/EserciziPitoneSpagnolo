class Auto:
    modello=""
    marca=""
    targa=""
    cilindrata=0
    def __init__(self,modello,marca,targa,cilindrata):#classe auto con attributi modello,marca,cilindrata e targa
        self.cilindrata=cilindrata
        self.modello=modello
        self.marca=marca
        self.targa=targa
       
def Menu():
 x=1  #metodo menu dove vengono mostrate le opzioni disonibili
 scelta=2
 while scelta !=4:
    print("======Menu=======")
    for x ,opzione in enumerate( listaopzioni,start=1):
          print(f"[{x}] {opzione} ")#Stampa opzioni
    scelta=int(input("->"))
    Scelta(scelta)#La scelta viene inviata al suo metodo

def Scelta( scelta):#metodo scelta
    if scelta==1:
        InserisciAuto()#se scelta =1 inserimento
        return 1
    if scelta ==2:
        
        Visualizza()#se scelta =2 visualizza
        return 1
    if scelta== 3:
        RimuoviPersona()#se scelta =3 rimuovi auto
        return 1
    else:
        return 0 #altrimenti ritorna 0 e  torna direttamante a Menu
def InserisciAuto():#metodo inserimento
    marca = input("Inserisci la marca: ")
    targa = input("Inserisci la targa: ")
    modello = input("Inserisci il modello: ")
    cilindrata = int(input("Inserisci la cilindrata "))#chiedo modello targa cilindrata e marca
    macchina= Auto(modello=modello,marca=marca,targa=targa,cilindrata=cilindrata)
    listaAuto.append(macchina)# e aggiungo alla lista l'auto

def Visualizza():#metodo visualizza
    for self in listaAuto: #ciclo for per stampare le auto
        print(f"Marca:{self.marca} modello:{self.modello} cilindrata{self.cilindrata} targa:{self.targa}")
    
def RimuoviPersona():#metodo rimozione
    marca=input("Inserisci la marca dell'auto che vuoi rimuovere:")
    modello=input("Inserisci il modello dell'auto che vuoi rimuovere:")
    targa=int(input("Inserisci la targa dell'auto da rimuovere:"))#Chiedo i dati dell'auto da rimuovere
    for x in listaAuto:
        if x.targa==targa and x.modello==modello and x.marca==marca:#controllo che tutti i campi siano uguali
            listaAuto.remove(x)
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
listaAuto=[]
scelta=""
Menu()#chiamo il metodo menu

         
        