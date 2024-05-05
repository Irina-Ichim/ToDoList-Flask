"""
Módulo para la gestión de tareas pendientes.
El programa permite al usuario agregar nuevas tareas, marcar tareas como completadas,
mostrar todas las tareas pendientes y eliminar tareas de la lista.
"""

from gestor_tarea import GestorTareas
from excepciones import TareaError

def mostrar_menu():
    """Muestra el menú de opciones disponibles."""
    print("======= Menú =======")
    print("1. Agregar nueva tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    """Función principal del programa."""
    gestor = GestorTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_tarea = input("Ingrese el nombre de la nueva tarea: ")
            try:
                gestor.agregar_tarea(nombre_tarea)
                print("Tarea agregada exitosamente.")
            except TareaError as e:
                print(f"Error: {e}")
        
        elif opcion == "2":
            if not gestor.tareas:
                print("No hay tareas pendientes.")
            else:
                try:
                    posicion = int(input("Ingrese la posición de la tarea a marcar como completada: "))
                    gestor.marcar_completada(posicion)
                except ValueError:
                    print("Por favor ingrese un número válido.")
                except TareaError as e:
                    print(f"Error: {e}")
        
        elif opcion == "3":
            gestor.mostrar_tareas()
        
        elif opcion == "4":
            if not gestor.tareas:
                print("No hay tareas pendientes.")
            else:
                try:
                    posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
                    gestor.eliminar_tarea(posicion)
                except ValueError:
                    print("Por favor ingrese un número válido.")
                except TareaError as e:
                    print(f"Error: {e}")
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()
