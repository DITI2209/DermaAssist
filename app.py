from flask import Flask, request, render_template
import firebase_admin
from firebase_admin import credentials, auth, storage
import jinja2
from datetime import timedelta
import pyrebase
from flask import Flask, redirect, url_for, flash, session
from flask_session import Session


app = Flask(__name__)
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

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = None
        
        # Attempt to sign in with the given email and password
        error = False
        if not email or not password:
            error = True
            flash('Please enter your email and password.')
        else:
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                # session['user'] = email
            except auth.AuthError as e:
                # Handle any authentication errors
                error_code = e.detail.get('code')
                if error_code == 'EMAIL_NOT_FOUND':
                    error = True
                    flash('Invalid email address.')
                elif error_code == 'INVALID_PASSWORD':
                    error = True
                    flash('Invalid password.')
                else:
                    error = True
                    flash('An error occurred. Please try again later.')
        
        # If the user was successfully signed in, redirect to the upload page
        if user and not error:
            return redirect(url_for('upload'))
    
    # If the request method is GET, render the login page
    return render_template('login.html')

# @app.route('/login1')
# def login1():
#     return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            user = auth.create_user_with_email_and_password(email, password)
            # Redirect to the dashboard or homepage
            return redirect(url_for('login'))
        elif auth.get_user_by_email(email) is not None:
            # Handle email already exists error
            flash('Email already exists.')
        else:
            # Handle password mismatch error
            flash('Passwords do not match.')
    else:
        return render_template('signup.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Upload the file to Firebase Storage
            storage.child("images/"+file.filename).put(file)
            return 'Successful'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)