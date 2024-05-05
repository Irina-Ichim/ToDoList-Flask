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
    
class TaskTime(db.Model):
    """
    Modelo de datos para representar el tiempo de una tarea.

    Attributes:
        task_time_id (int): ID único del registro de tiempo de tarea.
        task_id (int): ID de la tarea relacionada.
        start_time (DateTime): Fecha y hora de inicio de la tarea.
        pause_time (DateTime): Fecha y hora de pausa de la tarea (null si la tarea no está pausada).
        resume_time (DateTime): Fecha y hora de reanudación de la tarea (null si la tarea no está pausada).
        end_time (DateTime): Fecha y hora de finalización de la tarea.
        total_time (int): Tiempo total acumulado de la tarea (en segundos).
        status (str): Estado de la tarea (activo, pausado, completado, etc.).
    """
    task_time_id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('todo.task_id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    pause_time = db.Column(db.DateTime)
    resume_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    total_time = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"TaskTime(task_time_id={self.task_time_id}, task_id={self.task_id}, status={self.status})"



@app.route('/')
def home():
    """
    Ruta para mostrar la página de inicio con la lista de tareas.
    """
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)


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
