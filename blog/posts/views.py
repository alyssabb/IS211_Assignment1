from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from users.models import User
from db import db

def get_post_views(app):
    
    # View that show a list of posts from new to old
    @app.route("/")
    def home():
        posts = Post.query.all()
        posts.reverse()
        return render_template("home.html", user=current_user, posts=posts)

    # View that takes data from a html form and creates a post with that data
    @app.route("/create-post", methods=['GET', 'POST'])
    @login_required
    def create_post():
        if request.method == "POST":
            title = request.form.get('title')
            text = request.form.get('text')

            # Checks if the content exists and returns an invalid post response if it doesn't
            if not text or not title:
                flash('Invalid post', category='error')
            else:
                post = Post(title=title, text=text, author=current_user.id)
                db.session.add(post)
                db.session.commit()
                flash('Post created!', category='success')
                return redirect(url_for('home'))

        return render_template('create_post.html', user=current_user)
    
    # Returns a form with the data of a specific post to be updated
    # If a change is made this view updates the post
    @app.route("/edit-post/<id>", methods = ['GET', 'POST'])
    @login_required
    def edit_post(id):
        post = Post.query.filter_by(id=id).first()
        
        if current_user.id != post.author:
            flash('Permission denied', category='error')
        # If the post does not exists send an error response
        if not post:
            flash('Post does not exist', category='error')
            
        if request.method == "POST":
            title = request.form.get('title')
            text = request.form.get('text')
            
            if not title or not text: 
                flash('Post not updated', category='error')
            else:
                post.title = title
                post.text = text
                db.session.commit()
                flash('Post updated.', category='success')
                return redirect(url_for('home'))
        
        return render_template('create_post.html', user=current_user, post=post)

    # View that lets the user delete a post based in its id
    @app.route("/delete-post/<id>")
    @login_required
    def delete_post(id):
        post = Post.query.filter_by(id=id).first()

        # If the post doesn't exist or the user is not the owner of the post 
        # return an error response
        if not post or current_user.id != post.author:
            flash("Post could not be deleted.", category='error')
        else:
            db.session.delete(post)
            db.session.commit()
            flash('Post deleted.', category='success')

        return redirect(url_for('home'))
    
    return app