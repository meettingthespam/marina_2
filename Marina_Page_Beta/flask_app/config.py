import os

class Config:
    SECRET_KEY =  os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #os.environ.get('SQLALCHEMY_DATABASE_URI')
    # you can set key as config
    GOOGLEMAPS_KEY = os.environ.get('GOOGLEMAPS_KEY_SPAM')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME_pseudo')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD_pseudo')
