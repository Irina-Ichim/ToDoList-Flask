"""
Módulo para definir la clase Tarea.

La clase Tarea representa una tarea con un nombre y un estado de completado o pendiente.
Permite crear tareas, marcarlas como completadas y obtener una representación en cadena de la tarea.

"""
from excepciones import TareaError

class Tarea:
    """Clase para representar una tarea."""

    def __init__(self, nombre):
        if not nombre:
            raise TareaError(TareaError.NOMBRE_INCOMPLETO)
        self.nombre = nombre
        self.completada = False

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __str__(self):
        """Devuelve la representación en cadena de la tarea."""
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea: {self.nombre} - Estado: {estado}"
