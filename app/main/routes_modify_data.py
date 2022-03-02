import json
import re

from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import login_required

from app import current_app, db
from app.main import bp
from app.main.forms import UserForm, TaskForm
from app.models import User, Task, Status
from datetime import datetime


@bp.route('/modify_user/<user_id>', methods=['GET', 'POST'])
def modify_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    data_form = dict(name=user.name,
                     email=user.email,
                     phone=user.phone)

    form = UserForm(data=data_form)

    if form.validate_on_submit():

        user.name = form.name.data
        user.email = form.email.data
        user.phone = form.phone.data

        db.session.add(user)
        db.session.commit()

        flash('Your user has been modified.')
        return redirect(url_for('main.see_user', user_id=user_id))

    return render_template('insert_data.html', title='Modify user', form=form, header='Modify user')


@bp.route('/modify_task/<task_id>', methods=['GET', 'POST'])
def modify_task(task_id):
    task = Task.query.filter_by(id=task_id).first()

    data_form = dict(title=task.title,
                     description=task.description,
                     due_date=task.due_date,
                     status=task.status,
                     user=task.user)

    form = TaskForm(data=data_form)

    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.updated = datetime.now()
        task.due_date = form.due_date.data
        task.status = form.status.data
        task.user = form.user.data

        db.session.add(task)
        db.session.commit()

        flash('Your task has been modified.')
        return redirect(url_for('main.see_task', task_id=task_id))

    return render_template('insert_data.html', title='Modify task', form=form, header='Modify task')
