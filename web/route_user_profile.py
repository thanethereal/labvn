from flask import Flask, render_template, request, jsonify, redirect, url_for
from __main__ import app
from database.services.user_service import UserService, UserProfileService

@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user():
    users = UserProfileService.merge_user_user_profile()
    return render_template('edit_user.html', users=users)

@app.route('/update_user/<int:item_id>', methods=['GET', 'POST'])
def update_user(item_id):
    if request.method == 'POST':
        image_url = request.form['image_url']
        description= request.form['description']
        role = request.form['role']
        link_facebook = request.form['linkfacebook']
        link_instagram= request.form['linkinsta']
        link_zalo = request.form['linkzalo']
        UserProfileService.update_profile(user_id=item_id, avatar=image_url, bio=description, role=role, link_facebook=link_facebook, link_instagram=link_instagram, link_zalo=link_zalo)
        return redirect(url_for('edit_user'))
    # Render template cho trang sửa
    return render_template('edit_user.html')
