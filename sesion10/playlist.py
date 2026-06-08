playlist = []
num_canciones = int(input("Cuantas canciones quieres añadir? "))

for i in range(num_canciones):
    cancion = str(input(f"Canción {i+1} "))
    playlist.append(cancion)


print("----- PLAYLIST -----")
print()
for j in range(num_canciones):
    print(f"{j+1}. {playlist[j]}")

print(f"""

Primera canción: {playlist[0]}
Última canción: {playlist[-1]}
Total de canciones: {len(playlist)}
""")

while True:
    print("""

MENU
1. Buscar por posición
2. Buscar por nombre
3. Salir
          """)
    opcion = int(input("Escoge una opción: "))
    match(opcion):
        case 1: 
            posicion = int(input("Escoge una posición: "))
            if posicion-1 in range(len(playlist)):
                print(f"La canción en la posición {posicion} es {playlist[posicion-1]}")
            else:
                print(f"La playlist tiene solo {len(playlist)} posiciones")
        case 2:
            cancion = input(f"Que canción quieres buscar? ")
            if cancion in playlist:
                print(f"La canción {cancion} existe en la playlist en la posicion {playlist.index(cancion)+1}")
            else:
                print("La canción no existe en la playlist")
        case 3:
            print("Adiós!")
            break
        case _:
            print("Escoge una opción válida")