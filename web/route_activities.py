from flask import Flask, render_template, request, jsonify, redirect, url_for
from app import app
from database.services.activities_service import ActivitiesService
from database.services.header_image_service import HeaderImageService
from database.services.footer_service import FooterService
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/usr/share/nginx/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/activities')
def activities():
    activities = ActivitiesService.get_all_activities()
    header_image = HeaderImageService.get_header_image_by_name("Activities")
    footer = FooterService.get_footer_by_id(1)
    return render_template('activities.html', activities= activities, header_image=header_image, footer=footer)

@app.route('/edit_activities', methods=['GET'])
def edit_activities():
    activities = ActivitiesService.get_all_activities()
    return render_template('edit_activities.html', activities=activities)

# Route để thêm mục mới
@app.route('/add_activities', methods=['POST'])
def add_activities():
    name = request.form['name']
    description = request.form['description']
    image_files = request.files.getlist('image_files[]')  # Nhận danh sách các file hình ảnh từ form

    # Tạo danh sách các tên file đã được upload
    image_urls = []
    for image_file in image_files:
        if image_file.filename != '':
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_urls.append(filename)

    ActivitiesService.add_activity(name=name, description=description, image_urls=image_urls)

    return redirect(url_for('edit_activities'))

# Route để xóa mục
@app.route('/delete_activities/<int:item_id>')
def delete_activities(item_id):
    ActivitiesService.delete_activity(item_id)
    return redirect(url_for('edit_activities'))

@app.route('/update_activities/<int:item_id>', methods=['GET', 'POST'])
def update_activities(item_id):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image_files = request.files.getlist('image_files[]')  # Nhận danh sách các file hình ảnh từ form

        # Tạo danh sách các tên file đã được upload
        image_urls = []
        for image_file in image_files:
            if image_file.filename != '':
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_urls.append(filename)

        ActivitiesService.update_activity(item_id=item_id, name=name, description=description, image_urls=image_urls)
    return render_template('edit_activities.html')