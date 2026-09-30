
# ============================================================
# CLASE CLIENTE
# Esta clase representa los datos de cada cliente.
# ============================================================

class Cliente:

    def __init__(self, nombre, cedula):
        # Guardamos el nombre del cliente
        self.nombre = nombre

        # Guardamos la cédula del cliente
        self.cedula = cedula

    def __str__(self):
        # Retorna la información del cliente
        return f"Cédula: {self.cedula} | Nombre: {self.nombre}"


# ============================================================
# CLASE NODO
# Un nodo almacena un cliente y una referencia al siguiente
# nodo de la lista.
# ============================================================

class Nodo:

    def __init__(self, cliente):
        # Cliente almacenado dentro del nodo
        self.cliente = cliente

        # Referencia al siguiente nodo
        # Inicialmente no apunta a ningún nodo
        self.siguiente = None


# ============================================================
# CLASE LISTA CLIENTES
# Esta clase administra la lista enlazada simple.
# ============================================================

class ListaClientes:

    def __init__(self):
        # Al comenzar la lista está vacía.
        # Primero representa el primer nodo.
        self.primero = None

    # ========================================================
    # MÉTODO INSERTAR ORDENADO
    # Inserta el cliente teniendo en cuenta el orden
    # de la cédula.
    # ========================================================

    def insertar_ordenado(self, cliente):

        # Creamos un nuevo nodo con el cliente
        nuevo = Nodo(cliente)

        # ----------------------------------------------------
        # CASO 1: la lista está vacía
        # ----------------------------------------------------

        if self.primero is None:
            self.primero = nuevo

            print("\nCliente insertado correctamente.")
            return

        # ----------------------------------------------------
        # CASO 2: el cliente debe quedar de primero
        # ----------------------------------------------------

        if cliente.cedula < self.primero.cliente.cedula:

            nuevo.siguiente = self.primero
            self.primero = nuevo

            print("\nCliente insertado correctamente.")
            return

        # ----------------------------------------------------
        # CASO 3: buscar la posición correcta
        # ----------------------------------------------------

        actual = self.primero

        while (
            actual.siguiente is not None
            and actual.siguiente.cliente.cedula < cliente.cedula
        ):
            actual = actual.siguiente

        # Insertamos el nuevo nodo
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

        print("\nCliente insertado correctamente.")

    # ========================================================
    # MÉTODO LISTAR
    # Recorre la lista desde el primer nodo hasta el último.
    # ========================================================

    def listar_clientes(self):

        # Verificamos si la lista está vacía
        if self.primero is None:
            print("\nLa lista de clientes está vacía.")
            return

        # Comenzamos desde el primer nodo
        actual = self.primero

        print("\n========== CLIENTES ==========")

        # Recorremos todos los nodos hacia la derecha
        while actual is not None:

            print(actual.cliente)

            # Pasamos al siguiente nodo
            actual = actual.siguiente

        print("==============================")

    # ========================================================
    # MÉTODO MOSTRAR ESTRUCTURA
    # Muestra visualmente cómo están conectados los nodos.
    # ========================================================

    def mostrar_estructura(self):

        if self.primero is None:
            print("\nLa lista está vacía.")
            return

        actual = self.primero

        print("\nEstructura de la lista:")

        while actual is not None:

            print(
                f"[{actual.cliente.cedula} - "
                f"{actual.cliente.nombre}]",
                end=""
            )

            if actual.siguiente is not None:
                print(" -> ", end="")
            else:
                print(" -> None")

            actual = actual.siguiente


# ============================================================
# FUNCIÓN MENÚ
# Muestra las opciones disponibles para el usuario.
# ============================================================

def mostrar_menu():

    print("\n")
    print("========================================")
    print("       SISTEMA DE CLIENTES")
    print("       LISTA ENLAZADA SIMPLE")
    print("========================================")
    print("1. Insertar cliente")
    print("2. Listar clientes hacia la derecha")
    print("3. Salir")
    print("========================================")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    # Creamos la lista de clientes
    lista = ListaClientes()

    # Variable que controla el menú
    opcion = 0

    # Repetimos el menú hasta seleccionar Salir
    while opcion != 3:

        # Mostrar las opciones
        mostrar_menu()

        # Solicitar la opción al usuario
        try:
            opcion = int(input("Seleccione una opción: "))

        except ValueError:
            print("\nDebe ingresar un número.")
            continue

        # ====================================================
        # OPCIÓN 1: INSERTAR CLIENTE
        # ====================================================

        if opcion == 1:

            print("\n========== INSERTAR CLIENTE ==========")

            nombre = input("Ingrese el nombre del cliente: ")

            # Solicitar cédula
            try:
                cedula = int(input("Ingrese la cédula del cliente: "))

            except ValueError:
                print("\nLa cédula debe ser un número.")
                continue

            # Crear el objeto Cliente
            cliente = Cliente(nombre, cedula)

            # Insertar el cliente de manera ordenada
            lista.insertar_ordenado(cliente)

        # ====================================================
        # OPCIÓN 2: LISTAR CLIENTES
        # ====================================================

        elif opcion == 2:

            lista.listar_clientes()

            # Mostrar visualmente los enlaces
            lista.mostrar_estructura()

        # ====================================================
        # OPCIÓN 3: SALIR
        # ====================================================

        elif opcion == 3:

            print("\nPrograma finalizado.")
            print("Gracias por utilizar el sistema.")

        # ====================================================
        # OPCIÓN NO VÁLIDA
        # ====================================================

        else:

            print("\nOpción no válida.")
            print("Seleccione 1, 2 o 3.")


# ============================================================
# EJECUTAR EL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()
