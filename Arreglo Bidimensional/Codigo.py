

def cargar(arreglo):

    contador = 1
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            arreglo[i][j] = contador
            contador += 1



def imprimir_regular(arreglo):

    print("\n--- Visualización Regular ---")
    for fila in arreglo:
        for elemento in fila:
            print(f"[{elemento:2d}]", end=" ")
        print()

def imprimir_escalonado(arreglo):

    print("\n--- Visualización Escalonada ---")
    for i, fila in enumerate(arreglo):
    
        print("    " * i, end="") 
        for elemento in fila:
            print(f"[{elemento:2d}]", end=" ")
        print()

def imprimir_piramide(arreglo):

    print("\n--- Visualización en Pirámide ---")
    total_filas = len(arreglo)
    for i, fila in enumerate(arreglo):
        # Calcula el espacio a la izquierda para centrar los elementos
        # Cada bloque '[XX] ' ocupa 5 caracteres en la terminal
        espacios = (total_filas - i - 1) * 2.5
        print(" " * int(espacios), end="")
        for elemento in fila:
            print(f"[{elemento:2d}]", end="")
        print()


# --- Bloque Principal ---

# 1. Definimos una estructura base en memoria (por ejemplo, una pirámide de 5 filas)
filas = 5
arreglo = [[0] * (i + 1) for i in range(filas)]

# 2. Cargamos los datos secuenciales una sola vez
cargar(arreglo)

# 3. Demostramos las tres formas diferentes de visualizar los MISMOS datos
imprimir_regular(arreglo)
imprimir_escalonado(arreglo)
imprimir_piramide(arreglo)
