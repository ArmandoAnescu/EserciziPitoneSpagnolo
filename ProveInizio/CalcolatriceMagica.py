
totale=0
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def Operazione(num1,num2,simbolo):
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
    elif simbolo=="!" or simbolo=="fattoriale":
        totale=num1*factorial(num1-1)
    else:
        print("Math Error")
    print(totale)

while True:
    numero1=0
    numero2=0
    val=None
    print("per uscire scrivi stop")
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
    val=input()
    if val=="stop"or val=="STOP":
        break
    else:
        simboloNome=val
    Operazione(num1=numero1,num2=numero2,simbolo=simboloNome)
