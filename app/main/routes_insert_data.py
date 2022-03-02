from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from app import db
from app.main import bp
from app.main.forms import UserForm, TaskForm
from app.models import Status, Task, User
from app.utils.parsers import parse_input_list


@bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()

    if form.validate_on_submit():

        user = User(name=form.name.data,
                    email=form.email.data,
                    phone=form.phone.data)

        db.session.add(user)
        db.session.commit()

        flash('Your user is now live!')
        return redirect(url_for('main.see_user_list'))

    return render_template('insert_data.html', title='Add user', form=form, header='Add user')


@bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()

    if form.validate_on_submit():
        task = Task(title=form.title.data,
                    description=form.description.data,
                    due_date=form.due_date.data,
                    status=form.status.data,
                    user=form.user.data)

        db.session.add(task)
        db.session.commit()

        flash('Your task  is now live!', 'success')
        return redirect(url_for('main.see_task_list'))

    return render_template('insert_data.html', title='Add task', form=form, header='Add task')
