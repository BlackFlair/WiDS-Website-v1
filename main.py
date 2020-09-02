from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/team')
def team():
    core = [['../static/images/team/ApporvaSingh.jpg', 'Apporva Singh', 'Anchor', 'BIO', 'LINKEDIN'],
            ['../static/images/team/Arya.jpg', 'Arya', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/Balachandra.png', 'Balachandra', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/DerrylKevinMonis.jpg', 'Derryl Kevin Monis', 'Anchor', 'Computer Science Student | NCC Cadet | Data Science Enthusiast', 'https://www.linkedin.com/in/derryl-kevin-monis-337a16110/'],
            ['../static/images/team/EshaGupta.jpg', 'Esha Gupta', 'Anchor', 'Computer Science | Coder | Intern at GirlScript Foundation', 'https://www.linkedin.com/in/esha-gupta-56b660191'],
            ['../static/images/team/HarshithaLingapalem.jpg', 'Harshitha Lingapalem', 'Head Volunteer', 'Computer Science Undergraduate, Meditation Coach- Enthusiast at Core Computers and Building Mobile Applications!', 'https://www.linkedin.com/in/harshitha-lingapalem-9b6981139/'],
            ['../static/images/team/LikhithaS.jpg', 'Likhitha S', 'Anchor', 'BIO', 'LINKEDIN'],
            ['../static/images/team/MuhammedShafi.jpg', 'Muhammed Shafi', 'Anchor & Designer', 'BIO', 'LINKEDIN'],
            ['../static/images/team/NikhilR.jpg', 'Nikhil R', 'Anchor', 'BIO', 'LINKEDIN'],
            ['../static/images/team/NishanthGowda.jpg', 'Nishanth Gowda', 'Social Media & Marketing', 'Computer Science Student | Data Science Enthusiast', 'http://linkedin.com/in/nishanth-gowda-102257194'],
            ['../static/images/team/Nithyashree.jpg', 'Nithyashree', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/PranavBedreGH.jpg', 'Pranav Bedre G H', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/Pruthvi.jpg', 'Pruthvi', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/Rituraj.jpg', 'Rituraj', 'ROLE', 'For me the world is binary, either its a 1 or a 0. To have loved and keep loving computers always, is my life. ', 'https://www.linkedin.com/in/ritu-raj-8992bb55/'],
            ['../static/images/team/SaarangGRajan.jpg', 'Saarang G Rajan', 'Social Media & Marketing', 'BIO', 'LINKEDIN'],
            ['../static/images/team/SamuelT.jpg', 'Samuel T', 'Anchor & Designer', 'Computer Science Student | Machine Learning Enthusiast', 'https://www.linkedin.com/in/samuel-t-87a494185/'],
            ['../static/images/team/Sashank.jpg', 'Sashank', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/ShivalokeshReddy.jpg', 'Shivalokesh Reddy', 'Designer', 'BIO', 'LINKEDIN'],
            ['../static/images/team/ShrishtiShreya.jpg', 'Shrishti Shreya', 'ROLE', 'Computer Science Student | Web Developer Enthusiast', 'https://www.linkedin.com/in/shrishti-shreya-02828a190/'],
            ['../static/images/team/SkandhaGuruDutt.jpg', 'Skandha Guru Dutt', 'Social Media & Marketing', 'Computer Science Student | ML and Data Science Enthusiast', 'https://www.linkedin.com/in/skandha-n-29901816b/'],
            ['../static/images/team/SrirajAsnotikar.jpg', 'Sriraj Asnotikar', 'Social Media & Marketing', 'BIO', 'LINKEDIN'],
            ['../static/images/team/SurinMachaiahMT.jpg', 'Surin Machaiah M T', 'Community Partnership & Developer', 'Full Stack Developer | Web Developement | App Development | Android | Flutter | Machine Learning | Robotic Process Automation (RPA)', 'https://www.linkedin.com/in/surin-machaiah-m-t-57b00416b'],
            ['../static/images/team/YPrahasith.jpg', 'Y Prahasith', 'ROLE', 'CSE Student  | Full Stack Web Developer', 'https://www.linkedin.com/in/y-prahasith-12b829173/']]

    volunteer = [['../static/images/test.jpg', 'Kum Somi', 'Marketing', 'Beta-Microsoft Learn Student Ambassador | ML enthusiast | Poet ', 'https://www.linkedin.com/in/kum-somi-25aa8a152'],
                 ['../static/images/test.jpg', 'Sujay Mudgal', 'Marketing ', 'I have my own startup and i have passion about business and marketing as these two play a very vital role in growing up of a Things', 'LINKEDIN'],
                 ['../static/images/test.jpg', 'Swathi G', ' ', ' ', 'https://www.linkedin.com/in/swathi-g-52a8181a0']]

    faculty = [['../static/images/test.jpg', 'NAME', 'ROLE', 'BIO', 'LINKEDIN']]

    return render_template("team.html", core=core, l_c=len(core), volunteer=volunteer, l_v=len(volunteer), faculty=faculty, l_f=len(faculty))


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
          ['12:50 PM', '01:10 PM', '---', 'Kavitha Dwivedi (ISM)', 'https://www.linkedin.com/in/kavitadwivedi/'],
          ['01:10 PM', '01:30 PM', '---', 'Dr.Lavanya Tekumalla', 'https://www.linkedin.com/in/lavanyats/'],
          ['01:30 PM', '01:50 PM', 'Prevent your Models from failing silently in Production', 'Sabari Lakshmi Krishnamoorthy (Saturam)', 'https://www.linkedin.com/in/sabari-lakshmi-k/'],
          ['01:50 PM', '02:10 PM', 'Actively Managing Risks with AI', 'Snigdha Ghosh (Paypal)', 'https://www.linkedin.com/in/snigdharay/'],
          ['02:10 PM', '02:30 PM', 'Inspirational Journey of Embibe (AI in education)', 'Aditi Avasthi', 'https://www.linkedin.com/in/aditiavasthi/']]

    d2 = [['10:30 AM', '10:50 AM', 'What can the shape of neighborhood show-and-tell?', 'Prof. Jaya Nair (IIT Bangalore)', 'https://www.linkedin.com/in/jayanair/'],
          ['10:50 AM', '11:10 AM', '---', 'Narmada Sambaturu (IISC)', 'https://www.linkedin.com/in/narmada-sambaturu-76155720/'],
          ['11:10 AM', '11:30 AM', 'Future and impact of AI, NLP', 'Dr.Anupama Ray (IBM Research)', 'https://www.linkedin.com/in/anupama-ray-55140826/'],
          ['11:30 AM', '11:50 AM', 'Big Buck Change in Banking', 'Vidhya Veeraraghavan', 'https://www.linkedin.com/in/vidhyaveeraraghavan/'],
          ['11:50 AM', '12:10 PM', 'Gender equality in tech', 'Deepti Rai (Senior Data Scientist - Policy Research, LinkedIn)', 'https://www.linkedin.com/in/dptrai/'],
          ['12:10 PM', '12:30 PM', 'Big omics data in Alzheimers disease', 'Dr. Aditi Verma', 'https: // www.linkedin.com / in / aditi - verma - b695aa3a / '],
          ['12:30 PM', '12:50 PM', 'AI driven Voice Solutions in Healthcare', 'Aishwarya Pathak (United Health)', 'https://www.linkedin.com/in/aishwarya-pathak-184382b5/?originalSubdomain=in'],
          ['12:50 PM', '01:10 PM', 'AI "Truth and Myth"', 'Siboli Mukherjee (MUST Research)', 'https://www.linkedin.com/in/siboli-m-4106757'],
          ['01:10 PM', '01:30 PM', 'From Text to Media - My Journey in AI since 2001', 'Amruta Purandare (Cinematrix)', 'https://www.linkedin.com/in/pamruta/'],
          ['01:30 PM', '01:50 PM', 'AWS Ecosystem for Big Data Analytics', 'Sridevi (Agilisium)', 'https://www.linkedin.com/in/sridevi-murugayen/'],
          ['01:50 PM', '02:10 PM', 'ML to supercharge a Conversational Commerce experience', 'Tina Mani (YFret)', 'https://www.linkedin.com/in/tinamani/']]

    return render_template("agenda.html", d1=d1, d2=d2)


@app.route('/datathon')
def datathon():
    return render_template("datathon.html")


if __name__ == '__main__':
    app.run(debug=True)