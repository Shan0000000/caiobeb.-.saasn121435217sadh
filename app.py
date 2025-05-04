import os
from flask import Flask, render_template,request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv




load_dotenv()





app = Flask(__name__)

# Set the absolute path for the database file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
app.config['SECRET_KEY'] = '05052010'

USERNAME = "jim" 
PASSWORD = "05052025"



# Routes
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form.get("username")
        pw = request.form.get("password")
        user = user.lower()

    
        if user == USERNAME and pw == PASSWORD:
            return redirect(url_for('shallwe'))
        else:
            flash("Incorrect username or password!")

    
    return render_template("index.html")





@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route("/home",methods=['GET', 'POST'])

def home():

    
    return render_template('home.html')


@app.route("/shallwe",methods=['GET', 'POST'])
def shallwe():
                  


        
    return render_template('shallwe.html')


@app.route("/bday",methods=['GET', 'POST'])
def bday():


    return render_template('bday.html')

@app.route("/result",methods=['GET', 'POST'])

def result():
    if request.method == 'POST':
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        q3 = request.form.get('q3').strip()
        q4 = request.form.get('q4').lower().strip()

        if q1 != '':
            c1 = """সত্যি বলতে আমি ঠিক জানিনা।
একটা যুক্তি দার করিয়েছিলাম ভালোই এক বছর আগে।
তবে যুক্তিতা এতই যুক্তিহীন যে, সেটার কথা তোলা সময় নষ্ট ছাড়া  আর কিছুনা।
আসলে কোনো মানেই হয়না।আবার অনেক মানেও হয়।
যদিও শেষটা ভালো না তবে, মানুষ হিসেবে দুজনই পরিবর্তিত হয়।
উন্নতি কিংবা অবনতি,  দূটোর একটা তো হবেই।
It hurts but it changes too. 
And we need changes to live
            
            
              """
        else:
            c1 = """ বলেছিলাম তো,  প্রত্যেক ক্রিয়ার সমান ও বিপরীত প্রতিক্রিয়া আছে।
                এই ফাকা পেইজই সেই প্রতিক্রিয়া। """


     

    msg = EmailMessage()
    msg['Subject'] = 'New Form Submission'
    msg['From'] = 'nsbur494@gmail.com'  # use your email
    msg['To'] = 'nsbur494@gmail.com'    # send it to yourself
    EMAIL_ADDRESS = 'nsbur494@gmail.com'
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    msg.set_content(f"""
    Q1: {q1}
   
    """)

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('nsbur494@gmail.com', EMAIL_PASSWORD)
        smtp.send_message(msg)


    return render_template('result.html',
    q1=q1,c1=c1)




# Main execution
if __name__ == "__main__":
    with app.app_context():
        app.run()

