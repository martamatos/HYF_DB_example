from flask import Markup
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required

from app import current_app, db
from app.main import bp
from app.main.forms import ModifyDataForm

from app.models import User, Task, Status


@bp.route('/see_user_list')
def see_user_list():
    tab_status = {"users": "active", "tasks": "#"}
    header = Markup("<th>ID</th> \
                    <th>Name</th> \
                    <th>Email</th> \
                    <th>Phone</th>")

    # enzyme_header = Enzyme.__table__.columns.keys()
    page = request.args.get('page', 1, type=int)
    users = User.query.order_by(User.id.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.see_user_list', page=users.next_num) \
        if users.has_next else None
    prev_url = url_for('main.see_user_list', page=users.prev_num) \
        if users.has_prev else None
    return render_template("see_data.html", title='See users', data=users.items,
                           data_type='user', tab_status=tab_status, header=header,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/see_user/<user_id>', methods=['GET', 'POST'])
def see_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    data = []
    data_nested = []

    data.append({'field_name': 'Name', 'data': user.name})
    data.append({'field_name': 'Email', 'data': user.email})
    data.append({'field_name': 'Phone', 'data': user.phone})

    form = ModifyDataForm()
    if form.validate_on_submit():
        return redirect(url_for('main.modify_user', user_id=user_id))

    return render_template("see_data_element.html", title='See enzyme', data_name=user.name, data_type='User',
                           data_list=data, data_list_nested=data_nested, form=form)


@bp.route('/see_task_list')
def see_task_list():
    tab_status = {"users": "#", "tasks": "active"}
    header = Markup("<th>ID</th> \
                    <th>Title</th> \
                    <th>Description</th> \
                    <th>Created</th> \
                    <th>Updated</th> \
                    <th>Due date</th> \
                    <th>Status</th> \
                    <th>User</th>")

    # enzyme_header = Enzyme.__table__.columns.keys()
    page = request.args.get('page', 1, type=int)
    tasks = Task.query.order_by(Task.id.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.see_task_list', page=tasks.next_num) \
        if tasks.has_next else None
    prev_url = url_for('main.see_task_list', page=tasks.prev_num) \
        if tasks.has_prev else None
    return render_template("see_data.html", title='See tasks', data=tasks.items,
                           data_type='task', tab_status=tab_status, header=header,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/see_task/<task_id>', methods=['GET', 'POST'])
def see_task(task_id):
    task = Task.query.filter_by(id=task_id).first()

    data = []
    data_nested = []

    data.append({'field_name': 'Title', 'data': task.title})
    data.append({'field_name': 'Description', 'data': task.description})
    data.append({'field_name': 'Created', 'data': task.created})
    data.append({'field_name': 'Updated', 'data': task.updated})
    data.append({'field_name': 'Due date', 'data': task.due_date})
    data.append({'field_name': 'Status', 'data': task.status.name})
    data.append({'field_name': 'User', 'data': task.user.name})

    form = ModifyDataForm()
    if form.validate_on_submit():
        return redirect(url_for('main.modify_task', task_id=task_id))

    return render_template("see_data_element.html", title='See task', data_name=task.title,
                           data_type='task', data_list=data, data_list_nested=data_nested, form=form)

