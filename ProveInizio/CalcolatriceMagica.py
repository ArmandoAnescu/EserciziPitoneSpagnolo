
totale=0
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def Operazione(num1,num2,simbolo):#metodo per eseguire i calcoli
    if simbolo=="*" or simbolo=="moltiplicazione":
        totale=num1*num2
    elif simbolo=="/" or simbolo=="divsione":
        totale=num1/num2
    elif simbolo=="-" or simbolo=="differenza":
        totale=num1-num2
    elif simbolo=="+" or simbolo=="addizione":
        totale=num1+num2
    elif simbolo=="^" or simbolo=="potenza":
        totale=num1**num2
    elif simbolo=="!" or simbolo=="fattoriale":##controllo che il simbolo o la parola inserita corrispondano all'operazione giusta
        totale=num1*factorial(num1-1)#per fare il fattoriale uso il metodo factorial, moltiplico il mio numero per i numeri prima di lui moltiplicati tra loro
    else:#es 9, fara prima 8*7*6*5*4*3*2*1 e poi ritorna il risultato e lo moltiplica appunto per 9
        print("Math Error")#se il simbolo inserito o non è tra quelli presenti o la parola è scritta male non coincide non esegue l'op e ritorna Math error
    print(totale)

while True:#faccio un while true
    numero1=0
    numero2=0
    val=None
    print("per uscire scrivi stop")#scrivo all'utente di inserire al parola stop o STOP
    print("Inserisci il primo numero")
    val=input()
    if val=="stop" or val=="STOP":
        break
    else:
        numero1=float(val)
    print("Inserisci il seondo numero")
    val=input()
    if val=="stop"or val=="STOP":
        break
    else:
        numero2=float(val)
    print("Inserisci il simbolo o il nome dell'operazione")
    val=input()#uso val per leggere l'input e controllare che non sia la parola stop e se != da stop allora assegna il valore e va avanti
    if val=="stop"or val=="STOP":
        break
    else:
        simboloNome=val
    Operazione(num1=numero1,num2=numero2,simbolo=simboloNome)#passo quello che ho letto al metodo
