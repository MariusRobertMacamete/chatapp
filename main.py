import os
from flask import Flask, render_template, url_for, request, redirect, flash
app = Flask(__name__)
#

FOLDER = os.path.join('static')
app.config['UPLOAD_FOLDER'] = FOLDER
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Male-Avatar.png')
full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'Male-Avatar.png')
full_filename3 = os.path.join(app.config['UPLOAD_FOLDER'], 'Male-Avatar.png')
full_filename0 = os.path.join(app.config['UPLOAD_FOLDER'], 'Male-Avatar.png')

list = {
        'profile':full_filename0,
        'key':[1, 2, 3, 4, 5],
        'photo':[full_filename,full_filename2,full_filename3],
        'text':['abc', 'cde', 'efg']
        }

@app.route("/")
def index():
    return render_template("index.html", list = list)

class FriendsAction():
    def __init__(self):
        pass
        #connect to tinydb

    def get_friends_list(self):
        pass

if __name__ =="__main__":
	app.run(host = '0.0.0.0',port=5000, debug = True)
