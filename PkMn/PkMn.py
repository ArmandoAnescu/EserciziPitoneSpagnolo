#to do:
#Precisione
#Pokemon predefinit, pokemon già fatti e con moveset predefinito, sistema di scelta
#Evolution System, un sistema degli exp che permette a un PkMn di evolversi al livello predefinito ex:charmeleon in charizard al 36
#
class Level:
    expAccumulated=0
    evolutionLvl=[]
    def __init__(self,livello,lvlEvo):
        self.level=livello
        self.evolutionLvl=lvlEvo
    def CalcolaLevelEsp(self,lvlDefeated):
        import math
        expReceived=int(math.pow(lvlDefeated^3)/12)
        expNextLvl=int (((math.pow(self.level,3)*4)/5))#calcola l'esp per andare al next level
        self.expAccumulated +=expReceived
        if expNextLvl== self.expAccumulated:
            self.level +=1
        else:
            print(f"Mancano {expNextLvl-self.expAccumulated} per raggiungere il prossimo livello")
    def RareCandy(self):
        self.level+=1
        self.expAccumulated=0
    
        
class Move:
    moveName=""
    def __init__(self, name, type, Dmg):
        self.moveName=name
        self.movetype=type
        self.moveDmg=Dmg
        
class Stats:
    hpBar=0
    def __init__(self, HP, Atk, Def):
        self.HP=HP
        self.hpBar=int(HP)
        self.Atk=Atk
        self.Def=Def
        self.SpAtk=int(Atk+((Atk*110)/100))
        self.SpDef=int(Def+((Def*110)/100))
        
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
            if self.movesList[i].moveName==" " or self.movesList[i].moveName=="":
                continue
            print(f"{i+1}. {self.movesList[i].moveName}")
    def CheckEvolution(self):
        for lvl in range(len(self.lvl.evolutionLvl)):
            if self.lvl.level==self.lvl.evolutionLvl[lvl]:
                print(f"Cosa!?{self.name} si sta evolvendo!")
                print("Oops, dimenticato di integrare le evoluzioni RIP")
    def Battle(self,move,counter):
        if int(move.moveDmg)/4 >=self.stats.hpBar:
            self.stats.hpBar=0
            counter+=1
            print(f"{self.name} è caduto")
        else:
            self.stats.hpBar=self.stats.hpBar - (move.moveDmg/4)
        return counter
starter=[Pokemon("Treeko","Erba",20,20,20,moves=[Move("Azione","normale",20),Move("Semitraglia","erba","35")],level=Level(10,[16,36])),Pokemon("Mudkip","Acqua",20,20,20,moves=[Move("Azione","normale",20),Move("Idropulsar","sacqua","35")],level=Level(10,[16,36])),
         Pokemon("Dialga","Drago Acciaio",220,29999,20,moves=[Move("Fendi tempo","acciao",40000),Move("Dragospiro","drago","35")],level=Level(100,0)),Pokemon("Palkia","Drago Acqua",220,29999,20,moves=[Move("Fendi spazio","acqua",40000),Move("Idropulsar","acqua","35")],level=Level(100,[0,0]))
         ]

urPkMn=[]
oppPkMn=[]
opzioni=["Lotta","Vedi i miei Pkmn","Aggiungi Pkmn","RimuoviPkmn","Esci"]

def Lotta():
    import random
    userKO=0
    oppKO=0 
    for i in range(len(urPkMn)):
        oppPkMn.append(starter[i])
    print("Inizia la lotta")
    for i in range(len(urPkMn)):
        print(f"{userName} manda in campo{urPkMn[i].name}")
        while urPkMn[i].stats.hpBar>0 and oppPkMn[i].stats.hpBar>0:
            if urPkMn[i].stats.hpBar!=0:
                print(f"{urPkMn[i].name} è ansioso di combattere, che mossa vuoi usare?")
                print(f"{urPkMn[i].printMoves()}")
                try:
                    sceltaU=int(input("Che mossa vuoi usare?->"))-1
                except:
                    print("Non hai inserito una lore valido!!!!")
                    continue
                if sceltaU<0 or sceltaU>len(urPkMn[i].movesList):
                    continue
            
            oppPkMn[i].Battle(urPkMn[i].movesList[sceltaU],oppKO)
            if oppPkMn[i].stats.hpBar!=0:
                oppMove= random.choice(oppPkMn[i].movesList)
                print(f"Il {oppPkMn[i].name} ha usato {oppMove.moveName} ")
                urPkMn[i].Battle(oppMove,userKO)
            
    if oppKO==len(urPkMn):
        print(f"Ha vinto {userName}")
    else:
        print("Ha vinto l'avversario")
def Visualizza(lista):
    for i in range(len(lista)):
        print(f"{i+1}. {lista[i].name} {lista[i].type}")
        print(f"{lista[i].stats.printStats()}")
        print(f"{lista[i].printMoves()}")
        
def RimuoviPkMn(lista):
    
    print("ATTENZIONE! Sei sicuro di voler liberare questo pokemon? L'esperienza accumulata verra persa insieme al pokemon y/n:")
    scelta=input()
    if scelta=="y" or scelta=="si" or scelta=="yes" or scelta=="sì":
        remove=input("Inserisci il nome del pokemon da rimuovere:")
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
        try:
            choice=int(input("->"))
        except:
            print("errore")
            continue
        if choice==1:
            Lotta()
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
    print("A che livello è il tuo pokemon")
    level=int(input("->"))
    print("A che livello si evolve?:")
    evolvl=int(input())
    lvl=Level(level,evolvl)
    return Pokemon(name,type,hp,attack,defense,moves,lvl)
userName=input("Qual'è il tuo nome giovane allenotoe/allenatrice?: ")
nPkmn=int(input(f"Quanti pokemon vuoi {userName}? Max 6:"))
# for i in range(nPkmn):
#     urPkMn.append(createPokemon())
urPkMn.append(Pokemon("Dialga","Drago Acciaio",220,29999,20,moves=[Move("Fendi tempo","acciao",40000),Move("Dragospiro","drago","35")],level=Level(100,[0,0])))
urPkMn.append(Pokemon("Palkia","Drago Acqua",220,29999,20,moves=[Move("Fendi spazio","acqua",40000),Move("Idropulsar","acqua","35")],level=Level(100,[0,0])))
Menu()
