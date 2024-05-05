from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)
from database.services.header_image_service import HeaderImageService

from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = '/usr/share/nginx/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/edit_header_image', methods=['GET'])
def edit_header_image():
    header_images = HeaderImageService.get_all_header_images()
    return render_template('edit_header_image.html', header_images=header_images)

# Route để thêm mục mới
@app.route('/add_header_image', methods=['POST'])
def add_header_image():
    page_name = request.form['name']
    image_files = request.files.getlist('image_files[]')  # Nhận danh sách các file hình ảnh từ form

    # Tạo danh sách các tên file đã được upload
    image_urls = []
    for image_file in image_files:
        if image_file.filename != '':
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_urls.append(filename)
    HeaderImageService.add_header_image(page_name=page_name, image_urls=image_urls)

    return redirect(url_for('edit_header_image'))

# Route để xóa mục
@app.route('/delete_header_image/<int:item_id>')
def delete_header_image(item_id):
    HeaderImageService.delete_header_image(item_id)
    return redirect(url_for('edit_header_image'))

# Route để cập nhật mục
@app.route('/update_header_image/<int:item_id>', methods=['GET', 'POST'])
def update_header_image(item_id):
    if request.method == 'POST':
        page_name = request.form['name']
        image_files = request.files.getlist('image_files[]')  # Nhận danh sách các file hình ảnh từ form

        # Tạo danh sách các tên file đã được upload
        image_urls = []
        for image_file in image_files:
            if image_file.filename != '':
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_urls.append(filename)
        HeaderImageService.update_header_image(item_id=item_id, page_name=page_name, image_urls=image_urls)
        return redirect(url_for('edit_header_image'))
    return render_template('edit_header_image.html')