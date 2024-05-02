from flask import Flask, render_template, request, jsonify, redirect, url_for
from __main__ import app
from database.services.accommodation_service import AccommodationService
from database.services.header_image_service import HeaderImageService
from database.services.footer_service import FooterService
@app.route('/accommodations')
def accommodations():
    info = AccommodationService.get_accommodation_info_by_id(1)
    rooms = AccommodationService.get_all_room_types()
    header_image = HeaderImageService.get_header_image_by_name("Home Page")
    footer = FooterService.get_footer_by_id(1)
    return render_template('accommodations.html', info=info, rooms=rooms, footer= footer, header_image=header_image)


@app.route('/edit_accommodation_info', methods=['GET'])
def edit_accommodation_info():
    info = AccommodationService.get_accommodation_info_by_id(1)
    if info is None:
        title='Beachfront Restaurant',
        description='Indulge in a delightful culinary experience by the seaside with an extensive selection of dishes from Europe, Vietnam, and traditional Vietnamese family dinners. Our beachfront restaurant offers a diverse menu featuring mouthwatering options to satisfy every craving. From savory European classics to authentic Vietnamese specialties, guests can embark on a culinary journey that celebrates the rich flavors and traditions of both cultures. In addition to our delectable food offerings, we also feature an enticing array of beverages, including a variety of beers and handcrafted cocktails. Whether you prefer a refreshing beer to complement your meal or a meticulously crafted cocktail to enjoy as you soak in the ocean breeze, our bar has something for everyone. Join us during our restaurant hours to experience the perfect blend of flavors and cultures, creating unforgettable memories with every sip and bite.'
        AccommodationService.add_accommodation_info(title=title, description=description)
    return render_template('edit_accommodation_info.html', info=info)

# Route để cập nhật mục
@app.route('/update_accommodation_info/<int:item_id>', methods=['GET', 'POST'])
def update_accommodation_info(item_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        AccommodationService.update_accommodation_info(item_id=item_id, title=title, description=description)
        return redirect(url_for('edit_accommodation_info'))
    return render_template('edit_accommodation_info.html')


@app.route('/edit_accommodation_room_info', methods=['GET'])
def edit_accommodation_room_info():
    rooms = AccommodationService.get_all_room_types()
    return render_template('edit_accommodation_room_info.html', rooms=rooms)

# Route để thêm mục mới
@app.route('/add_accommodation_room_info', methods=['POST'])
def add_accommodation_room_info():
    name = request.form['name']
    description = request.form['description']
    image_urls = request.form.getlist('image_urls[]')  # Nhận danh sách các URL hình ảnh từ form

    AccommodationService.add_room_type(name=name, description=description, image_urls=image_urls)
    return redirect(url_for('edit_accommodation_room_info'))

# Route để xóa mục
@app.route('/delete_accommodation_room_info/<int:item_id>')
def delete_accommodation_room_info(item_id):
    AccommodationService.delete_room_type(item_id)
    return redirect(url_for('edit_accommodation_room_info'))

# Route để cập nhật mục
@app.route('/update_accommodation_room_info/<int:item_id>', methods=['GET', 'POST'])
def update_accommodation_room_info(item_id):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image_urls = request.form.getlist('image_urls[]')
        AccommodationService.update_room_type(item_id=item_id, name=name, description=description, image_urls=image_urls)
        return redirect(url_for('edit_accommodation_room_info'))
    return render_template('edit_accommodation_room_info.html')