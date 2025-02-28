class Stats:

    hpBar = 0
    def __init__(self, HP, Atk, Def,Speed):
        self.HP = HP
        self.hpBar = int(HP)
        self.Atk = Atk
        self.Def = Def
        self.SpAtk = int(Atk+((Atk*110)/100))
        self.SpDef = int(Def+((Def*110)/100))
        self.Speed = int(Speed)

    def printStats(self):
        print(f"HP: {self.HP}")
        print(f"Attacco: {self.Atk}")
        print(f"Difesa: {self.Def}")
        print(f"Attacco Speciale: {self.SpAtk}")
        print(f"Difesa Speciale: {self.SpDef}")
