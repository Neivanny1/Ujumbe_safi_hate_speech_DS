import pickle
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import MySQLdb.cursors
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from googletrans import Translator
import re

app = Flask(__name__)

# Configure MySQL
# Set upload folder and allowed extensions for image uploads
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'crud'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'twitter'
mysql = MySQL(app)

# Set a secret key for session management
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account and check_password_hash(account['password'], password):
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            session['pic'] = account['profile_pic']
            session['fullname'] = account['fullname']
            return render_template('index.html', username=session['username'], pic=session['pic'])  # Pass 'pic' to the template
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)


"""
Adds a route to register users to the system
"""
@app.route('/register/', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        profile_pic = request.files['profile_pic']  # Get the uploaded file
        
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = 'Invalid email address. Please enter a valid email.'
            return render_template('register.html', msg=msg)
        
        # Validate password length
        if len(password) < 6:
            msg = 'Password must be at least 6 characters long.'
            return render_template('register.html', msg=msg)
        
        # Validate password complexity (e.g., at least one uppercase, one lowercase, one digit)
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$", password):
            msg = 'Password must contain at least one lowercase letter, one uppercase letter, and one digit.'
            return render_template('register.html', msg=msg)
        
        # Further validation logic for username, email uniqueness, etc.
        
        if profile_pic and allowed_file(profile_pic.filename):
            filename = secure_filename(profile_pic.filename)
            profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save the file to the server
            # Hashing the password using Werkzeug
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            # Pushing user data into the database
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO accounts (fullname, username, password, email, profile_pic) VALUES (%s, %s, %s, %s, %s)",
                           (fullname, username, hashed_password, email, filename,))  # Save file name in database
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return render_template('login.html', msg=msg)
        else:
            msg = 'Invalid file format. Please upload a valid image.'
    return render_template('register.html', msg=msg)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
'''
Getting all posts
'''
def get_all_tweets():
    with app.app_context():
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM posts ORDER BY timestamp DESC")
        posts = cursor.fetchall()
        cursor.close()
    
    return posts
    
@app.route('/posts')
def posts():
    posts = get_all_tweets()
    return render_template('posts.html', posts=posts)

@app.route('/redirect_to_posts')
def redirect_to_posts():
    return redirect('/posts')

"""
home redirection
"""
@app.route('/home/')
def home():
    if 'loggedin' in session:
        return render_template('index.html', posts=get_all_tweets(), username=session['username'], pic=session['pic'])
    return redirect(url_for('login'))


def load_tfidf():
    tfidf = pickle.load(open("tf_idf.pkt", "rb"))
    return tfidf

def load_model():
    nb_model = pickle.load(open("toxicity_model.pkt", "rb"))
    return nb_model
def toxicity_prediction(text):
    tfidf = load_tfidf()
    text_tfidf = tfidf.transform([text]).toarray()
    nb_model = load_model()
    prediction = nb_model.predict(text_tfidf)
    class_name = "Toxic" if prediction == 1 else "Non-Toxic"
    return class_name

def swahili_to_english(tweet):
    translator = Translator()
    translation = translator.translate(tweet, dest='en')
    return translation.text

@app.route('/create_post', methods=['POST'])
def create_post():
    if request.method == 'POST':
        if 'loggedin' in session:
            current_user = session['id']
            fullname = session['fullname']
            username = session['username']
            tweet = request.form['tweet']
            pic = request.files['post_pic']
            # Validate tweet length
            if len(tweet) > 280:
                flash("Tweet is too long. Please keep it under 280 characters.")
                return redirect(url_for('home'))
            res = swahili_to_english(tweet)
            toxicity = toxicity_prediction(res)
            if toxicity == "Toxic":
                flash("Error: Tweet contains toxic content. You cannot post toxic tweets.")
                return redirect(url_for('home'))

            timestamp = datetime.now()

            try:
                # Retrieve profile pic from session
                profile_pic = session.get('pic', '')

                if pic and allowed_file(pic.filename):
                    filename = secure_filename(pic.filename)
                    # Store only the file name
                    post_pic = filename
                    # Save the post picture to the upload folder
                    pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                else:
                    post_pic = None

                cursor = mysql.connection.cursor()

                # Insert the new post into the 'posts' table
                cursor.execute("INSERT INTO posts (user_id, fullname, username, tweet, post_pic, profile_pic, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                               (current_user, fullname, username, tweet, post_pic, profile_pic, timestamp))

                # Commit the transaction and close the cursor
                mysql.connection.commit()
                cursor.close()

                flash("Tweet posted successfully!")
                return redirect(url_for('home'))  # Redirect to the 'home' endpoint

            except Exception as e:
                # Rollback the transaction in case of error
                mysql.connection.rollback()
                flash("An error occurred while creating the post: " + str(e))
                return redirect(url_for('home'))

    return redirect(url_for('login'))
@app.route('/manual')
def manual_test():
    return render_template('testpage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
