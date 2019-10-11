import random

intentosRealizados = 0

miNombre = input(print("Hola como te llamas?"))
numero = random.randint(1,100)
print("hola "+miNombre+" estoy pensando en un numero entre 1 y 100")

while intentosRealizados <= 10:
    estimacion = input(print("Intenta adivinar: "))
    estimacion = int(estimacion)
    intentosRealizados +=1

    if estimacion < numero:
        print("Tu estimacion es muy baja")

    if estimacion > numero:
        print("Tu estimacion es muy alta")

    if estimacion == numero:
        break
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print("buen trabajo: "+miNombre+" has adivinado mi numero en: "+intentosRealizados+" intentos")
if estimacion != numero:
    numero = str(numero)
    print("has perdido, el numero era: "+numero)