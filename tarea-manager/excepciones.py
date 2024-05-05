"""Módulo para definir excepciones personalizadas relacionadas con las tareas."""

class TareaError(Exception):
    """Clase de excepción personalizada para errores relacionados con las tareas."""
    NOMBRE_INCOMPLETO = "El nombre de la tarea no puede estar vacío."
    POSICION_INVALIDA = "La posición especificada no es válida."
    ERROR_GENERICO = "Se produjo un error al procesar la tarea."
    ERROR_AGREGAR_TAREA = "Error al agregar la tarea."
    ERROR_MOSTRAR_TAREAS = "Error al mostrar las tareas."
    ERROR_MARCAR_COMPLETADA = "Error al marcar la tarea como completada."
    ERROR_ELIMINAR_TAREA = "Error al eliminar la tarea."
