# Ujumbe_safi_hate_speech_DS
# Ujumbe Model 
This is a model that is used to predict the sentiment of a given text.
## Project Structure
cisco@labvm:~/Desktop/Ujumbe_safi_hate_speech_DS$ tree
.
├── backend
│   ├── api.py
│   ├── app.py
│   ├── database.sql
│   ├── images
│   ├── __pycache__
│   │   └── test.cpython-38.pyc
│   ├── README.md
│   ├── requirements.txt
│   ├── static
│   │   ├── css
│   │   │   ├── login.css
│   │   │   ├── styles.css
│   │   │   └── teststyles.css
│   │   ├── images
│   │   │   ├── bg.png
│   │   │   ├── blurry-twitter-image.jpeg
│   │   │   ├── car.jpg
│   │   │   ├── fonta.png
│   │   │   ├── fontb.png
│   │   │   └── profile.png
│   │   ├── js
│   │   │   └── testscript.js
│   │   └── uploads
│   │       ├── car.jpg
│   │       ├── fontb.png
│   │       ├── img.png
│   │       ├── keyboard.jpg
│   │       ├── profile.png
│   │       ├── rcom.png
│   │       ├── search.png
│   │       └── student_f.png
│   ├── templates
│   │   ├── analyse.html
│   │   ├── bootstrap.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── posts.html
│   │   ├── register.html
│   │   ├── test.html
│   │   └── testpage.html
│   ├── tf_idf.pkt
│   └── toxicity_model.pkt
├── datasets
│   ├── hate1.csv
│   ├── hate.csv
│   └── hate_tweets.csv
├── frontend
│   ├── about
│   │   ├── index.html
│   │   ├── slider.js
│   │   └── style.css
│   ├── html css website
│   │   ├── images
│   │   │   ├── about.jpeg
│   │   │   ├── icon-1.svg
│   │   │   ├── icon-2.svg
│   │   │   ├── icon-3.svg
│   │   │   ├── icon-4.svg
│   │   │   ├── icon-5.svg
│   │   │   ├── icon-6.svg
│   │   │   ├── portfolio-1.jpg
│   │   │   ├── portfolio-2.jpg
│   │   │   ├── portfolio-3.jpg
│   │   │   ├── portfolio-4.jpg
│   │   │   ├── portfolio-5.jpg
│   │   │   └── portfolio-6.jpg
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   ├── images
│   │   ├── car.jpg
│   │   └── profile.png
│   ├── index.html
│   ├── styles.css
│   └── test-page
│       ├── bg.png
│       ├── blurry-twitter-image.jpeg
│       ├── fonta.png
│       ├── fontb.png
│       ├── testpage.html
│       ├── testscript.js
│       └── teststyles.css
├── notebooks
│   ├── clean.ipynb
│   ├── model_train.ipynb
│   └── Toxicity_Classifier.ipynb
└── README.md

17 directories, 71 files
cisco@labvm:~/Desktop/Ujumbe_safi_hate_speech_DS$ tree 
.
├── backend
│   ├── api.py
│   ├── app.py
│   ├── database.sql
│   ├── images
│   ├── __pycache__
│   │   └── test.cpython-38.pyc
│   ├── README.md
│   ├── requirements.txt
│   ├── static
│   │   ├── css
│   │   │   ├── login.css
│   │   │   ├── styles.css
│   │   │   └── teststyles.css
│   │   ├── images
│   │   │   ├── bg.png
│   │   │   ├── blurry-twitter-image.jpeg
│   │   │   ├── car.jpg
│   │   │   ├── fonta.png
│   │   │   ├── fontb.png
│   │   │   └── profile.png
│   │   ├── js
│   │   │   └── testscript.js
│   │   └── uploads
│   │       ├── car.jpg
│   │       ├── fontb.png
│   │       ├── img.png
│   │       ├── keyboard.jpg
│   │       ├── profile.png
│   │       ├── rcom.png
│   │       ├── search.png
│   │       └── student_f.png
│   ├── templates
│   │   ├── analyse.html
│   │   ├── bootstrap.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── posts.html
│   │   ├── register.html
│   │   ├── test.html
│   │   └── testpage.html
│   ├── tf_idf.pkt
│   └── toxicity_model.pkt
├── datasets
│   ├── hate1.csv
│   ├── hate.csv
│   └── hate_tweets.csv
├── frontend
│   ├── about
│   │   ├── index.html
│   │   ├── slider.js
│   │   └── style.css
│   ├── html css website
│   │   ├── images
│   │   │   ├── about.jpeg
│   │   │   ├── icon-1.svg
│   │   │   ├── icon-2.svg
│   │   │   ├── icon-3.svg
│   │   │   ├── icon-4.svg
│   │   │   ├── icon-5.svg
│   │   │   ├── icon-6.svg
│   │   │   ├── portfolio-1.jpg
│   │   │   ├── portfolio-2.jpg
│   │   │   ├── portfolio-3.jpg
│   │   │   ├── portfolio-4.jpg
│   │   │   ├── portfolio-5.jpg
│   │   │   └── portfolio-6.jpg
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   ├── images
│   │   ├── car.jpg
│   │   └── profile.png
│   ├── index.html
│   ├── styles.css
│   └── test-page
│       ├── bg.png
│       ├── blurry-twitter-image.jpeg
│       ├── fonta.png
│       ├── fontb.png
│       ├── testpage.html
│       ├── testscript.js
│       └── teststyles.css
├── notebooks
│   ├── clean.ipynb
│   ├── model_train.ipynb
│   └── Toxicity_Classifier.ipynb
└── README.md

17 directories, 71 files
### Backend Folder
This folder holds the backend code for the application.
Hosts the model and the API.

### Frontend Folder
This folder holds the frontend code for the application.

Hosts the UI.
### Dataset Folder
This folder holds the dataset used for the application and Trainig the model
### Notebooks
This folder holds the notebooks used for the application. Contains code used to trained the model.
Kindly test the notebooks with google coolab
### However all these are intergrated inside backend folder hence touch backend folder with caution.
## Installation
1. git clone https://github.com/Neivanny1/Ujumbe_safi_hate_speech_DS.git
2. cd Ujumbe_safi_hate_speech_DS
3. python3 -m venv env
4. source env/bin/activate
5. cd backend
6. pip install -r requirements.txt
7. python3 app.py
8. Go to web browser and type localhost:5000

## DEMO
