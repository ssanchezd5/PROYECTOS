class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        # Operación: Creación
        self.cabeza = None

    def agregar(self, dato):
        # Operación: Inserción (al final)
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        # Operación: Recorrido
        actual = self.cabeza
        if not actual:
            print("La lista está vacía.")
            return
        while actual:
            print(f"[{actual.dato}]", end=" -> ")
            actual = actual.siguiente
        print("None")

    def buscar(self, valor):
        # Operación: Búsqueda
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == valor:
                return posicion  # Retorna la ubicación
            actual = actual.siguiente
            posicion += 1
        return -1  # No encontrado

    def eliminar(self, valor):
        # Operación: Eliminación
        actual = self.cabeza
        anterior = None

        while actual and actual.dato != valor:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print(f"El valor {valor} no se encuentra en la lista.")
            return

        if anterior is None:
            # Eliminar el primer nodo (cabeza)
            self.cabeza = actual.siguiente
        else:
            # Saltar el nodo actual para eliminarlo
            anterior.siguiente = actual.siguiente
        print(f"Nodo con valor {valor} eliminado.")


# --- Programa Interactivo ---
mi_lista = ListaEnlazada()

print("--- Gestión de Lista Enlazada ---")
while True:
    print("\n1. Agregar 2. Mostrar 3. Buscar 4. Eliminar 5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        dato = input("Escribe el dato a insertar: ")
        mi_lista.agregar(dato)
    elif opcion == "2":
        mi_lista.mostrar()
    elif opcion == "3":
        dato = input("Dato a buscar: ")
        pos = mi_lista.buscar(dato)
        if pos != -1:
            print(f"¡Encontrado! Está en la posición {pos}.")
        else:
            print("No se encontró el dato.")
    elif opcion == "4":
        dato = input("Dato a eliminar: ")
        mi_lista.eliminar(dato)
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")