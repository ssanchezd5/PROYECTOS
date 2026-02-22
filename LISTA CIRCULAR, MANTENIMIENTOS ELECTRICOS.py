# Sistema de Mantenimiento de Equipos Eléctricos
# Lista Enlazada Circular

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre):
        nuevo = Nodo(nombre)

        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = nuevo
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    def mostrar(self):
        if self.cabeza is None:
            print("No hay equipos registrados.")
            return

        temp = self.cabeza
        while True:
            print("Equipo:", temp.nombre)
            temp = temp.siguiente
            if temp == self.cabeza:
                break

    def siguiente_mantenimiento(self):
        if self.cabeza:
            print("Equipo en mantenimiento:", self.cabeza.nombre)
            self.cabeza = self.cabeza.siguiente

    def eliminar(self, nombre):
        if self.cabeza is None:
            return

        actual = self.cabeza
        anterior = None

        while True:
            if actual.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    temp = self.cabeza
                    while temp.siguiente != self.cabeza:
                        temp = temp.siguiente
                    self.cabeza = actual.siguiente
                    temp.siguiente = self.cabeza
                print("Equipo eliminado.")
                return

            anterior = actual
            actual = actual.siguiente

            if actual == self.cabeza:
                break

        print("Equipo no encontrado.")


# Programa principal
lista = ListaCircular()

while True:
    print("\n--- SISTEMA DE MANTENIMIENTO ---")
    print("1. Agregar equipo")
    print("2. Mostrar equipos")
    print("3. Siguiente mantenimiento")
    print("4. Eliminar equipo")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del equipo: ")
        lista.agregar(nombre)

    elif opcion == "2":
        lista.mostrar()

    elif opcion == "3":
        lista.siguiente_mantenimiento()

    elif opcion == "4":
        nombre = input("Nombre del equipo a eliminar: ")
        lista.eliminar(nombre)

    elif opcion == "5":
        break
        D