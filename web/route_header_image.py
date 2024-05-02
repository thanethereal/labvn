from flask import Flask, render_template, request, jsonify, redirect, url_for
from __main__ import app
from database.services.header_image_service import HeaderImageService

@app.route('/edit_header_image', methods=['GET'])
def edit_header_image():
    header_images = HeaderImageService.get_all_header_images()
    return render_template('edit_header_image.html', header_images=header_images)

# Route để thêm mục mới
@app.route('/add_header_image', methods=['POST'])
def add_header_image():
    page_name = request.form['name']
    image_urls = request.form.getlist('image_urls[]')  # Nhận danh sách các URL hình ảnh từ form
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
        image_urls = request.form.getlist('image_urls[]')
        HeaderImageService.update_header_image(item_id=item_id, page_name=page_name, image_urls=image_urls)
        return redirect(url_for('edit_header_image'))
    return render_template('edit_header_image.html')