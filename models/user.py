from app import db, ma


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

    def __repr__(self):
        return '<User %r>' % self.name

    def toDict(self):
        return {"id: %r" % self.id}


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        #exclude = ("name","id")
        ordered = True
