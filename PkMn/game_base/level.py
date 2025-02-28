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