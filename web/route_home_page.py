from flask import Flask, render_template, request, jsonify, redirect, url_for
from __main__ import app
from database.services.home_page_service import HomePageService
from database.services.header_image_service import HeaderImageService
from database.services.footer_service import FooterService
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/home_page')
def home_page():
    descriptions = HomePageService.get_all_descriptions()
    main_sections = HomePageService.get_all_sections()
    header_image = HeaderImageService.get_header_image_by_name("Home Page")
    footer = FooterService.get_footer_by_id(1)
    return render_template('home_page.html', descriptions = descriptions, main_sections = main_sections, header_image= header_image, footer=footer)

@app.route('/edit_home_page_description', methods=['GET', 'POST'])
def edit_home_page_description():
    descriptions = HomePageService.get_all_descriptions()
    return render_template('edit_home_page_description.html', descriptions=descriptions)


@app.route('/add_home_page_description', methods=['POST'])
def add_home_page_description():
    text = request.form['text']
    image_file = request.files['image_file']
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_url = filename
        HomePageService.add_description(text=text, image_url=image_url)
        return redirect(url_for('edit_home_page_description'))
    else:
        # Handle invalid file format
        return "Invalid file format"

@app.route('/update_home_page_description/<int:item_id>', methods=['GET', 'POST'])
def update_home_page_description(item_id):
    if request.method == 'POST':
        text = request.form['text']
        if 'image_url' in request.files:
            image_file = request.files['image_url']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename
        else:
            # If no image file is provided, keep the existing image URL
            image_url = request.form['image_url']

        # Update the description
        HomePageService.update_description(id=item_id, text=text, image_url=image_url)
        return redirect(url_for('edit_home_page_description'))
    return render_template('edit_home_page_description.html')

@app.route('/delete_home_page_description/<int:item_id>')
def delete_home_page_description(item_id):
    HomePageService.delete_description(item_id)
    return redirect(url_for('edit_home_page_description'))

@app.route('/edit_home_page_main_section', methods=['GET', 'POST'])
def edit_home_page_main_section():
    sections = HomePageService.get_all_sections()
    return render_template('edit_home_page_main_section.html', item = None, sections=sections)

# Route để thêm mục mới
@app.route('/add_home_page_main_section', methods=['POST'])
def add_home_page_main_section():
    title = request.form['title']
    link = request.form['link']
    image_file = request.files['image_file']
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_url = filename
        HomePageService.add_section(title, image_url, link)
    return redirect(url_for('edit_home_page_main_section'))

# Route để xóa mục
@app.route('/delete_home_page_main_section/<int:item_id>')
def delete_home_page_main_section(item_id):
    HomePageService.delete_section(item_id)
    return redirect(url_for('edit_home_page_main_section'))

# Route để cập nhật mục
@app.route('/update_home_page_main_section/<int:item_id>', methods=['GET', 'POST'])
def update_home_page_main_section(item_id):
    if request.method == 'POST':
        # Lấy dữ liệu mới từ form
        title = request.form['title']
        link = request.form['link']
        if 'image_url' in request.files:
            image_file = request.files['image_url']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename
        else:
            # If no image file is provided, keep the existing image URL
            image_url = request.form['image_url']
        HomePageService.update_section(item_id, title, image_url, link)
        return redirect(url_for('edit_home_page_main_section'))
    return render_template('edit_home_page_main_section.html')