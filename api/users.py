# from app import app
# from flask import request, redirect, url_for, render_template
#
#
# @app.route('/')
# def index():
#     return render_template('add_user.html')
#
# @app.route('/users/add', methods=['POST'])
# def add_users():
#     from models.user import User
#     name = request.form['name']
#     email = request.form['email']
#     cpf = request.form['cpf']
#     phone = request.form['phone']
#     password = request.form['password']
#     user = User(None, name, email, password, cpf, phone)
#     app.db.session.add(user)
#     app.db.session.commit()
#     return redirect(url_for('index'))
