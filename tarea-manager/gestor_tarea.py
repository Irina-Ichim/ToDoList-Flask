"""
Módulo para la gestión de tareas pendientes.
La clase permite agregar nuevas tareas, marcar tareas como completadas,
mostrar todas las tareas pendientes y eliminar tareas de la lista.

"""

from tarea import Tarea
from excepciones import TareaError

class GestorTareas:
    """
    Clase para gestionar una lista de tareas pendientes.
    """

    def __init__(self):
        """
        Inicializa el gestor de tareas con una lista vacía de tareas.
        """
        self.tareas = []

    def agregar_tarea(self, nombre):
        """
        Agrega una nueva tarea a la lista de tareas.
        Raises:
            TareaError: Si ocurre un error al agregar la tarea.
        """
        try:
            tarea = Tarea(nombre)
            self.tareas.append(tarea)
        except TareaError as e:
            raise TareaError(e) from e

    def mostrar_tareas(self):
        """
        Muestra todas las tareas pendientes.

        Raises:
            TareaError: Si ocurre un error al mostrar las tareas.
        """
        try:
            if not self.tareas:
                print("No hay tareas pendientes.")
                return
            print("Tareas Pendientes:")
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea}")
        except Exception as exc:
            raise TareaError(TareaError.ERROR_GENERICO) from exc

    def marcar_completada(self, posicion):
        """
        Marca una tarea como completada dado su posición en la lista.

        Raises:
            TareaError: Si la posición especificada no es válida o si ocurre un error 
            al marcar la tarea como completada.
        """
        try:
            tarea = self.tareas[posicion - 1]
            tarea.marcar_completada()
            print(f"La tarea '{tarea.nombre}' ha sido marcada como completada.")
        except IndexError as exc:
            raise TareaError(TareaError.ERROR_MARCAR_COMPLETADA) from exc
        except Exception as exc:
            raise TareaError(TareaError.ERROR_GENERICO) from exc

    def eliminar_tarea(self, posicion):
        """
        Elimina una tarea de la lista dado su posición.
        Si la posición especificada no es válida o si ocurre un error al eliminar la tarea.
        """
        try:
            tarea_eliminada = self.tareas.pop(posicion - 1)
            print(f"La tarea '{tarea_eliminada.nombre}' ha sido eliminada.")
        except IndexError as exc:
            raise TareaError(TareaError.ERROR_ELIMINAR_TAREA) from exc
        except Exception as exc:
            raise TareaError(TareaError.ERROR_GENERICO) from exc
