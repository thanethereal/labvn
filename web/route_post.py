from flask import Flask, render_template, request, jsonify, redirect, url_for
from __main__ import app
from database.services.post_service import PostService
from database.services.footer_service import FooterService
from database.services.header_image_service import HeaderImageService
@app.context_processor
def utility_processor():
    return dict(len=len)

@app.route('/post')
def post():
    posts = PostService.get_all_posts()
    header_image = HeaderImageService.get_header_image_by_name("Home Page")
    footer = FooterService.get_footer_by_id(1)
    if not posts:
        # Generate fake data if posts are empty
        generate_fake_data()
        posts = PostService.get_all_posts()
    return render_template('post.html', posts=posts, header_image=header_image, footer=footer)

def generate_fake_data():
    # Generate fake data for posts
    fake_posts = [
        {'title': 'Fake Post 1', 'content': 'This is a fake post, This is a fake post, This is a fake post, This is a fake post,This is a fake post ,This is a fake post This is a fake post.', 'image_url' : '../static/img/527619306.jpg', 'user_id': 1},
        {'title': 'Fake Post 2', 'content': 'This is another fake post.','image_url' : '../static/img/527619306.jpg', 'user_id': 1}
        # Add more fake posts as needed
    ]
    for post_data in fake_posts:
        PostService.create_post(**post_data)

@app.route('/edit_post', methods=['GET', 'POST'])
def edit_post():
    posts = PostService.get_all_posts()
    return render_template('edit_post.html', posts=posts)


@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    image_url = request.form['image_url']
    user_id = 1
    PostService.create_post(title=title, content=content, image_url=image_url, user_id=user_id)
    return redirect(url_for('edit_post'))

@app.route('/update_post/<int:item_id>', methods=['GET', 'POST'])
def update_post(item_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image_url = request.form['image_url']
        PostService.update_post(item_id, title, content, image_url, user_id=1)
        return redirect(url_for('edit_post'))
    return render_template('edit_post.html')

@app.route('/delete_post/<int:item_id>')
def delete_post(item_id):
    PostService.delete_post(item_id)
    return redirect(url_for('edit_post'))

@app.route('/view_post/<int:post_id>')
def view_post(post_id):
    post = PostService.get_post_by_id(post_id)
    if post:
        return render_template('view_post.html', post=post)
    else:
        # Handle the case when the post with the given ID does not exist
        return render_template('post_not_found.html', post_id=post_id)
