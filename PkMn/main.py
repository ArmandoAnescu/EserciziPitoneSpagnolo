from game_base.pokemon import Pokemon

from game_base.battle import battle



        

starter=[Pokemon("Treeko","Erba",20,20,20,moves=[Move("Azione","normale",20),Move("Semitraglia","erba","35")],level=Level(10,[16,36])),Pokemon("Mudkip","Acqua",20,20,20,moves=[Move("Azione","normale",20),Move("Idropulsar","sacqua","35")],level=Level(10,[16,36])),
         Pokemon("Dialga","Drago Acciaio",220,29999,20,moves=[Move("Fendi tempo","acciao",40000),Move("Dragospiro","drago","35")],level=Level(100,0)),Pokemon("Palkia","Drago Acqua",220,29999,20,moves=[Move("Fendi spazio","acqua",40000),Move("Idropulsar","acqua","35")],level=Level(100,[0,0]))
         ]


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

#     urPkMn.append(createPokemon())
urPkMn.append(Pokemon("Dialga","Drago Acciaio",220,29999,20,moves=[Move("Fendi tempo","acciao",40000),Move("Dragospiro","drago","35")],level=Level(100,[0,0])))
urPkMn.append(Pokemon("Palkia","Drago Acqua",220,29999,20,moves=[Move("Fendi spazio","acqua",40000),Move("Idropulsar","acqua","35")],level=Level(100,[0,0])))
Menu()
