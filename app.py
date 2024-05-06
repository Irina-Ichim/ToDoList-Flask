"""
Módulo para una aplicación de lista de tareas con Flask y SQLAlchemy.
Permite agregar, marcar como completadas y eliminar tareas.
"""

from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    """
    Modelo de datos para representar una tarea.

    Attributes:
        task_id (int): ID único de la tarea.
        name (str): Nombre de la tarea.
        done (bool): Indicador de si la tarea está completada o no.
    """
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    done = db.Column(db.Boolean)


@app.route('/')
def home():
    """
    Ruta para mostrar la página de inicio con la lista de tareas.
    """
    # Obtener la lista de tareas
    todo_list = Todo.query.all()
    
     # Obtener la hora actual y formatearla en HH:MM:SS
    hora_actual = datetime.now().strftime('%H:%M:%S')
    
    # Renderizar la plantilla HTML con la lista de tareas y la hora actual
    return render_template('base.html', todo_list=todo_list, hora_actual=hora_actual)


@app.route('/add', methods=['POST'])
def add():
    """
    Ruta para agregar una nueva tarea.

    Returns:
        redirect: Redirige a la página de inicio después de agregar la tarea.
    """
    name = request.form.get("name")
    new_task = Todo(name=name, done=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    """
    Ruta para marcar una tarea como completada.
    """
    todo = Todo.query.get(todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    """
    Ruta para eliminar una tarea.

    Args:
        todo_id (int): El ID de la tarea a eliminar.

    Returns:
        redirect: Redirige a la página de inicio después de eliminar la tarea.
    """
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run()
