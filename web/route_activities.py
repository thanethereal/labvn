from flask import Flask, render_template, request, jsonify, redirect, url_for
from __main__ import app
from database.services.activities_service import ActivitiesService
from database.services.header_image_service import HeaderImageService
from database.services.footer_service import FooterService
@app.route('/activities')
def activities():
    activities = ActivitiesService.get_all_activities()
    header_image = HeaderImageService.get_header_image_by_name("Home Page")
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
    image_urls = request.form.getlist('image_urls[]')  # Nhận danh sách các URL hình ảnh từ form

    ActivitiesService.add_activity(name=name, description=description, image_urls=image_urls)

    return redirect(url_for('edit_activities'))

# Route để xóa mục
@app.route('/delete_activities/<int:item_id>')
def delete_activities(item_id):
    ActivitiesService.delete_activity(item_id)
    return redirect(url_for('edit_activities'))

# Route để cập nhật mục
@app.route('/update_activities/<int:item_id>', methods=['GET', 'POST'])
def update_activities(item_id):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image_urls = request.form.getlist('image_urls[]')
        ActivitiesService.update_activity(item_id=item_id, name=name, description=description, image_urls=image_urls)
    return render_template('edit_activities.html')