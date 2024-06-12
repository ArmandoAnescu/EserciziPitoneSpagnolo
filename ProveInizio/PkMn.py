class Move:
    moveName=""
    def __init__(self, name, type, Dmg):
        self.moveName=name
        self.movetype=type
        self.moveDmg=Dmg
class Pokemon:
    movesList=[]
    def __init__(self, name, type, hp, attack, defense,moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
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
for i in range(6):
    urPkMn.append(createPokemon())