from flask import Flask, render_template, request, jsonify, redirect, url_for
from app import app
from database.services.user_service import UserService, UserProfileService

from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/usr/share/nginx/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    users = UserProfileService.merge_user_user_profile()
    return render_template('edit_user.html', users=users)

@app.route('/update_user/<int:item_id>', methods=['GET', 'POST'])
def update_user(item_id):
    if request.method == 'POST':
        description= request.form['description']
        role = request.form['role']
        link_facebook = request.form['linkfacebook']
        link_instagram= request.form['linkinsta']
        link_zalo = request.form['linkzalo']
        if 'image_upload' in request.files:
            image_file = request.files['image_upload']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename
        else:
            # If no image file is provided, keep the existing image URL
            image_url = request.form['image_upload']
        UserProfileService.update_profile(user_id=item_id, avatar=image_url, bio=description, role=role, link_facebook=link_facebook, link_instagram=link_instagram, link_zalo=link_zalo)
        return redirect(url_for('edit_user'))
    # Render template cho trang sửa
    return render_template('edit_user.html')
