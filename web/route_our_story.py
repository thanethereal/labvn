from flask import Flask, render_template, request, jsonify, redirect, url_for
from app import app
from database.services.our_story_service import OurStoryService, TourismBenefitEveryoneService
from database.services.user_service import UserProfileService
from database.services.header_image_service import HeaderImageService
from database.services.footer_service import FooterService

from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/usr/share/nginx/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/aboutus')
def aboutus():
    our_story = OurStoryService.get_all_our_stories()
    tourism_benefit_everyones = TourismBenefitEveryoneService.get_all_tourism_benefit_everyones()
    profiles = UserProfileService.merge_user_user_profile()
    header_image = HeaderImageService.get_header_image_by_id(6)
    footer = FooterService.get_footer_by_id(1)
    return render_template('aboutus.html',our_story=our_story, tourism_benefit_everyones=tourism_benefit_everyones, profiles=profiles, header_image=header_image, footer=footer)

@app.route('/edit_our_story', methods=['GET', 'POST'])
def edit_our_story():
    data = OurStoryService.get_all_our_stories()
    return render_template('edit_our_story.html', data=data)


@app.route('/add_our_story', methods=['POST'])
def add_our_story():
    text = request.form['text']
    image_file = request.files['image_file']
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_url = filename
    OurStoryService.add_our_story(text=text, image_url=image_url)
    return redirect(url_for('edit_our_story'))

@app.route('/update_our_story/<int:item_id>', methods=['GET', 'POST'])
def update_our_story(item_id):
    if request.method == 'POST':
        text = request.form['text']
        if 'image_upload' in request.files:
            image_file = request.files['image_upload']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename
        else:
            # If no image file is provided, keep the existing image URL
            image_url = request.form['image_upload']
        OurStoryService.update_our_story(item_id, text, image_url)
        return redirect(url_for('edit_our_story'))
    return render_template('edit_our_story.html')

@app.route('/delete_our_story/<int:item_id>')
def delete_our_story(item_id):
    OurStoryService.delete_our_story(item_id)
    return redirect(url_for('edit_our_story'))

@app.route('/edit_tourism_benefit_everyone', methods=['GET', 'POST'])
def edit_tourism_benefit_everyone():
    data = TourismBenefitEveryoneService.get_all_tourism_benefit_everyones()
    return render_template('edit_tourism_benefit_everyone.html', data=data)

@app.route('/add_tourism_benefit_everyone', methods=['POST'])
def add_edit_tourism_benefit_everyone():
    text = request.form['text']
    image_file = request.files['image_file']
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_url = filename
    TourismBenefitEveryoneService.add_tourism_benefit_everyone(text=text, image_url=image_url)
    return redirect(url_for('edit_tourism_benefit_everyone'))

@app.route('/update_tourism_benefit_everyone/<int:item_id>', methods=['GET', 'POST'])
def update_tourism_benefit_everyone(item_id):
    if request.method == 'POST':
        text = request.form['text']
        if 'image_upload' in request.files:
            image_file = request.files['image_upload']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename
        else:
            # If no image file is provided, keep the existing image URL
            image_url = request.form['image_upload']
        TourismBenefitEveryoneService.update_tourism_benefit_everyone(item_id, text, image_url)
        return redirect(url_for('edit_tourism_benefit_everyone'))
    return render_template('edit_tourism_benefit_everyone.html')

@app.route('/delete_tourism_benefit_everyone/<int:item_id>')
def delete_tourism_benefit_everyone(item_id):
    TourismBenefitEveryoneService.delete_tourism_benefit_everyone(item_id)
    return redirect(url_for('edit_tourism_benefit_everyone'))

@app.route('/profile/<int:id>')
def member_profile(id):
    # Fetch member details from the database based on member_id
    member = UserProfileService.get_profile_by_user_id(id)
    return render_template('member_profile.html', member=member)
