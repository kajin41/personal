from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import config

app = Flask(__name__)

app.config['MAIL_SERVER'] = config.MAIL_SERVER
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD

mail = Mail(app)
nav_items = ['about', 'experience', 'skills', 'contact']


@app.route('/')
def index():
    return render_template("home3.html", title="Gregory Mercado", nav_items=nav_items)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", title="Contact")
    else:
        try:
            if int('0x' + request.form['name'], 16) > 0x5914b52de6c50:
                return 400
        except ValueError:
            pass

        msg = Message(
            request.form['subject'],
            sender=(request.form['name'], config.MAIL_USERNAME),
            recipients=config.ADMINS,
            reply_to=request.form['email'])
        msg.html = request.form['message'] + '\n' + request.headers['X-Forwarded-For']
        with app.app_context():
            mail.send(msg)
        return 'message sent'


if __name__ == '__main__':
    app.run()
