from flask import Flask, render_template, request, jsonify, redirect, url_for
from __main__ import app
from database.services.footer_service import FooterService

@app.route('/edit_footer', methods=['GET', 'POST'])
def edit_footer():
    footers = FooterService.get_all_footers()
    if not footers:
        footers = FooterService.add_footer('+84 978931085', 'info@lifesabeachvietnam.com', 'Thôn 2 Bãi Bàng, QL1D, Xuân Hải, Sông Cầu, Phú Yên 560000, Vietnam', 'https://www.facebook.com/', 'https://www.instagram.com/', 'https://www.tiktok.com/')

    return render_template('edit_footer.html', footers=footers)

@app.route('/update_footer/<int:item_id>', methods=['GET', 'POST'])
def update_footer(item_id):
    if request.method == 'POST':
        phone = request.form['phone']
        email= request.form['email']
        address = request.form['address']
        link_facebook = request.form['linkfacebook']
        link_instagram= request.form['linkinsta']
        link_tiktok = request.form['linktiktok']
        FooterService.update_footer(item_id=item_id, phone=phone, email=email, address=address, link_facebook=link_facebook, link_instagram=link_instagram, link_tiktok=link_tiktok)
        return redirect(url_for('edit_footer'))
    # Render template cho trang sửa
    return render_template('edit_footer.html')