from flask import Flask, render_template, request, jsonify, redirect, url_for
from __main__ import app
from database.services.our_story_service import OurStoryService, TourismBenefitEveryoneService
from database.services.user_service import UserProfileService
from database.services.header_image_service import HeaderImageService
from database.services.footer_service import FooterService
@app.route('/aboutus')
def aboutus():
    our_story = OurStoryService.get_all_our_stories()
    tourism_benefit_everyones = TourismBenefitEveryoneService.get_all_tourism_benefit_everyones()
    profiles = UserProfileService.get_all_profiles()
    header_image = HeaderImageService.get_header_image_by_name("Home Page")
    footer = FooterService.get_footer_by_id(1)
    return render_template('aboutus.html',our_story=our_story, tourism_benefit_everyones=tourism_benefit_everyones, profiles=profiles, header_image=header_image, footer=footer)

@app.route('/edit_our_story', methods=['GET', 'POST'])
def edit_our_story():
    data = OurStoryService.get_all_our_stories()
    return render_template('edit_our_story.html', data=data)


@app.route('/add_our_story', methods=['POST'])
def add_our_story():
    text = request.form['text']
    image_url = request.form['image_url']
    OurStoryService.add_our_story(text=text, image_url=image_url)
    return redirect(url_for('edit_our_story'))

@app.route('/update_our_story/<int:item_id>', methods=['GET', 'POST'])
def update_our_story(item_id):
    if request.method == 'POST':
        text = request.form['text']
        image_url = request.form['image_url']
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
    image_url = request.form['image_url']
    TourismBenefitEveryoneService.add_tourism_benefit_everyone(text=text, image_url=image_url)
    return redirect(url_for('edit_tourism_benefit_everyone'))

@app.route('/update_tourism_benefit_everyone/<int:item_id>', methods=['GET', 'POST'])
def update_tourism_benefit_everyone(item_id):
    if request.method == 'POST':
        text = request.form['text']
        image_url = request.form['image_url']
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
