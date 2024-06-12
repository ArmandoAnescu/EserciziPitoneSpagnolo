#to do:
#Precisione
#Pokemon predefinit, pokemon già fatti e con moveset predefinito, sistema di scelta
#Level Up and Evolution System, un sistema degli exp che permette a un PkMn di evolversi al livello predefinito ex:charmeleon in charizard al 36
#
class Level:
    expAccumulated=0
    def __init__(self,livello):
        self.level=livello
    def CalcolaLevelEsp(self,expReceived):
        import math
        expNextLvl=int (((math.sqrt(self.level)/2)*10)*8)
        self.expAccumulated +=expReceived
        if expNextLvl== self.expAccumulated:
            self.level +=1
        else:
            print(f"Mancano {expNextLvl-self.expAccumulated} per raggiungere il prossimo livello")
        
class Move:
    moveName=""
    def __init__(self, name, type, Dmg):
        self.moveName=name
        self.movetype=type
        self.moveDmg=Dmg
        
class Stats:
    def __init__(self, HP, Atk, Def):
        self.HP=HP
        self.Atk=Atk
        self.Def=Def
        self.SpAtk=Atk+((Atk*110)/100)
        self.SpDef=Def+((Def*110)/100)
        
    def printStats(self):
        print(f"HP: {self.HP}")
        print(f"Attacco: {self.Atk}")
        print(f"Difesa: {self.Def}")
        print(f"Attacco Speciale: {self.SpAtk}")
        print(f"Difesa Speciale: {self.SpDef}")
        
class Pokemon:
    movesList=[]
    
    def __init__(self, name, type, hp, attack, defense,moves,level):
        self.name = name
        self.type = type
        self.stats=Stats(HP=hp,Atk=attack,Def=defense)
        self.movesList=moves
        self.lvl=level
        
    def newMove(self,move):
        if(len(self.movesList)==4):
            print("non puoi più aggiungere mosse")
            print("scegli la mossa che vuoi sostituire")
            for i in range(len(self.movesList)):
                print(f"{i+1}. {self.movesList[i].moveName}")
            choice=input("what's your choice?->")
            self.movesList.pop(choice)
            self.movesList.append(move)
        else:
            self.movesList.append(move)
            
    def printMoves(self):
        for i in range(len(self.movesList)):
            print(f"{i+1}. {self.movesList[i].moveName}")
starter=[Pokemon("Treeko","Erba",20,20,20,moves=[Move("Azione","normale",20),Move("Semitraglia","erba","35")])]
urPkMn=[]
oppPkMn=[]
opzioni=["Lotta","Vedi i miei Pkmn","Aggiungi Pkmn","RimuoviPkmn","Esci"]

def Visualizza(lista):
    for i in range(len(lista)):
        print(f"{i+1}. {lista[i].name} {lista[i].type}")
        print(f"{lista[i].stats.printStats()}")
        print(f"{lista[i].printMoves()}")
        
def RimuoviPkMn(lista):
    print("ATTENZIONE! Sei sicuro di voler liberare questo pokemon? L'esperienza accumulata verra persa insieme al pokemon y/n:")
    scelta=input()
    if scelta=="y" or scelta=="si" or scelta=="yes" or scelta=="sì":
        remove=input("inserisci il nome del pokemon da rimuovere:")
        for i in lista:
            if i.name==remove:
                lista.remove(i)
                print("Rimozione avvenuta con successo!!")
                return
        print("pokemon non trovato")
        return 0
    else:
        print("Operazione annullata")
        return 1
    
        
def Menu():
    while True:
        print("cosa vuoi fare?")
        for i in range(len(opzioni)):
            print(f"{i+1}. {opzioni[i]}")
        choice=int(input("->"))
        if choice==1:
            print("Scusa funzione non disponibile")
        elif choice==2:
            Visualizza(urPkMn)
        elif choice ==3:
            if len(urPkMn)<5:
                urPkMn.append(createPokemon())
            else:
                print("hai già 6 pokemon non puoi averne di più")
        elif choice==4:
             RimuoviPkMn()
        elif choice==5:
            break
        else:
            print("Mi dispiace non c' una funzione numero",choice)

def createPokemon():
    name=input("nome del pokemon->")
    type=input("tipo del pokemon->")
    hp=int(input("hp del pokemon->"))
    attack=int(input("attacco del pokemon->"))
    defense=int(input("difesa del pokemon->"))
    moves=[]
    for i in range(4):
        moveName=input(f"nome della mossa {i+1}->")
        if(moveName==" " or moveName== ""):
            continue
        moveType=input(f"tipo della mossa {i+1}->")
        moveDmg=int(input(f"danno della mossa {i+1}->"))
        moves.append(Move(moveName,moveType,moveDmg))
    return Pokemon(name,type,hp,attack,defense,moves)
nPkmn=int(input("Quanti pokemon vuoi? Max 6:"))
for i in range(nPkmn):
    urPkMn.append(createPokemon())
Menu()
            