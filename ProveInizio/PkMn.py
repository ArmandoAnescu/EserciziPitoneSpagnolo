#to do:
#Aggiungi Atk.sp Def.Sp Spd
#Precisione
#Pokemon predefinit, pokemon già fatti e con moveset predefinito, sistema di scelta
#Level Up and Evolution System, un sistema degli exp che permette a un PkMn di evolversi al livello predefinito ex:charmeleon in charizard al 36
#
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
    def printStata(self):
        print(f"HP: {self.HP}")
        print(f"Attack: {self.Atk}")
        print(f"Defense: {self.Def}")
        print(f"Special Attack: {self.SpAtk}")
        print(f"Special Defense: {self.SpDef}")
class Pokemon:
    movesList=[]
    def __init__(self, name, type, hp, attack, defense,moves):
        self.name = name
        self.type = type
        self.stats=Stats(HP=hp,Atk=attack,Def=defense)
        self.movesList=moves
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
urPkMn=[]
oppPkMn=[]
opzioni=["Lotta","Vedi i miei Pkmn","Aggiungi Pkmn","RimuoviPkmn","Esci"]
def Menu():
    while True:
        print("cosa vuoi fare?")
        for i in range(len(opzioni)):
            print(f"{i+1}. {opzioni[i]}")
        choice=int(input("->"))
        if choice==1:
            print("Scusa funzione non disponibile")
        elif choice==2:
            for i in range(len(urPkMn)):
                print(f"{i+1}. {urPkMn[i].name} {urPkMn[i].type}")
        elif choice ==3:
            if len(urPkMn)<5:
                urPkMn.append(createPokemon())
            else:
                print("hai già 6 pokemon non puoi averne di più")
        elif choice==4:
            print("scusa funzione non disponibile")
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
            