import time
import os

#  Mostrar contextualizacion de la vacuna
def MostrarIntroduccion():
    print ("=============================================================",
        "\n===                        HISTORIA                       ===",
        "\n=============================================================",
        "\n  Un virus desconocido ha puesto en peligro a la humanidad,",
        "\n tú, como científico, debes fabricar una vacuna utilizando 6",
        "\n   ingredientes. Pero no es tan fácil... Debes elegir los ",
        "\n    ingredientes correctos para que la vacuna funcione.",
        "\n        ¡El destino del mundo está en tus manos!")
    input("\n--          Presiona enter para continuar          ---")

#  Mostrar reglas del juego
def MostrarReglas():
    print ("=============================================================",
        "\n===                         REGLAS                        ===",
        "\n=============================================================",
        "\n-- • Debes seleccionar 6 ingredientes",
        "\n-- •	No puedes repetir ingredientes",
        "\n-- •	Tienes 3 vidas",
        "\n-- •	Si eliges mal, la vacuna tenerdra efectos secundarios",
        "\n-- •	Si eliges correctamente, salvas a la humanidad")
    input("\n--          Presiona enter para continuar          ---")
    
#  Mostrar ingredientes para la vacuna
def MostrarIngredientes():
    print ("\n======================================================",
        "\n===             FABRICACION DE VACUNAS            ===",
        "\n======================================================",
        "\n-- Ingredientes disponibles:",
        "\n-- 1.",
        "\n-- 2.",
        "\n-- 3.",
        "\n-- 4.",
        "\n-- 5.",
        "\n-- 6.",
        "\n-- 7.",
        "\n-- 8." \
        "\n-- 9.",
        "\n-- 10. Caldo de pollito.",
        "\n-- Seleccione 6 ingredientes:")

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


# SeleccionarIngrediente() -> Permite elegir
def SeleccionarIngrediente():
    ingrediente_elegido = input(
        "Ingrese el nombre o número del ingrediente que desea seleccionar: "
    ).strip()
    return ingrediente_elegido

def ValidarOpcion(ingrediente):
    if ingrediente in ingredientes_disponibles:
        return True
    else:
        print('Mensaje: "Ingresa una opción válida"')
        return False


# IngredienteRepetido() -> Evita seleccionar el mismo ingrediente
def IngredienteRepetido(ingrediente, lista_seleccionados):
    if ingrediente in lista_seleccionados:
        print('Mensaje: "Ya seleccionaste este ingrediente"')
        return True
    else:
        return False


# AgregarIngrediente() -> Agrega el ingrediente elegido
def AgregarIngrediente(ingrediente, lista_seleccionados):
    lista_seleccionados.append(ingrediente)
    print(f"-> Ingrediente '{ingrediente}' agregado con éxito.")
    return lista_seleccionados



def ejecutar_paso_seleccion():
    ingrediente = SeleccionarIngrediente()

    # Evaluación según los rombos del diagrama
    if ValidarOpcion(ingrediente):
        if not IngredienteRepetido(ingrediente, lista_seleccionados):
            AgregarIngrediente(ingrediente, lista_seleccionados)
