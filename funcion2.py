from random import randint

# Función 1 de Julián Oliva
def julianOliva(intentos):

    print(f"Voy a generar un número al azar entre el 1 y 100 ¿Puedes adivinarlo en {intentos} intentos?")

    # Generar un número al azar
    numeroAzar = randint(1, 100)

    while intentos > 0:
        try:
            adivinar = int(input(f"¿Qué número? ({intentos} intentos restantes): "))
        except ValueError:
            print("[!] Ingrese un número entero.")
            continue

        if not (adivinar >= 1 and adivinar <= 100):
            print("[!] Tienes que ingresar un número entre el 1 y 100.")
            continue

        # Descontar un intento cuando el input es valido
        intentos -= 1

        # Condiciones para cuando lo adivina, no lo adivina o cuando se queda sin intentos
        if adivinar == numeroAzar:
            print(f"\n¡Lo adivinaste!\nEl número era: {numeroAzar}")
            return
        elif intentos == 0:
            print(f"\nQue lastima...\nEl número era: {numeroAzar}")
        elif adivinar > numeroAzar:
            print("Es menor.")
        else:
            print("Es mayor.")

julianOliva(10)