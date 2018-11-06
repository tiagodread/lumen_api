from flask import render_template
from flask import request, jsonify, redirect, url_for
from . import db, ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    cpf = db.Column(db.String(20), unique=True)
    phone = db.Column(db.String(20))

    def __init__(self, id=None, name=None, email=None, password=None, cpf=None, phone=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.phone = phone

    def index(self):
        users = User.query.all()
        return render_template('add_user.html', users=users)

    def add_users(self):
        name = request.form['name']
        email = request.form['email']
        cpf = request.form['cpf']
        phone = request.form['phone']
        password = request.form['password']
        user = User(None, name, email, password, cpf, phone)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    def list_users(self):
        if 'email' in request.args:
            users = User.query.filter(User.email == request.args.get('email'))
        else:
            users = User.query.all()
        users_schema = UserSchema(many=True)
        out = users_schema.dump(users).data
        return jsonify({'users': out})

    def __repr__(self):
        return '<User %r>' % self.name

    def toDict(self):
        return {"id: %r" % self.id}


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        # exclude = ("name","id")
        ordered = True
