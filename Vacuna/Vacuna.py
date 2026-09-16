import time
import os

# ============================================================
# LISTAS Y VARIABLES
# ============================================================

ingredientes_disponibles = [
    "Agua Destilada",
    "Estabilizante",
    "Varsol",
    "Antígeno A",
    "Antígeno B",
    "Conservante",
    "Nieldertos",
    "Pomada",
    "Acetaminofen",
    "Caldo de pollito"
]

lista_seleccionados = []

vidas = 3

# Ingredientes correctos para fabricar la vacuna
ingredientes_correctos = [
    "Caldo de pollito",
    "Estabilizante",
    "Antígeno A",
    "Antígeno B",
    "Pomada",
    "Acetaminofen"
]


# ============================================================
# MOSTRAR INTRODUCCIÓN --- Funcion sin parametro y sin retorno
# ============================================================

def MostrarIntroduccion():
    os.system("cls")
    print(
        "=============================================================",
        "\n===                        HISTORIA                       ===",
        "\n=============================================================",
        "\n  Un virus desconocido ha puesto en peligro a la humanidad,",
        "\n tú, como científico, debes fabricar una vacuna utilizando 6",
        "\n   ingredientes. Pero no es tan fácil... Debes elegir los",
        "\n    ingredientes correctos para que la vacuna funcione.",
        "\n        ¡El destino del mundo está en tus manos!"
    )

    input("\n--          Presiona enter para continuar          ---")


# ============================================================
# MOSTRAR REGLAS --- Funcion sin parametro y sin retorno
# ============================================================

def MostrarReglas():
    os.system("cls")
    print(
        "=============================================================",
        "\n===                         REGLAS                        ===",
        "\n=============================================================",
        "\n-- • Debes seleccionar 6 ingredientes",
        "\n-- • No puedes repetir ingredientes",
        "\n-- • Tienes 3 vidas",
        "\n-- • Si eliges mal, la vacuna tendrá efectos secundarios",
        "\n-- • Si eliges correctamente, salvas a la humanidad"
    )

    input("\n--          Presiona enter para continuar          ---")


# ============================================================
# MOSTRAR INGREDIENTES --- Funcion sin parametro y sin retorno
# ============================================================

def MostrarIngredientes():
    os.system("cls")

    print(
        "\n======================================================",
        "\n===             FABRICACION DE VACUNAS            ===",
        "\n======================================================",
        "\n-- Ingredientes disponibles:"
    )

    for i, ingrediente in enumerate(ingredientes_disponibles, start=1):
        print(f"-- {i}. {ingrediente}")

    print("\n-- Vidas disponibles:", vidas)


# ============================================================
# SELECCIONAR INGREDIENTE --- Funcion sin parametro y con retorno
# ============================================================

def SeleccionarIngrediente():

    try:
        ingrediente_elegido = int(input(
            "\nIngrese el número del ingrediente que desea seleccionar: "
        ))

        return ingrediente_elegido

    except ValueError:
        print('\nMensaje: "Debes ingresar un número."')
        return None


# ============================================================
# VALIDAR OPCIÓN --- Funcion con parametro y con retorno
# ============================================================

def ValidarOpcion(ingrediente):

    if ingrediente is not None and 1 <= ingrediente <= len(ingredientes_disponibles):
        return True
    else:
        print('\nMensaje: "Ingresa una opción válida."')
        return False


# ============================================================
# INGREDIENTE REPETIDO --- Funcion con parametro y con retorno
# ============================================================

def IngredienteRepetido(ingrediente, lista_seleccionados):

    nombre_ingrediente = ingredientes_disponibles[ingrediente - 1]

    if nombre_ingrediente in lista_seleccionados:
        print('\nMensaje: "Ya seleccionaste este ingrediente."')
        return True
    else:
        return False


# ============================================================
# AGREGAR INGREDIENTE --- Funcion con parametro y con retorno
# ============================================================

def AgregarIngrediente(ingrediente, lista_seleccionados):

    nombre_ingrediente = ingredientes_disponibles[ingrediente - 1]

    lista_seleccionados.append(nombre_ingrediente)

    print(
        f"\n-> Ingrediente '{nombre_ingrediente}' agregado con éxito."
    )

    return lista_seleccionados


# ============================================================
# EJECUTAR PASO DE SELECCIÓN --- Funcion sin parametro y con retorno
# ============================================================

def ejecutar_paso_seleccion():

    ingrediente = SeleccionarIngrediente()

    if not ValidarOpcion(ingrediente):
        return False

    if IngredienteRepetido(ingrediente, lista_seleccionados):
        return False

    AgregarIngrediente(ingrediente, lista_seleccionados)

    return True


# ============================================================
# COMPROBAR VACUNA --- Funcion sin parametro y con retorno
# ============================================================

def ComprobarVacuna():

    if set(lista_seleccionados) == set(ingredientes_correctos):
        return True
    else:
        return False


# ============================================================
# MOSTRAR RESULTADO --- Funcion sin parametro y sin retorno
# ============================================================

def MostrarResultado():

    os.system("cls")

    print(
        "=============================================================",
        "\n===                    RESULTADO                          ===",
        "\n============================================================="
    )

    print("\nIngredientes seleccionados:")

    for ingrediente in lista_seleccionados:
        print(f"-> {ingrediente}")

    if ComprobarVacuna():

        print(
            "\n=============================================================",
            "\n             ¡VACUNA FABRICADA CORRECTAMENTE!",
            "\n=============================================================",
            "\n¡Has salvado a la humanidad!"
        )
        input()
        exit()

    else:

        print(
            "\n=============================================================",
            "\n                  VACUNA INCORRECTA",
            "\n=============================================================",
            "\nLa combinación de ingredientes no es correcta."
            "\nVuelve a intentar\n\nESPERA UN MOMENTO"
        )
        global vidas
        vidas -= 1
        time.sleep(5)


# ============================================================
# PROGRAMA PRINCIPAL 
# ============================================================

MostrarIntroduccion()
MostrarReglas()
MostrarIngredientes()

while (vidas != 0):
    lista_seleccionados.clear()
    for i in range(6):

        bandera = False

        while bandera == False:

            print(f"\nIngrediente {i + 1} de 6")
            print(f"Vidas restantes: {vidas}")

            bandera = ejecutar_paso_seleccion()

            # Si hubo un error, se pierde una vida
            if bandera == False:

                vidas -= 1

                print(f"\n¡Has perdido una vida!")
                print(f"Vidas restantes: {vidas}")

                if vidas == 0:

                    print(
                        "\n=============================================================",
                        "\n                  GAME OVER",
                        "\n=============================================================",
                        "\nTe has quedado sin vidas."
                    )

                    exit()

    MostrarResultado()
