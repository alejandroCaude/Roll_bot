import random #importo la funcion de ramdon para sacar números randoms
import sys



#***********************************************
#   Para pasar los parametros por argumentos, se necesita hacerlo con la siguiente sintaxsis '/roll (tiradas)'
#***********************************************


#creo la funcion roll()
def roll(tiradas,caras):
    suma=0
    lista=[] 
    #Hago un bucle for para sacar los numeros randoms con el rango segun las tiradas que haya realizado
    for i in range(int(tiradas)):
        num_r=random.randint(1, int(caras)) #guardo en la variable num_r, el número random que haya sacado
        lista.append(num_r) #guardo el numero random en una lista
        suma += num_r #sumo los numeros random para sacar el total
   
    print(str(lista) + " = " + str(suma)) #Imprimo la lista (con todos los números randoms), y el resultado de la suma

def roll2(tiradas,caras):
#Si la variable tiradas, esta vacia...
    if not tiradas:
        tiradas=1 #Al estar vacia la variable, la igualo a un 1, ya que si esta vacia, corresponde a un 1
        #Si el numero de caras es menor de 4, o mayor de 20, le imprimo por pantalla que debe estar en el rango entre 4 y 20
        if int(caras)<4 or int(caras)>20:
            print("Las caras deben ser mayor de 4, y menor de 20")
        else:
            roll(tiradas,caras)  
    else:
        #Si el numero de caras es menor de 4, o mayor de 20, le imprimo por pantalla que debe estar en el rango entre 4 y 20
        if int(caras)<4 or int(caras)>20:
            print("Las caras deben ser mayor de 4, y menor de 20")
        else:
            roll(tiradas,caras)

#tira=input("/roll ") #Pido los datos
tira = sys.argv[2] #Paso por argumento los datos que deseo poner
separado2=tira.split('+')
separado3=len(separado2)

#Hago un bucle for, el rango segun las tiradas que haya realizado
for i in range(int(separado3)):
    separado3=[]
    separado3=separado2[i].split('d') #Con un .split, separado la cadena que acabo de meter
    tiradas=separado3[0] #Tiradas es el primer numero que se mete, que corresponde a las tiradas
    caras=int(separado3[1])#caras, es el segundo número que se pone, que corresponde a las caras que tiene el dado
    if not tiradas:
        tiradas=1
        roll2(tiradas,caras)
    else:       
        roll2(tiradas,caras)