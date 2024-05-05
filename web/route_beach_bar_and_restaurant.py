from flask import Flask, render_template, request, jsonify, redirect, url_for
from app import app
from database.services.beach_bar_restaurant_service import BeachBarRestaurantService
from database.services.header_image_service import HeaderImageService
from database.services.footer_service import FooterService

from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/usr/share/nginx/static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/beach_bar_restaurant')
def beach_bar_restaurant():
    restaurant_info = BeachBarRestaurantService.get_restaurant_info_by_id(1)
    foods = BeachBarRestaurantService.get_all_foods()
    drinks = BeachBarRestaurantService.get_all_drinks()
    image_collection = BeachBarRestaurantService.get_all_image_collection()
    menus = BeachBarRestaurantService.get_all_restaurant_menu()
    header_image = HeaderImageService.get_header_image_by_name("Beach bar restaurant")
    footer = FooterService.get_footer_by_id(1)
    if restaurant_info is None:
        restaurant_name='Beachfront Restaurant'
        beach_bar_hours='9:00 AM - 12:00 PM'
        restaurant_hours='9:00 AM - 10:00 PM'
        happy_hour_hours='6:00 PM - 7:00 PM'
        description='Indulge in a delightful culinary experience by the seaside with an extensive selection of dishes from Europe, Vietnam, and traditional Vietnamese family dinners. Our beachfront restaurant offers a diverse menu featuring mouthwatering options to satisfy every craving. From savory European classics to authentic Vietnamese specialties, guests can embark on a culinary journey that celebrates the rich flavors and traditions of both cultures. In addition to our delectable food offerings, we also feature an enticing array of beverages, including a variety of beers and handcrafted cocktails. Whether you prefer a refreshing beer to complement your meal or a meticulously crafted cocktail to enjoy as you soak in the ocean breeze, our bar has something for everyone. Join us during our restaurant hours to experience the perfect blend of flavors and cultures, creating unforgettable memories with every sip and bite.'
        BeachBarRestaurantService.add_restaurant_info(restaurant_name, beach_bar_hours, restaurant_hours, happy_hour_hours, description)
        
    return render_template('beach_bar_restaurant.html', restaurant_info=restaurant_info, foods=foods, drinks= drinks, image_collection=image_collection, menus=menus, header_image=header_image, footer=footer)

@app.route('/edit_beach_bar_restaurant_info', methods=['GET', 'POST'])
def edit_beach_bar_restaurant_info():
    restaurant_info = BeachBarRestaurantService.get_all_restaurant_infos()
    return render_template('edit_beach_bar_restaurant_info.html', restaurant_info=restaurant_info)

# Route để cập nhật mục
@app.route('/update_beach_bar_restaurant_info/<int:item_id>', methods=['GET', 'POST'])
def update_beach_bar_restaurant_info(item_id):
    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name']
        beach_bar_hours = request.form['beach_bar_hours']
        restaurant_hours = request.form['restaurant_hours']
        happy_hour_hours = request.form['happy_hour_hours']
        description = request.form['description']
        BeachBarRestaurantService.update_restaurant_info(item_id, restaurant_name, beach_bar_hours, restaurant_hours, happy_hour_hours, description)
        return redirect(url_for('edit_beach_bar_restaurant_info'))
    return render_template('edit_beach_bar_restaurant_info.html')

@app.route('/edit_beach_bar_restaurant_foods', methods=['GET', 'POST'])
def edit_beach_bar_restaurant_foods():
    foods = BeachBarRestaurantService.get_all_foods()
    return render_template('edit_beach_bar_restaurant_foods.html', foods=foods)

# Route để thêm mục mới
@app.route('/add_foods', methods=['POST'])
def add_foods():
    name = request.form['name']
    image_file = request.files['image_file']
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_url = filename
    BeachBarRestaurantService.add_food(name=name, image_url=image_url)
    return redirect(url_for('edit_beach_bar_restaurant_foods'))

# Route để xóa mục
@app.route('/delete_foods/<int:item_id>')
def delete_foods(item_id):
    BeachBarRestaurantService.delete_food(item_id)
    return redirect(url_for('edit_beach_bar_restaurant_foods'))

# Route để cập nhật mục
@app.route('/update_foods/<int:item_id>', methods=['GET', 'POST'])
def update_foods(item_id):
    if request.method == 'POST':
        name = request.form['name']
        if 'image_file' in request.files:
            image_file = request.files['image_file']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename
        else:
            # If no image file is provided, keep the existing image URL
            image_url = request.form['image_file']
        BeachBarRestaurantService.update_food(item_id, name=name, image_url=image_url)
        return redirect(url_for('edit_beach_bar_restaurant_foods'))
    return render_template('edit_beach_bar_restaurant_foods.html')

