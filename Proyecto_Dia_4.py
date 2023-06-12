"""1. Pedir al usuario el nombre
 2. El programa le dice que a pensado un numero entre el 0 y el 100,
  y que tien 8 intentos para adivinarlo
  3. El jugador dice un numero, el programa da cuatro opciones
  1- si es menor de uno o mayor de 100 no esta permitido range if n < 0 or n > 100
  2- si es menor el numero que a elegido el programa N < ?
  3- si es mayor al numero n > ?
  4- si acierta n == ?, se informa que a ganado y cuantos intentos le ha tomado
  * si el usuario no ha ganado en el primer intento se le va a volver a pedir que ingrese otro numero,
   asi hasta que gane o se agoten los ocho intentos
  """
from random import randint

# variables
intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")



# El programa le dice que a pensado un numero entre el 0 y el 100,y que tien 8 intentos para adivinarlo
print(f"Bueno {nombre}, he pensado un numero entre el 0 y el 100.Tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero?: "))
    intentos += 1

    if estimado not in range(1,101):
        print("tu numero no se encuentra en el rango que va de 1 a 100")
    elif estimado < numero_secreto:
        print("Mi número es mas alto")
    elif estimado > numero_secreto:
        print("Mi número es mas bajo")
    else:
        print(f"Felicitaciones {nombre}!! has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El número secreto era {numero_secreto}")

