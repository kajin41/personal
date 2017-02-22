from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import config

app = Flask(__name__)

mail = Mail(app)


@app.route('/')
def index():
    return render_template("home3.html", title="Gregory Mercado")

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html", title="Portfolio")

@app.route('/resume')
def resume():
    return render_template("resume.html", title="Resume")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", title="Contact")
    else:
        msg = Message(
            request.form['subject'],
            sender=(request.form['name'], config.MAIL_USERNAME),
            recipients=config.ADMINS,
            reply_to=request.form['email'])
        msg.html = request.form['message']
        with app.app_context():
            mail.send(msg)
        return redirect('/')


if __name__ == '__main__':
    app.run()
