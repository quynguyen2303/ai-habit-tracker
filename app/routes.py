from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Habit, HabitEntry
from datetime import date

main = Blueprint('main', __name__)

@main.route('/')
def index():
    habits = Habit.query.all()
    return render_template('index.html', habits=habits)

@main.route('/habit/add', methods=['GET', 'POST'])
def add_habit():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        
        if name:
            habit = Habit(name=name, description=description)
            db.session.add(habit)
            db.session.commit()
            return redirect(url_for('main.index'))
            
    return render_template('add_habit.html')