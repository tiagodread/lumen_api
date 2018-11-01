from flask import Flask, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/lumen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/')
def index():
    from models.user import User
    users = User.query.all()
    return render_template('add_user.html', users=users)


@app.route('/users/add', methods=['POST'])
def add_users():
    from models.user import User
    name = request.form['name']
    email = request.form['email']
    cpf = request.form['cpf']
    phone = request.form['phone']
    password = request.form['password']
    user = User(None, name, email, password, cpf, phone)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/users', methods=['GET'])
def list_users():
    from models.user import User
    from models.user import UserSchema
    if 'email' in request.args:
        users = User.query.filter(User.email == request.args.get('email'))
    else:
        users = User.query.all()
    users_schema = UserSchema(many=True)
    out = users_schema.dump(users).data
    return jsonify({'users': out})

if __name__ == '__main__':
    app.run()
