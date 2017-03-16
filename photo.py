from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import config

photo_app = Flask(__name__)

photo_app.config['MAIL_SERVER'] = config.MAIL_SERVER
photo_app.config['MAIL_PORT'] = 465
photo_app.config['MAIL_USE_TLS'] = False
photo_app.config['MAIL_USE_SSL'] = True
photo_app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
photo_app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD

mail = Mail(photo_app)


@photo_app.route('/')
def index():
    return render_template("photo.html", title="Gregory Mercado - Photography")

if __name__ == '__main__':
    photo_app.run()