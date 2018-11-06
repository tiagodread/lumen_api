class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost:5432/lumen'
    SQLALCHEMY_TRACK_MODIFICATIONS = True