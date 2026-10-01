# Piedra, papel, tijera

jugador1 = input("Jugador 1: ")
jugador2 = input("Jugador 2: ")

if jugador1 == jugador2:
    print("EMPATE")
elif (jugador1.lower() == "piedra" and jugador2.lower() == "tijera") or\
      (jugador1.lower() == "papel" and jugador2.lower() == "pieda") or\
          (jugador1.lower() == "tijera" and jugador2.lower() == "papel"):
    print("JUGADOR 1")
else:
    print("JUGADOR 2")