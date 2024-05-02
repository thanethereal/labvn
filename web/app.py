from flask import Flask, render_template, request, jsonify, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
app = Flask(__name__)

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

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