@app.route('/edit_beach_bar_restaurant_drinks', methods=['GET', 'POST'])
def edit_beach_bar_restaurant_drinks():
    drinks = BeachBarRestaurantService.get_all_drinks()
    return render_template('edit_beach_bar_restaurant_drinks.html', drinks=drinks)

# Route để thêm mục mới
@app.route('/add_drinks', methods=['POST'])
def add_drinks():
    name = request.form['name']
    image_file = request.files['image_file']
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_url = filename
    BeachBarRestaurantService.add_drink(name=name, image_url=image_url)
    return redirect(url_for('edit_beach_bar_restaurant_drinks'))

# Route để xóa mục
@app.route('/delete_drinks/<int:item_id>')
def delete_drinks(item_id):
    BeachBarRestaurantService.delete_drink(item_id)
    return redirect(url_for('edit_beach_bar_restaurant_drinks'))

# Route để cập nhật mục
@app.route('/update_drinks/<int:item_id>', methods=['GET', 'POST'])
def update_drinks(item_id):
    if request.method == 'POST':
        name = request.form['name']
        if 'image_file' in request.files:
            image_file = request.files['image_file']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename
        else:
            # If no image file is provided, keep the existing image URL
            image_url = request.form['image_file']
        BeachBarRestaurantService.update_drink(item_id, name=name, image_url=image_url)
        return redirect(url_for('edit_beach_bar_restaurant_drinks'))
    return render_template('edit_beach_bar_restaurant_drinks.html')

@app.route('/edit_beach_bar_restaurant_discover_our_beach_bar', methods=['GET', 'POST'])
def edit_beach_bar_restaurant_discover_our_beach_bar():
    data = BeachBarRestaurantService.get_all_image_collection()
    return render_template('edit_beach_bar_restaurant_discover_our_beach_bar.html', data=data)

# Route để thêm mục mới
@app.route('/add_discover_our_beach_bars', methods=['POST'])
def add_discover_our_beach_bars():
    overlay_content = request.form['overlay_content']
    image_file = request.files['image_file']
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_url = filename
    BeachBarRestaurantService.add_image_collection(image_url=image_url, overlay_content=overlay_content)
    return redirect(url_for('edit_beach_bar_restaurant_discover_our_beach_bar'))

# Route để xóa mục
@app.route('/delete_discover_our_beach_bars/<int:item_id>')
def delete_discover_our_beach_bars(item_id):
    BeachBarRestaurantService.delete_image_collection(item_id)
    return redirect(url_for('edit_beach_bar_restaurant_discover_our_beach_bar'))

# Route để cập nhật mục
@app.route('/update_discover_our_beach_bars/<int:item_id>', methods=['GET', 'POST'])
def update_discover_our_beach_bars(item_id):
    if request.method == 'POST':
        overlay_content = request.form['overlay_content']
        if 'image_file' in request.files:  # Kiểm tra xem người dùng đã gửi file ảnh hay chưa
            image_file = request.files['image_file']
            if image_file and allowed_file(image_file.filename):  # Kiểm tra định dạng file ảnh
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename  # Lưu đường dẫn của ảnh mới

        # Cập nhật thông tin của mục trong cơ sở dữ liệu
        BeachBarRestaurantService.update_image_collection(item_id=item_id, overlay_content=overlay_content, image_url=image_url)

        return redirect(url_for('edit_beach_bar_restaurant_discover_our_beach_bar'))

    return render_template('edit_beach_bar_restaurant_discover_our_beach_bar.html')


@app.route('/edit_beach_bar_restaurant_menu', methods=['GET', 'POST'])
def edit_beach_bar_restaurant_menu():
    data = BeachBarRestaurantService.get_all_restaurant_menu()
    return render_template('edit_beach_bar_restaurant_menu.html', data=data)

# Route để thêm mục mới
@app.route('/add_menu', methods=['POST'])
def add_menu():
    image_file = request.files['image_file']
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_url = filename
    BeachBarRestaurantService.add_restaurant_menu(image_url=image_url)
    return redirect(url_for('edit_beach_bar_restaurant_menu'))

# Route để xóa mục
@app.route('/delete_menu/<int:item_id>')
def delete_menu(item_id):
    BeachBarRestaurantService.delete_restaurant_menu(item_id)
    return redirect(url_for('edit_beach_bar_restaurant_menu'))

# Route để cập nhật mục
@app.route('/update_menu/<int:item_id>', methods=['GET', 'POST'])
def update_menu(item_id):
    if request.method == 'POST':
        if 'image_file' in request.files:
            image_file = request.files['image_file']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = filename
        else:
            # If no image file is provided, keep the existing image URL
            image_url = request.form['image_file']
        BeachBarRestaurantService.update_restaurant_menu(item_id, image_url=image_url)
        return redirect(url_for('edit_beach_bar_restaurant_menu'))
    return render_template('edit_beach_bar_restaurant_menu.html')
