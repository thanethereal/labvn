from flask import Flask, render_template, request, jsonify, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abff871c328c0a26747c2ee71bb3000e16a60840a4373b54'
import route_signin_signup 
import route_home_page
import route_beach_bar_and_restaurant
import route_accommondation
import route_activities
import route_getting_here
import route_our_story
import route_post
import route_user_profile
import route_header_image
import route_footer
import os
from flask import request
# UPLOAD_FOLDER = 'D:/labvn/web/static/uploads/'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/uploads')
# def index():
#     return render_template('uploads.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return 'No file part'
#     file = request.files['file']
#     if file.filename == '':
#         return 'No selected file'
#     if file and allowed_file(file.filename):
#         filename = file.filename
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         return 'File uploaded successfully'
#     else:
#         return 'File type not allowed'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

