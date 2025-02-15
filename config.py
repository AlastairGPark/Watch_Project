import os

class Config:
    SECRET_KEY = 'ALASTAIR'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///watch.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False