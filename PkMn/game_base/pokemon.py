from game_base.level import Level
from game_base.move import Move
from game_base.stats import Stats


class Pokemon:

    movesList = []

    def __init__(self, name, type, hp, attack, defense, moves, level):
        self.name = name
        self.type = type
        self.stats = Stats(HP=hp, Atk=attack, Def=defense)
        self.movesList = moves
        self.lvl = level

    def newMove(self, move):
        if (len(self.movesList) == 4):
            print("non puoi più aggiungere mosse")
            print("scegli la mossa che vuoi sostituire")
            for i in range(len(self.movesList)):
                print(f"{i + 1}. {self.movesList[i].moveName}")
            choice = input("what's your choice?->")
            self.movesList.pop(choice)
            self.movesList.append(move)
        else:
            self.movesList.append(move)

    def printMoves(self):
        for i in range(len(self.movesList)):
            if self.movesList[i].moveName == " " or self.movesList[i].moveName == "":
                continue
            print(f"{i + 1}. {self.movesList[i].moveName}")

    def CheckEvolution(self):
        for lvl in range(len(self.lvl.evolutionLvl)):
            if self.lvl.level == self.lvl.evolutionLvl[lvl]:
                print(f"Cosa!? {self.name} si sta evolvendo!")
                print("Oops, dimenticato di integrare le evoluzioni RIP")

    def Battle(self, move):
        if int(move.moveDmg) / 4 >= self.stats.hpBar:
            self.stats.hpBar = 0
            print(f"{self.name} è caduto")
            return True
        else:
            self.stats.hpBar = self.stats.hpBar - move.moveDmg / 4
            return False
        return counter