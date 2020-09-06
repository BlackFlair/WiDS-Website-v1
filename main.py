from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    about = "The Women in Data Science (WiDS) initiative aims to inspire and educate data scientists worldwide, regardless of gender, and to support women in the field. WiDS is a global movement that includes a number of initiatives  like global conferences , regional events , podcasts , datathon and webinars. WiDS Mysuru is organized in collaboration with four universities  - NIE , VVCE , GSSS and JSS"

    a_img = "../static/images/team/UshaRengaraju.jpg"
    a_name = "Usha Rengaraju"
    a_role = "WiDS Mysuru Amabassador"
    a_desc = "Usha is a polymath and India's first women Kaggle Grandmaster. She leads several communities like Women in Machine Learning and Data Science(WiMLDS – Bangalore and Mysore Chapter), TensorFlow User Group (TFUG Mysore ) and Women in Data Science Ambassador(WiDS Mysore). She organized NeuroAI (www.neuroai.in) which is India’s first-ever research symposium in the interface of Neuroscience and Data Science. She spoke at various conferences like ODSC, Pycon India, Indo Data Week, and GHCI. She specializes in Probabilistic Graphical Models, Machine Learning and Deep Learning. She has prepared curriculum for BITS Pilani’s masters in Data Science program (consumed by 20,000+ students ) and Upgrad’s PGP program in DS(consumed by 10,000+ students)"
    a_twitter = "https://twitter.com/URengaraju"
    a_linkedin = "https://www.linkedin.com/in/usha-rengaraju-b570b7a2/"

    university = ["../static/images/university/VVCE.jpg",
                  "../static/images/university/NIE.png",
                  "../static/images/university/GSSS.png",
                  "../static/images/university/JSS.png"]

    ambassador = [a_img, a_name, a_role, a_desc, a_linkedin, a_twitter]

    return render_template("index.html", about=about, ambassador=ambassador, university=university)


