from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash  # Import password hashing functions
import MySQLdb.cursors
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

# Configure MySQL
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'crud'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'twitter'
mysql = MySQL(app)

def get_all_tweets():
    with app.app_context():  # Ensure access to the MySQL connection within the application context
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        cursor.close()
    
    return posts



posts = get_all_tweets()

print(posts)
print('Type: ', type(posts))  # Add this line to check if posts are retrieved
