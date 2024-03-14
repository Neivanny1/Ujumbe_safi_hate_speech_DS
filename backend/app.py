from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash  # Import password hashing functions
import MySQLdb.cursors
from werkzeug.utils import secure_filename
import os

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
            return render_template('index.html', account=account)  # Pass 'pic' to the template
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



"""
home redirection
"""
@app.route('/home/')
def home():
    if 'loggedin' in session:
        return render_template('inde.html', username=session['username'], pic=session['pic'])
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
