import random

""" GAME ROOM CON PYTHON """

    
def main():
    """ Funcion que genera i lee i ejecuta las opciones del juego """

    while True:
        print("******************************************************")
        print("********************Menu de juegos********************")
        print("******************************************************")
        print("1. Adivinar numero")
        print("2. Piedra - Papel - Tijeras")
        print("3. El ahorcado")
        print("4. Salir")

        try:
            option = int(input("Indica una de las 4 opciones mostradas arriba: "))

            if option == 1:
                guess_number()
            elif option == 2:
                rock_paper_scissors()
            elif option == 3:
                hanged()
            elif option == 4:
                print("Saliendo de GAMEROOM... :(")
                break
            else:
                print("La opcion introducida no es valida, introduzca el numero de unade las 4 opciones!")
        except:
            print("La opcion introducida no es valida, introduzca el numero de una de las 4 opciones!")


def guess_number():
    """" Funcion que genera i controla el juego de adivinar el numero  """
    
    print("*******************************************************")
    print("******************Juego de adivinanza******************")
    print("*******************************************************")
    print("Tienes 3 intento spara adivinar un numero del 1 al 10")

    # Creamos el numero aleatorio con random i iniciamos el numero de intentos en 3
    nwin = random.randint(1,10)
    nwin = 7
    trys = 3

    while trys != 0:
        userGuess = input("Introduce un numero del 1 al 10: ")

        try:
            userGuess = int(userGuess)
        except:
            print("ERROR: el valor introducido no es un numero")
            

        if userGuess > 10 or userGuess < 1:
            print(f"El numero introduciodo no esta permitido, valores permitidos: 1,2,3,4,5,6,7,8,9,10. Valor introduciodo por el usuario: {userGuess}")   
            continue
        
        trys -= 1

        if userGuess < nwin:
            print(f"Numero de inetnos restantes: {trys}")
            print("El numero que has introducido es mas pequeño")
        elif userGuess > nwin:
            print(f"Numero de inetnos restantes: {trys}")
            print("El numero que has introducido es mas grande")
        else:
            print(f"Has ganado el juego, el numero era {nwin} :)")
            print("El juego de adivinanza se cerrara i volveras al menu")
            trys = 0
        
        if trys == 0:
            print(f"El numero de intentos restantes es {trys}")
            print("El juego de adivinanza se cerrara i volveras al menu")

    
def rock_paper_scissors():
    """ Funcion que genera y controla el juego de piedra papel y tijeras """

    print("*******************************************************")
    print("***************Juego piedra papel tijera***************")
    print("*******************************************************")
    print("Piedra papel tijera contra la maquina gana el mejor de 3")

    machinePoints = 0
    playerPoints = 0
    options = ["piedra", "papel", "tijeras"]

    while machinePoints < 3 and playerPoints < 3:

        playerSelec = input("Intodueix 'piedra', 'papel' o 'tijeras': ").lower()

        if playerSelec not in options:
            print("ERROR: Opcion erronia, vulve a intentar-lo :)")
            continue

        machineSelec = random.choice(options)
        print(f"La maquina ha escojido {machineSelec}")

        if machineSelec == playerSelec:
            print("Empate!!!")
            continue
        elif playerSelec == "papel" and machineSelec == "piedra":
            print("Has ganado este turno !")
            playerPoints += 1
        elif playerSelec == "piedra" and machineSelec == "tijeras":
            print("Has ganado este turno !")
            playerPoints += 1
        elif playerSelec == "tijeras" and machineSelec == "papel":
            print("Has ganado este turno !")
            playerPoints += 1
        else:
            print("La maquina ha ganado este turno!")
            machinePoints += 1

        print(f"Puntos: Player = {playerPoints} Machine = {machinePoints}")

    if playerPoints == 3:
        print("Has ganado el juego de piedra papel tijera, FELICIDADAES!!! :)")
    else:
        print("Ha ganado la Maquina... :(")


def hanged():
    """ Funcion que ejecuta i controla el juego del ahorcado """

    print("*******************************************************")
    print("******************Juego del ahorcado*******************")
    print("*******************************************************")
    print("Juego del ahorcado, el de toda la vida")

    with open('palabras.txt', 'r') as file:
        words = [line.strip() for line in file.readlines() if 3 <= len(line.strip()) <= 7]
    
    word = random.choice(words)
    trys = len(word) * 2
    board = ['_'] * len(word)
    
    print("Adivina la paraula: " + " ".join(board))
    
    while trys > 0:
        letter = input("Introduce una letra: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Introduce solo una letra.")
            continue
        
        if letter in word:
            for i, c in enumerate(word):
                if c == letter:
                    board[i] = letter
            print("Bien! La palabra ahora es: " + " ".join(board))
            if '_' not in board:
                print("Felicidades! Has acertado la palabra!")
                return
        else:
            trys -= 1
            print(f"La letra no es correcta. Te quedan {trys} intentos.")
        
        print("Adivina la palabra: " + " ".join(board))
    
    print(f"Has perdido! La palabra era '{word}'.")


if __name__ == "__main__":
    main()