@app.route('/team')
def team():
    core = [['../static/images/team/core/ApporvaSingh.jpg', 'Apporva Singh', 'Anchor', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/Arya.jpg', 'Arya', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/DerrylKevinMonis.jpg', 'Derryl Kevin Monis', 'Anchor', 'Computer Science Student | NCC Cadet | Data Science Enthusiast', 'https://www.linkedin.com/in/derryl-kevin-monis-337a16110/'],
            ['../static/images/team/core/EshaGupta.jpg', 'Esha Gupta', 'Anchor', 'Computer Science | Coder | Intern at GirlScript Foundation', 'https://www.linkedin.com/in/esha-gupta-56b660191'],
            ['../static/images/team/core/HarshithaLingapalem.jpg', 'Harshitha Lingapalem', 'Head Volunteer', 'Computer Science Undergraduate, Meditation Coach- Enthusiast at Core Computers and Building Mobile Applications!', 'https://www.linkedin.com/in/harshitha-lingapalem-9b6981139/'],
            ['../static/images/team/core/LikhithaS.jpg', 'Likhitha S', 'Anchor', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/MuhammedShafi.jpg', 'Muhammed Shafi', 'Anchor & Designer', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/NikhilR.jpg', 'Nikhil R', 'Anchor', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/NishanthGowda.jpg', 'Nishanth Gowda', 'Social Media & Marketing', 'Computer Science Student | Data Science Enthusiast', 'http://linkedin.com/in/nishanth-gowda-102257194'],
            ['../static/images/team/core/Nithyashree.jpg', 'Nithyashree', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/PranavBedreGH.jpg', 'Pranav Bedre G H', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/Pruthvi.jpg', 'Pruthvi', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/Rituraj.jpg', 'Rituraj', 'ROLE', 'For me the world is binary, either its a 1 or a 0. To have loved and keep loving computers always, is my life. ', 'https://www.linkedin.com/in/ritu-raj-8992bb55/'],
            ['../static/images/team/core/SaarangGRajan.jpg', 'Saarang G Rajan', 'Social Media & Marketing', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/SamuelT.jpg', 'Samuel T', 'Anchor & Designer', 'Computer Science Student | Machine Learning Enthusiast', 'https://www.linkedin.com/in/samuel-t-87a494185/'],
            ['../static/images/team/core/Sashank.jpg', 'Sashank', 'ROLE', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/ShivalokeshReddy.jpg', 'Shivalokesh Reddy', 'Designer', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/ShrishtiShreya.jpg', 'Shrishti Shreya', 'ROLE', 'Computer Science Student | Web Developer Enthusiast', 'https://www.linkedin.com/in/shrishti-shreya-02828a190/'],
            ['../static/images/team/core/SkandhaGuruDutt.jpg', 'Skandha Guru Dutt', 'Social Media & Marketing', 'Computer Science Student | ML and Data Science Enthusiast', 'https://www.linkedin.com/in/skandha-n-29901816b/'],
            ['../static/images/team/core/SrirajAsnotikar.jpg', 'Sriraj Asnotikar', 'Social Media & Marketing', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/SurinMachaiahMT.jpg', 'Surin Machaiah M T', 'Community Partnership & Developer', 'Full Stack Developer | Web Developement | App Development | Android | Flutter | Machine Learning | Robotic Process Automation (RPA)', 'https://www.linkedin.com/in/surin-machaiah-m-t-57b00416b'],
            ['../static/images/team/core/YPrahasith.jpg', 'Y Prahasith', 'ROLE', 'CSE Student  | Full Stack Web Developer', 'https://www.linkedin.com/in/y-prahasith-12b829173/']]

    volunteer = [['../static/images/team/volunteer/AyushiMishra.jpg', 'Ayushi Mishra', 'ROLE', 'Data Science and Machine Learning | NIE IEEE Student Branch Core Member - Secretary MD | Foreign Policy and International Affairs enthusiast', 'www.linkedin.com/in/ayushi-mishra7474'],
                 ['../static/images/team/volunteer/Balachandra.png', 'Balachandra', 'Volunteer Lead, WiMLDS', 'Flutter Developer | Microsoft Learn Student Ambassador | Web developer', 'https://www.linkedin.com/in/balachandra-ds-9554391a0'],
                 ['../static/images/team/volunteer/DharithriM.jpg', 'DharithriM', 'ROLE', 'Web development | C/C++ programming | Python | Digital marketing | Event management', 'https://www.linkedin.com/in/dharithri-m'],
                 ['../static/images/team/volunteer/KumSomi.jpg', 'Kum Somi', 'Marketing', 'Beta-Microsoft Learn Student Ambassador | ML enthusiast | Poet ', 'https://www.linkedin.com/in/kum-somi-25aa8a152'],
                 ['../static/images/team/volunteer/SujayMudgal.jpg', 'Sujay Mudgal', 'Marketing ', 'I have my own startup and i have passion about business and marketing as these two play a very vital role in growing up of a Things', 'LINKEDIN'],
                 ['../static/images/team/volunteer/SujaAnchan.jpg', 'Suja Anchan', 'ROLE', 'Web Developer | Full Stack Developer', 'https://www.linkedin.com/in/suja-anchan-b5950619b'],
                 ['../static/images/team/volunteer/SwathiG.jpg', 'Swathi G', 'ROLE', 'BIO', 'https://www.linkedin.com/in/swathi-g-52a8181a0']]

    faculty = [['../static/images/team/faculty/AnanthGS.jpg', 'Ananth G S', 'Assistant Professor', 'MCA, NIE', 'A Teacher by Profession and a Learner for life. Currently pursuing a Doctorate degree in Information Retrieval and Machine Learning', 'https://www.linkedin.com/in/ananth-gouri-1b06356a'],
               ['../static/images/team/faculty/CKVanamala.jpg', 'C K Vanamala', 'Associate Professor', 'IS&E, NIE', 'Joint Student Welfare Officer and Cultural Coordinator, NIE | Wireless Sensor Networks', 'https://www.linkedin.com/in/vanamala-c-k-49b758168'],
               ['../static/images/team/faculty/DrAbhinandanSP.jpg', 'Dr. Abhinandan S P', 'Associate Professor', 'CS&E, NIE', 'Cloud computing | edge computing | networked systems | AI | distributed algorithms | education | system design | IoT', 'https://www.linkedin.com/in/abhinandan-s-p-00115817/'],
               ['../static/images/team/faculty/DrJayasriBS.jpg', 'Dr. Jayasri B S', 'Associate Professor', 'CS&E, NIE', 'Wireless sensor network- reliability and energy issues | Statistical modeling | Python | Rational rose | Networking', 'https://www.linkedin.com/in/dr-jayasri-b-s-360b9a176'],
               ['../static/images/team/faculty/MJYogesh.jpg', 'M J Yogesh', 'Assistant Professor','CS&E, NIE', 'Statistical Modeling | Databases | Big Data Analytics | Java | PhD in Big Data Analytics', 'https://www.linkedin.com/in/m-j-yogesh-47564376'],
               ['../static/images/team/faculty/SuhaasKP.jpg', 'Suhaas K P', 'Assistant Professor', 'IS&E, NIE', 'Research Scholar', 'https://www.linkedin.com/in/suhaas-k-p-6347464b']]

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
          ['12:50 PM', '01:10 PM', '-', 'Kavitha Dwivedi (ISM)', 'https://www.linkedin.com/in/kavitadwivedi/'],
          ['01:10 PM', '01:30 PM', '-', 'Dr.Lavanya Tekumalla', 'https://www.linkedin.com/in/lavanyats/'],
          ['01:30 PM', '01:50 PM', 'Prevent your Models from failing silently in Production', 'Sabari Lakshmi Krishnamoorthy (Saturam)', 'https://www.linkedin.com/in/sabari-lakshmi-k/'],
          ['01:50 PM', '02:10 PM', 'Actively Managing Risks with AI', 'Snigdha Ghosh (Paypal)', 'https://www.linkedin.com/in/snigdharay/'],
          ['02:10 PM', '02:30 PM', 'Inspirational Journey of Embibe (AI in education)', 'Aditi Avasthi', 'https://www.linkedin.com/in/aditiavasthi/']]

    d2 = [['10:30 AM', '10:50 AM', 'What can the shape of neighborhood show-and-tell?', 'Prof. Jaya Nair (IIT Bangalore)', 'https://www.linkedin.com/in/jayanair/'],
          ['10:50 AM', '11:10 AM', '-', 'Narmada Sambaturu (IISC)', 'https://www.linkedin.com/in/narmada-sambaturu-76155720/'],
          ['11:10 AM', '11:30 AM', 'Future and impact of AI, NLP', 'Dr.Anupama Ray (IBM Research)', 'https://www.linkedin.com/in/anupama-ray-55140826/'],
          ['11:30 AM', '11:50 AM', 'Big Buck Change in Banking', 'Vidhya Veeraraghavan', 'https://www.linkedin.com/in/vidhyaveeraraghavan/'],
          ['11:50 AM', '12:10 PM', 'Gender equality in tech', 'Deepti Rai (Senior Data Scientist - Policy Research, LinkedIn)', 'https://www.linkedin.com/in/dptrai/'],
          ['12:10 PM', '12:30 PM', 'Big omics data in Alzheimers disease', 'Dr. Aditi Verma', 'https: // www.linkedin.com / in / aditi - verma - b695aa3a / '],
          ['12:30 PM', '12:50 PM', 'AI driven Voice Solutions in Healthcare', 'Aishwarya Pathak (United Health)', 'https://www.linkedin.com/in/aishwarya-pathak-184382b5/?originalSubdomain=in'],
          ['12:50 PM', '01:10 PM', 'AI "Truth and Myth"', 'Siboli Mukherjee (MUST Research)', 'https://www.linkedin.com/in/siboli-m-4106757'],
          ['01:10 PM', '01:30 PM', 'From Text to Media - My Journey in AI since 2001', 'Amruta Purandare (Cinematrix)', 'https://www.linkedin.com/in/pamruta/'],
          ['01:30 PM', '01:50 PM', 'AWS Ecosystem for Big Data Analytics', 'Sridevi (Agilisium)', 'https://www.linkedin.com/in/sridevi-murugayen/'],
          ['01:50 PM', '02:10 PM', 'ML to supercharge a Conversational Commerce experience', 'Tina Mani (YFret)', 'https://www.linkedin.com/in/tinamani/']]

    d3 = [['10:30 AM', '10:50 AM', 'Connections and Differences in Data Science and Operations Research', 'Dr.Ansuya Ghosh (Thoucentric)', 'https://www.linkedin.com/in/dr-anusuya-ghosh-5a900bba/'],
          ['10:50 AM', '11:10 AM', 'AWS Introduction', 'Preethi (Fidelity Investments)', 'https://www.linkedin.com/in/preethi-n/'],
          ['11:10 AM', '11:30 AM', 'Advancements of AI in healthcare', 'Dr.Pooja Rajdev (United Health)', 'https://www.linkedin.com/in/poojarajdev/'],
          ['11:30 AM', '11:50 AM', 'Applications of AI in healthcare', 'Dr.Swetha (Medwell Ventures)', 'https://in.linkedin.com/in/swetachoudhary'],
          ['11:50 AM', '12:10 AM', 'Data Science in People Development: A 21st Century Perspective', 'Krupa Ravi (Google)', 'https://in.linkedin.com/in/kruparavi'],
          ['12:10 AM', '12:30 AM', '-', 'Preethy Varma', 'https://www.linkedin.com/in/preethy-varma-33b4aa59/'],
          ['12:30 AM', '12:50 AM', 'AI in Fintech', 'Meghana SuryaKumar (Crediwatch)', 'https://in.linkedin.com/in/meghnasuryakumar'],
          ['12:50 AM', '01:10 AM', '-', 'Aditi Sinha (Locale.ai)', 'https://in.linkedin.com/in/aditi-sinha-6b774ba9'],
          ['01:10 AM', '01:30 AM', 'Art of Storytelling', 'Swati Gaur (Kantar)', 'https://in.linkedin.com/in/swatigaur'],
          ['01:30 AM', '01:50 AM', '-', 'Geetha (Ugam Solutions)', 'https://in.linkedin.com/in/geetha-apathotharanan-2296b318'],
          ['01:50 AM', '02:10 AM', '-', 'Sonal Gupta (Bridgei2i)', 'https://in.linkedin.com/in/sonalgupta1981'],
          ['02:10 AM', '02:30 AM', 'Skills required for data scientist role', 'Jigna Thacker (Kantar World)', 'https://www.linkedin.com/in/jignathacker08/'],
          ['02:30 AM', '02:50 AM', 'Deep Learning advancements in Healthcare', 'Rajarajeshwari K (Arteleus)', 'https://www.linkedin.com/in/rajarajeshwari-k-16a22310/']]

    d4 = [['10:30 AM', '10:50 AM', '-', 'Srujana Kaddevarmuth', 'https://www.linkedin.com/in/srujana-kaddevarmuth-37a32b18/'],
          ['10:50 AM', '11:10 AM', '-', 'Lakshya Sivaramkrishnan (Google)', 'https://www.linkedin.com/in/lakshyasi/'],
          ['11:10 AM', '11:30 AM', '-', 'Sabari (Saturam)', 'https://in.linkedin.com/in/sabari-lakshmi-k'],
          ['11:30 AM', '11:50 AM', '-', 'Sayantika Banik , Board Member Django Software Foundation', 'https://www.linkedin.com/in/sayantika-banik/'],
          ['11:50 AM', '12:10 AM', '-', 'Sharmistha Chatterjee', 'https://www.linkedin.com/in/sharmistha-chatterjee-7a186310/'],
          ['12:10 AM', '12:30 AM', '-', 'Mythili Krishnan', 'https://www.linkedin.com/in/mythili-krishnan-94a5125/'],
          ['12:30 AM', '12:50 AM', '-', ' Deepika Sandeep', 'https://www.linkedin.com/in/deepika-sandeep/'],
          ['12:50 AM', '01:10 AM', '-', 'Ruhi Sharma Mittal (IBM Research)', 'https://www.linkedin.com/in/ruhi-sharma-mittal-4352a337/'],
          ['01:10 AM', '01:30 AM', '-', 'Swati Gaur(Kantar)', 'https://in.linkedin.com/in/swatigaur'],
          ['01:30 AM', '01:50 AM', 'Professor Manjira Sinha (IIT Kharagpur)', 'https://in.linkedin.com/in/manjira-sinha-8554b157'],
          ['01:50 AM', '02:10 AM', '-', 'Elenora', '-'],
          ['02:10 AM', '02:30 AM', '-', 'Aarthi Kumar', 'https://www.linkedin.com/in/aarthikumar/']]

    d5 = [['01:00 PM', '02:00 PM', '-', 'Reeti Pandey (United HealthGroup)', 'https://www.linkedin.com/in/reeti-pandey-3992bb131/'],
          ['02:00 PM', '03:00 PM', '-', ' Pavithra Solai Jawahar (Swiggy)', 'https://www.linkedin.com/in/pavithrasolai/'],
          ['03:00 PM', '04:00 PM', '-', 'Gnana Lakshmi T C (Wiley)', 'https://www.linkedin.com/in/gyan-lakshmi/'],
          ['04:00 PM', '05:00 PM', '-', 'Shreya khare', 'https://www.linkedin.com/in/shreya-khare-52b23718/'],
          ['05:00 PM', '06:00 PM', '-', 'Kavitha Yogaraj', 'https://www.linkedin.com/in/kavitha-yogaraj-b257aa30/']]

    d6 = [['01:00 PM', '02:00 PM', 'State of art models NLP with hands on with Bert', 'Madhumitha Behera (Yodlee)', 'https://www.linkedin.com/in/madhumita-behera-8185367b'],
          ['02:00 PM', '03:00 PM', '-', 'Chirasmita Mallick (G2)', 'https://www.linkedin.com/in/chirasmitamallick/'],
          ['03:00 PM', '04:00 PM', '-', 'Dr. C.S.Jyothirmayee Rao (Genomic Data Scientist)', 'https://www.linkedin.com/in/dr-c-s-jyothirmayee-rao-396b3715/'],
          ['04:00 PM', '05:00 PM', '-', 'Shrutika Poyrekar (Yodlee)', 'https://www.linkedin.com/in/shrutikapoyrekar/'],
          ['05:00 PM', '06:00 PM', '-', 'Priyamvada Joshi (Publicis Sapient)', 'https://www.linkedin.com/in/priyamvada-joshi-aa51b632/?originalSubdomain=in']]

    d7 = [['01:00 PM', '02:00 PM', '-', 'Tanmayee Narendra (Phd Student - Germany)', 'https://www.linkedin.com/in/tanmayeenarendra/'],
           ['02:00 PM', '03:00 PM', '-', 'Ranjani Swaminathan , Ramya Victor & Shwetha Lakshman Rao', ' '],
           ['03:00 PM', '04:00 PM', '-', 'Mamta Jha', 'https://www.linkedin.com/in/mamta-jha/'],
           ['04:00 PM', '05:00 PM', '-', 'Priyanka Sawant', 'https://www.linkedin.com/in/priyanka-sawant-49b35a18/'],
           ['05:00 PM', '06:00 PM', '-', 'Sukanya Mondal', 'https://www.linkedin.com/in/sukanya-mondal-b4872495/'],
           ['06:00 PM', '07:00 PM', '-', 'Shubha Shedthikere (Swiggy)', 'https://www.linkedin.com/in/shubha-shedthikere-233a3814/']]

    d8 = [['01:00 PM', '02:00 PM', 'Lightning Talks', '-', '-'],
           ['02:00 PM', '03:00 PM', '-', 'Charmi Chokshi (Shipmnts)', 'https://www.linkedin.com/in/charmichokshi/'],
           ['03:00 PM', '04:00 PM', '-', ' Shailaja Grover (IIM Bangalore)', 'https://www.linkedin.com/in/shailaja-grover-402a576a/'],
           ['04:00 PM', '05:00 PM', '-', 'Kumari Deepshikha', 'https://www.linkedin.com/in/deepkshikha/'],
           ['05:00 PM', '06:00 PM', '-', ' Mady Mantha', 'https://www.linkedin.com/in/madymantha/']]

    return render_template("agenda.html", d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, d7=d7, d8=d8)


@app.route('/datathon')
def datathon():
    return render_template("datathon.html")


if __name__ == '__main__':
    app.run(debug=True)