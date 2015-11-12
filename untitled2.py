from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html", title="Gregory Mercado")

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html", title="Portfolio")

@app.route('/resume')
def resume():
    return render_template("resume.html", title="Resume")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact")


if __name__ == '__main__':
    app.run()
