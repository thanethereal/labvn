from flask import Flask, render_template, request, jsonify, redirect, url_for
from __main__ import app
from database.services.getting_here_service import GettingHereService
from database.services.header_image_service import HeaderImageService
from database.services.footer_service import FooterService
@app.route('/gettinghere')
def gettinghere():
    info = GettingHereService.get_getting_here_info_by_id(1)
    getting_heres = GettingHereService.get_all_getting_heres()
    header_image = HeaderImageService.get_header_image_by_name("Home Page")
    footer = FooterService.get_footer_by_id(1)
    return render_template('gettinghere.html', info=info, getting_heres=getting_heres, header_image=header_image, footer=footer)

@app.route('/edit_getting_here_info', methods=['GET', 'POST'])
def edit_getting_here_info():
    info = GettingHereService.get_all_getting_here_infos()
    if info is None or len(info) == 0:
        title='Directions',
        description='The city of Quy Nhon has good transport links although they may not be at the most convenient times of day.\nPLEASE MAKE SURE THAT YOU KEEP US INFORMED OF YOUR ANTICIPATED TIME OF ARRIVAL.'
        GettingHereService.add_getting_here_info(title=title, description=description)
        return render_template('edit_getting_here_info.html', info=info)
    return render_template('edit_getting_here_info.html', info=info)

# Route để cập nhật mục
@app.route('/update_getting_here_info/<int:item_id>', methods=['GET', 'POST'])
def update_getting_here_info(item_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        GettingHereService.update_getting_here_info(item_id=item_id, title=title, description=description)
    return render_template('edit_getting_here_info.html')


@app.route('/edit_getting_here', methods=['GET'])
def edit_getting_here():
    gettingheres = GettingHereService.get_all_getting_heres()
    return render_template('edit_getting_here.html', gettingheres=gettingheres)

# Route để thêm mục mới
@app.route('/add_getting_here', methods=['POST'])
def add_getting_here():
    name = request.form['name']
    description = request.form['description']
    image_urls = request.form.getlist('image_urls[]')  # Nhận danh sách các URL hình ảnh từ form
    links = request.form.getlist('links[]')
    GettingHereService.add_getting_here(name=name, image_urls=image_urls, links=links, description=description)

    return redirect(url_for('edit_getting_here'))

# Route để xóa mục
@app.route('/delete_getting_here/<int:item_id>')
def delete_getting_here(item_id):
    GettingHereService.delete_getting_here(item_id)
    return redirect(url_for('edit_getting_here'))

# Route để cập nhật mục
@app.route('/update_getting_here/<int:item_id>', methods=['GET', 'POST'])
def update_getting_here(item_id):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image_urls = request.form.getlist('image_urls[]')
        links = request.form.getlist('links[]')
        GettingHereService.update_getting_here(item_id=item_id, name=name, description=description, image_urls=image_urls, links=links)
        return redirect(url_for('edit_getting_here'))
    return render_template('edit_getting_here.html')