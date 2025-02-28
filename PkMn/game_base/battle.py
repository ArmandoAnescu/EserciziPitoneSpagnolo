def battle(playerPkmn,oppPkmn,userName):
    import random
    userKO=0
    oppKO=0
    userUsedPkMn=0
    oppUsedPkMn=0
    oppPkmn.clear()
    for i in range(len(playerPkmn)):
        oppPkmn.append()
    print("Inizia la lotta")
    while userUsedPkMn !=6 and oppUsedPkMn!=6:
        print(f"{userName} manda in campo{playerPkmn[userUsedPkMn].name}")
        while True:
            if playerPkmn[userUsedPkMn].stats.hpBar != 0:
                print(f"{playerPkmn[userUsedPkMn].name} è ansioso di combattere, che mossa vuoi usare?")
                print(f"{playerPkmn[userUsedPkMn].printMoves()}")
                try:
                    sceltaU = int(input("Che mossa vuoi usare?->")) - 1
                except:
                    print("Non hai inserito una lore valido!!!!")
                    continue
                if sceltaU < 0 or sceltaU > len(playerPkmn[i].movesList):
                    continue

            if oppPkmn[userUsedPkMn].Battle(playerPkmn[userUsedPkMn].movesList[sceltaU]):
                oppKO += 1
                oppUsedPkMn +=1
            if oppPkmn[oppUsedPkMn].stats.hpBar != 0:
                oppMove = random.choice(oppPkmn[oppUsedPkMn].movesList)
                print(f"Il {oppPkmn[oppUsedPkMn].name} ha usato {oppMove.moveName} ")
                if playerPkmn[userUsedPkMn].Battle(oppMove):
                    userKO += 1
                    userUsedPkMn+=1
            if playerPkmn[i].stats.hpBar > 0 and oppPkmn[i].stats.hpBar > 0:
                break;
    if oppKO == len(playerPkmn):
        print(f"Ha vinto {userName}")
    else:
        print("Ha vinto l'avversario")
