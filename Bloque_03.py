### EJEMPLOS CONDICIONALES


## 1. Usando uno de los operadores de comparación en Python, escribe un programa simple de dos 
# líneas que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor 
# que 100, y True si n es mayor o igual que 100.

## No debes crear ningún bloque if (hablaremos de ellos muy pronto). 
# Prueba tu código usando los datos que te proporcionamos.

n=int(input("Numero a comparar: "))

print(n < 100,n >= 100 )

## 2. ¿Como identidicamos el mayor de los dos numeros?
 
 #lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

#elegir el número más grande
if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

#imprimir el resultado
print("El número más grande es:", nmasGrande)

## 3. El codigo anterior al presentar una sola instruccion para las condiciones se pueden poner 
# sin sangria. Pero puede ser engañoso, por lo tanto es aconsejable no usarlo. 

#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

# elegir el número más grande
if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

#imprimir el resultado
print("El número más grande es: ", nmasGrande)



## 4.encontremos el mayor de los tres números. ¿Se ampliará el código? Un poco.
# Suponemos que el primer valor es el más grande. Luego verificamos esta hipótesis
# con los dos valores restantes.

#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)

##5. Pseudocodio: 

numeroMayor = -999999999
numero = int(input())
if numero == -1:
    exit()

if numero > numeroMayor:
    numeroMayor = numero
    
print(numero)

## 6. Funciones Integradas: 

# lee tres números
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

numeroMayor = max(numero1,numero2,numero3)

# imprimir el resultado
print("El número más grande es:", numeroMayor) 


## 7. LABORATORIO: Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o 
# flor de la paz, es una de las plantas para interiores más populares que filtra 
# las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno,
# formaldehído y amoníaco.
# Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada
# en forma de la palabra Espatifilo, grita involuntariamente a la consola la siguiente cadena:  
# "¡Espatifilo es la mejor planta de todas!" 
# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena 
# como entrada y que:

#Imprima el enunciado "Si, ¡El Espatifilo es la mejor planta de todos los tiempos!"  en 
# la pantalla si la cadena ingresada es "Espatifilo".
#Imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo".
#Imprima  "¡Espatifilo! ¡No [entrada]!"  de lo contrario. Nota: [entrada] es la cadena que
# se toma como entrada.

palabra = str(input("¿Que planta vas a regalar?: "))

planta1 = "Espatifilo"
planta2 =  "espatifilo"


if (palabra == planta1):
    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
else:
    if (palabra == planta2): 
        print("No, ¡quiero un gran Espatifilo!")
    else:
        print("¡Espatifilo! ¡No", palabra,"!" )
        

## LABORATORIO 2: 