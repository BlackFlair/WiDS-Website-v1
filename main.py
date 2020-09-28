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
            ['../static/images/team/core/ShrishtiShreya.jpg', 'Shrishti Shreya', 'Anchor', 'Computer Science Student | Web Developer Enthusiast', 'https://www.linkedin.com/in/shrishti-shreya-02828a190/'],
            ['../static/images/team/core/SkandhaGuruDutt.jpg', 'Skandha Guru Dutt', 'Social Media & Marketing', 'Computer Science Student | ML and Data Science Enthusiast', 'https://www.linkedin.com/in/skandha-n-29901816b/'],
            ['../static/images/team/core/SrirajAsnotikar.jpg', 'Sriraj Asnotikar', 'Social Media & Marketing', 'BIO', 'LINKEDIN'],
            ['../static/images/team/core/SurinMachaiahMT.jpg', 'Surin Machaiah M T', 'Community Partnership & Developer', 'Full Stack Developer | Web Developement | App Development | Android | Flutter | Flask | Machine Learning | Robotic Process Automation (RPA)', 'https://www.linkedin.com/in/surin-machaiah-m-t-57b00416b'],
            ['../static/images/team/core/YPrahasith.jpg', 'Y Prahasith', 'ROLE', 'CSE Student  | Full Stack Web Developer', 'https://www.linkedin.com/in/y-prahasith-12b829173/']]

    volunteer = [['../static/images/team/volunteer/AyushiMishra.jpg', 'Ayushi Mishra', 'ROLE', 'Data Science and Machine Learning | NIE IEEE Student Branch Core Member - Secretary MD | Foreign Policy and International Affairs enthusiast', 'www.linkedin.com/in/ayushi-mishra7474'],
                 ['../static/images/team/volunteer/Balachandra.png', 'Balachandra', 'Volunteer Lead, WiMLDS', 'Flutter Developer | Microsoft Learn Student Ambassador | Web developer', 'https://www.linkedin.com/in/balachandra-ds-9554391a0'],
                 ['../static/images/team/volunteer/Bharath.jpg', 'Bharath Narayan Puthane', 'ROLE', 'ISE Student | WiDS, Mysore Volunteer | Tech Enthusiast | Front - End Designer ', 'https://www.linkedin.com/in/bharath-n-puthane-349b441a4'],
                 ['../static/images/team/volunteer/DharithriM.jpg', 'DharithriM', 'ROLE', 'Web development | C/C++ programming | Python | Digital marketing | Event management', 'https://www.linkedin.com/in/dharithri-m'],
                 ['../static/images/team/volunteer/GanyaJ.jpeg', 'GanyaJ', 'ROLE', 'Computer Science Student | Data Science Enthusiast | Intern  at Progate | Debate Enthusiast and into writing', 'https://www.linkedin.com/in/ganya-janardhan'],
                 ['../static/images/team/volunteer/KumSomi.jpg', 'Kum Somi', 'Marketing', 'Beta-Microsoft Learn Student Ambassador | ML enthusiast | Poet ', 'https://www.linkedin.com/in/kum-somi-25aa8a152'],
                 ['../static/images/team/volunteer/SujayMudgal.jpg', 'Sujay Mudgal', 'Marketing ', 'I have my own startup and i have passion about business and marketing as these two play a very vital role in growing up of a Things', 'LINKEDIN'],
                 ['../static/images/team/volunteer/SujaAnchan.jpg', 'Suja Anchan', 'ROLE', 'Web Developer | Full Stack Developer', 'https://www.linkedin.com/in/suja-anchan-b5950619b'],
                 ['../static/images/team/volunteer/SwathiG.jpg', 'Swathi G', 'ROLE', 'BIO', 'https://www.linkedin.com/in/swathi-g-52a8181a0'],
                 ['../static/images/team/volunteer/VishruthS.jpg', 'Vishruth S', 'ROLE', 'Computer Science Student | Data Science Enthusiast', 'http://www.linkedin.com/in/vishruths16022000 ']]

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

    d3 = [['09:50 AM', '09:55 AM', 'WiDS Opening Video','-', '-'],
          ['09:55 AM', '10:00 AM', 'WiDS Mysuru Introduction', '-', '-'],
          ['10:00 AM', '10:30 AM', 'GSSS University Team - Welcome Note', '-', '-'],
          ['10:30 AM', '10:50 AM', 'Connections and Differences in Data Science and Operations Research', 'Dr.Ansuya Ghosh (Thoucentric)', 'https://www.linkedin.com/in/dr-anusuya-ghosh-5a900bba/'],
          ['10:50 AM', '11:10 AM', 'AWS Introduction', 'Preethi (Fidelity Investments)', 'https://www.linkedin.com/in/preethi-n/'],
          ['11:10 AM', '11:30 AM', 'Medical practitioners viewpoint on Covid Analytics', 'Dr.Swetha Choudhary (Medwell Ventures)', 'https://in.linkedin.com/in/swetachoudhary'],
          ['11:30 AM', '11:50 AM', 'Data Science in People Development: A 21st Century Perspective', 'Krupa Ravi (Google)', 'https://in.linkedin.com/in/kruparavi'],
          ['11:50 AM', '12:10 PM', 'A quick look at OpenAI’s GPT3', 'Preethy Varma', 'https://www.linkedin.com/in/preethy-varma-33b4aa59/'],
          ['12:10 PM', '12:30 PM', 'Art of Storytelling', 'Swati Gaur (Kantar)', 'https://in.linkedin.com/in/swatigaur'],
          ['12:30 PM', '12:50 PM', 'Data platform for AI / ML', 'Geetha Apathotharanan (Ugam Solutions)', 'https://in.linkedin.com/in/geetha-apathotharanan-2296b318'],
          ['12:50 PM', '01:10 PM', 'Women in Data Science Portfolio', 'Jigna Thacker (Kantar Worldpanel)', 'https://www.linkedin.com/in/jignathacker08/'],
          ['01:10 PM', '01:30 PM', 'Applied Data Science for SDGs', 'Parvathy Krishnan', 'https://www.linkedin.com/in/parvathykrishnank/'],
          ['01:30 PM', '01:50 PM', 'Arena of anomaly detection', 'Smitha Ganesh(Ericsson)', 'https://www.linkedin.com/in/smitha-ganesh-bb883418/']]

    d4 = [['09:40 AM', '09:50 AM', 'WiDS Opening Video','-', '-'],
          ['09:50 AM', '09:55 AM', 'WiDS Mysuru Introduction', '-', '-'],
          ['09:55 AM', '10:20 AM', 'Data Science for Sustainable Development Goals', 'Srujana Kaddevarmuth', 'https://www.linkedin.com/in/srujana-kaddevarmuth-37a32b18/'],
          ['10:20 AM', '10:40 AM', 'Key Driver Analysis of customer experience', 'Eleonora Nazander', 'https://www.linkedin.com/in/eleonoranazander/'],
          ['10:40 AM', '11:00 AM', 'Understanding Communities', 'Sayantika Banik , Board Member Django Software Foundation', 'https://www.linkedin.com/in/sayantika-banik/'],
          ['11:00 AM', '11:20 AM', 'Fair Recommendation systems', 'Sharmistha Chatterjee', 'https://www.linkedin.com/in/sharmistha-chatterjee-7a186310/'],
          ['11:20 AM', '11:40 AM', 'Failure Prediction for Servers/Web Applications using Anomaly Detection', 'Mythili Krishnan', 'https://www.linkedin.com/in/mythili-krishnan-94a5125/'],
          ['12:00 PM', '12:20 PM', 'Data Quality for Machine Learning', 'Ruhi Sharma Mittal (IBM Research)', 'https://www.linkedin.com/in/ruhi-sharma-mittal-4352a337/'],
          ['12:20 PM', '12:40 PM', 'Advancements in NLP Research', 'Prof. Manjira Sinha (IIT Kharagpur)', 'https://in.linkedin.com/in/manjira-sinha-8554b157'],
          ['12:40 PM', '01:00 PM', 'Data science in the accounting world', 'Aarthi Kumar', 'https://www.linkedin.com/in/aarthikumar/'],
          ['01:00 PM', '01:20 PM', 'Distributed Data and Personalized Predictions', 'Charmi Chokshi', 'https://www.linkedin.com/in/charmichokshi/'],
          ['01:20 PM', '01:40 PM', 'How data science makes its way into agriculture?', 'Ananya', 'https://www.linkedin.com/in/ananya-r'],
          ['01:40 PM', '02:00 PM', 'Continuous delivery of data pipelines', 'Sabari Lakshmi Krishnamoorthy(Saturam)', 'https://www.linkedin.com/in/sabari-lakshmi-k/']]

    d5 = [['12:00 PM', '12:20 PM', 'Actively Managing Risks with AI','Snigdha Ghosh Ray(Paypal)', 'https://www.linkedin.com/in/snigdharay/'],
          ['12:20 PM', '12:40 PM', 'Fairness in machine learning', 'Lakshya Sivaramakrishnan (Google)', 'https://www.linkedin.com/in/lakshyasi/'],
          ['12:40 PM', '01:00 PM', 'Machine learning approach for personalized genomics', 'Shreya Sharma (Medgenome)', 'https://www.linkedin.com/in/shreya-sharma-245871139/'],
          ['01:00 PM', '02:00 PM', 'Demystifying Time Series', 'Ranjani Swaminathan , Ramya Victor and Shwetha Lakshman Rao(VMware)', '-'],
          ['02:00 PM', '03:00 PM', 'Face and Mask Detection using Feature Pyramid Networks', 'Pavithra Solai Jawahar (Swiggy)', 'https://www.linkedin.com/in/pavithrasolai/'],
          ['03:00 PM', '04:00 PM', 'Introduction to Quantum Computing', 'Kavitha Yogaraj , Carmen Recio Valcarce ( IBM Quantum)', '-'],
          ['04:00 PM', '05:00 PM', 'Deep learning systems for voice recognition', 'Shreya khare (IBM Research)', 'https://www.linkedin.com/in/shreya-khare-52b23718/'],
          ['05:00 PM', '07:00 PM', 'Blockchain evolution: From Bitcoin to Algorand', 'Gnana Lakshmi T C (Wiley)', 'https://www.linkedin.com/in/gyan-lakshmi/'],
          ['07:00 PM', '07:20 PM', 'NLP based Chatbot', 'Khushi Rj (IBM)', 'https://www.linkedin.com/in/khushi-rj-64562762/'],
          ['07:20 PM', '07:40 PM', 'Genomic perspective of biology and Sequencing.', 'Sanjukta Dutta (Cognizant)', 'https://www.linkedin.com/in/sanjukta-dutta-9a0224156/'],
          ['07:40 PM', '08:00 PM', 'Building Custom Scalable Face Recognition Pipeline', 'Dimple Bansal (Couture.ai)', 'https://www.linkedin.com/in/dimple-bansal-8b985981/']]

    d6 = [['12:00 PM', '12:20 PM', 'AI in telecom in the era of 5G and IoT','Shalini Sinha', 'https://www.linkedin.com/in/shalinisinha79bi/'],
          ['12:20 PM', '12:40 PM', 'Explainable Models', 'Richa Sharma', 'https://www.linkedin.com/in/richa-sharma-808102121/'],
          ['12:40 PM', '01:00 PM', 'Kisan Suvidha: Blockchain & AI System To Help Farmers In India', 'Laisha Wadhwa', 'https://www.linkedin.com/in/laisha-wadhwa/'],
          ['01:00 PM', '02:00 PM', 'State of art models NLP with hands on with Bert', 'Madhumitha Behera (Yodlee)', 'https://www.linkedin.com/in/madhumita-behera-8185367b'],
          ['02:00 PM', '03:00 PM', 'Language models and New era in NLP research', 'Chirasmita Mallick (G2)', 'https://www.linkedin.com/in/chirasmitamallick/'],
          ['04:00 PM', '05:00 PM', 'Graph embedding in hyperbolic space', 'Shrutika Poyrekar (Yodlee)', 'https://www.linkedin.com/in/shrutikapoyrekar/'],
          ['05:00 PM', '06:00 PM', 'Market basket analysis', 'Priyamvada Joshi (Publicis Sapient)', 'https://www.linkedin.com/in/priyamvada-joshi-aa51b632/?originalSubdomain=in'],
          ['06:00 PM', '06:20 PM', 'Hypothesis testing - for mean and proportion.', 'Julian Sara Joseph', 'https://www.linkedin.com/in/julian-s-joseph/'],
          ['06:20 PM', '06:40 PM', 'Behavioral Biometric approach to User Authentication', 'Karthika kamath', 'https://www.linkedin.com/in/karthika-kamath/'],
          ['06:40 PM', '07:00 PM', 'Epigenetics: The Neglected Paradigm', 'Pratiksha Sable , Vinita khot (MUST Research)', '-'],
          ['07:00 PM', '07:20 PM', 'Web Scraping Google Play Store using Selenium', 'Lavanya Gupta', 'https://www.linkedin.com/in/lgupta18/'],
          ['07:20 PM', '07:40 PM', 'Data Quality- Framework & Actions', 'Shilpa Arora', 'https://www.linkedin.com/in/shilpa-arora-84aba149/'],
          ['06:00 PM', '06:20 PM', 'Lessons of Data Science', 'Dr.Neha Sharma', 'https://www.linkedin.com/in/dr-neha-sharma-2127141b/']]

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

@app.route('/registration')
def registration():
    details = [['Day 1: Saturday, 5 September, 2020', ],
               ['DAY 2: Sunday, 6 September, 2020', ],
               ['DAY 3: Sunday, 12 September, 2020', 'https://www.shorturl.at/ghixN'],
               ['DAY 4: Sunday, 13 September, 2020', 'https://www.shorturl.at/nwBT9'],
               ['DAY 5: Sunday, 19 September, 2020', 'https://www.shorturl.at/flnwX'],
               ['DAY 6: Sunday, 20 September, 2020', 'https://www.shorturl.at/hmqPQ'],
               ['DAY 7: Sunday, 26 September, 2020', 'https://www.shorturl.at/sEPRU'],
               ['DAY 8: Sunday, 27 September, 2020', 'https://www.shorturl.at/juzBO']]

    return render_template("registration.html", details=details)


if __name__ == '__main__':
    app.run(debug=True)