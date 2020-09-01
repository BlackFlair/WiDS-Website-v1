from flask import Flask, render_template

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
    d1 = [['10:30 AM', '10:50 AM', 'The myths in Data science and Machine Learning', 'Mathangi Sri (Gojek)', 'https://www.linkedin.com/in/mathangisri/'],
          ['10:50 AM', '11:10 AM', 'Developing actionable insights on top of model outputs', 'Smita SuryaNarayanan (Yodlee)', 'https://www.linkedin.com/in/smithas/'],
          ['11:10 AM', '11:30 AM', 'Deep Learning Advancements in NLP', 'Shruti Gupta (Google)', 'https://www.linkedin.com/in/shruti-gupta-88662367/'],
          ['11:30 AM', '11:50 AM', 'Data Science in Music', 'Sonika Malloth', 'https://www.linkedin.com/in/sonika-malloth-a3755018/'],
          ['11:50 AM', '12:10 PM', 'Datalake for Datascience in AWS', 'Vijaya Nirmala (IBM)', 'https://www.linkedin.com/in/vijayanirmalagopal-5a54159a/'],
          ['12:10 PM', '12:30 PM', 'Natural Language Processing & its Applications', ' Kanishka Priyadharshini (Cisco)', 'https://www.linkedin.com/in/kanishka-priyadharshini-a8023467/'],
          ['12:30 PM', '12:50 PM', 'AI in healthcare', 'Dr.Arathi Sreekumari I (GE Research)', 'https://www.linkedin.com/in/arathi-sreekumari-9184bb71/'],
          ['12:50 PM', '01:10 PM', 'XXXX', 'Kavitha Dwivedi (ISM)', 'https://www.linkedin.com/in/kavitadwivedi/'],
          ['01:10 PM', '01:30 PM', 'XXXX', 'Dr.Lavanya Tekumalla', 'https://www.linkedin.com/in/lavanyats/'],
          ['01:30 PM', '01:50 PM', 'Prevent your Models from failing silently in Production', 'Sabari Lakshmi Krishnamoorthy (Saturam)', 'https://www.linkedin.com/in/sabari-lakshmi-k/'],
          ['01:50 PM', '02:10 PM', 'Actively Managing Risks with AI', 'Snigdha Ghosh (Paypal)', 'https://www.linkedin.com/in/snigdharay/'],
          ['02:10 PM', '02:30 PM', 'Inspirational Journey of Embibe (AI in education)', 'Aditi Avasthi', 'https://www.linkedin.com/in/aditiavasthi/']]

    return render_template("agenda.html", d1=d1)


@app.route('/datathon')
def datathon():
    return render_template("datathon.html")


if __name__ == '__main__':
    app.run(debug=True)