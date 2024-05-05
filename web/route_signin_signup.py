from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)
from database.services.user_service import UserService
from database.models.user import *
from flask import session
# Route để xử lý đăng ký
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    # Kiểm tra xem người dùng đã tồn tại chưa
    user = UserService.get_user_by_email(email=email)
    if user:
        return jsonify({'error': 'Email is existed!'})
    try:
        UserService.create_user(name=name, email=email, password=password)
        return redirect(url_for('signin'))
    except:
        return jsonify({'error': 'All fields are required!'})

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = UserService.login(email, password)
    if user:
        session['user_id'] = user.id  # Lưu user_id vào session
        return render_template('dashboard.html')
    else:
        return jsonify({'error': 'Email or password is wrong!'})


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('signin'))
