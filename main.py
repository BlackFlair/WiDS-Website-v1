from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/speakers')
def speakers():
    return render_template("speakers.html")


@app.route('/agenda')
def agenda():
    return render_template("agenda.html")


@app.route('/datathon')
def datathon():
    return render_template("datathon.html")


if __name__ == '__main__':
    app.run(debug=True)