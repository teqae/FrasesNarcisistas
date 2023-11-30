import random
from colorama import Fore, Style, init

init(autoreset=True)

def obtener_numero_aleatorio(limite_inferior, limite_superior):
    return random.randint(limite_inferior, limite_superior)

def obtener_limite_inferior_superior():
    while True:
        try:
            limite_inferior = int(input("Introduce el límite inferior del rango: "))
            limite_superior = int(input("Introduce el límite superior del rango: "))

            if limite_inferior >= limite_superior:
                print(Fore.RED + "El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo.")
            else:
                return limite_inferior, limite_superior
        except ValueError:
            print(Fore.RED + "Por favor, introduce números válidos para los límites.")

def adivina_el_numero():
    print(Fore.BLUE + "=" * 60)
    print(Style.BRIGHT + f"{'¡Bienvenido a Adivina el Número!':^60}")
    print(Fore.BLUE +"=" * 60)
    print(Style.RESET_ALL + "Estoy pensando en un número dentro de un rango que tú definirás.")

    limite_inferior, limite_superior = obtener_limite_inferior_superior()
    numero_a_adivinar = obtener_numero_aleatorio(limite_inferior, limite_superior)
    intentos = 0

    while True:
        try:
            intento = int(input(f"Adivina el número entre {limite_inferior} y {limite_superior}: "))
            intentos += 1

            if intento < numero_a_adivinar:
                print(Fore.YELLOW + "El número es mayor. ¡Intenta de nuevo!")
            elif intento > numero_a_adivinar:
                print(Fore.YELLOW + "El número es menor. ¡Intenta de nuevo!")
            else:
                print(Fore.GREEN + "=" * 60)
                print(Style.BRIGHT + f"¡Felicidades! Has adivinado el número {numero_a_adivinar} en {intentos} intentos.")
                print(Fore.GREEN +"=" * 60)
                break
        except ValueError:
            print(Fore.RED + "Por favor, introduce un número válido.")

    print(Style.RESET_ALL + "¡Gracias por jugar!")

# Iniciar el juego
adivina_el_numero()