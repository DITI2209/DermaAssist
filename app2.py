import pyrebase
config = {
    "apiKey": "AIzaSyAR0XBuGC2yywq-q1DfQKfLl26LKk6l9K8",
  "authDomain": "fir-try-28f01.firebaseapp.com",
  "databaseURL": "https://fir-try-28f01-default-rtdb.firebaseio.com",
  "projectId": "fir-try-28f01",
  "storageBucket": "fir-try-28f01.appspot.com",
  "messagingSenderId": "588321601903",
  "appId": "1:588321601903:web:e072797fc9189e9465d09a",
  "measurementId": "G-04938M5W17"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()
from flask import Flask,render_template,request, session
from flask_session import Session
import jinja2
app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/getstarted', methods = ['GET', 'POST'])
def getstarted():
    return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    # if request.method == 'POST':
    #     pass1 = request.form['pass1']
    #     pass2 = request.form['pass2']
    #     if pass1 == pass2:
    #         if pass1:
    #             fname = request.form['fname']
    #             lname = request.form['lname']
    #             email = request.form['email']
    #             password = request.form['pass1']
    #             new_user = auth.create_user_with_email_and_password(email, password)
    #             auth.send_email_verification(new_user['idToken'])
    #             return render_template('verify_email.html')
    #         else:
    #             existing_account = "This email id has already been used"
    return render_template('signup.html')

@app.route('/login_signup', methods = ['GET', 'POST'])
def login_signup():
    return render_template('signup.html')

@app.route('/login_upload', methods = ['GET', 'POST'])
def login_upload():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
            return render_template('home.html')
        except:  
                return 'failed to login'
    return render_template('upload.html')

@app.route('/after_signup', methods = ['GET', 'POST'])
def after_signup():
    return render_template('login.html')

@app.route('/upload_to_db', methods = ['GET', 'POST'])
def upload_to_db():
    if request.method == 'POST':
        skin = request.files['skin']
        storage.child("images/"+skin.filename).put(skin)
        return 'Successful'
    return render_template('upload.html')

@app.route('/signup_login', methods = ['GET', 'POST'])
def signup_login():
    if request.method == 'POST':
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']
        if pass1 == pass2:
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            password = request.form['pass1']
            new_user = auth.create_user_with_email_and_password(email, password)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)