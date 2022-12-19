from flask import render_template, redirect, url_for, request, flash
from .models import User
from flask_login import login_user, logout_user, login_required, current_user

def get_auth_routes(app):
    
    # View that gets user credentials from a form
    # Checks if a user with the username exists
    # Compares the input password with the user password
    # Logs in the user if nothing goes wrong
    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get("username")
            password = request.form.get("password")

            user = User.query.filter_by(username=username).first()
            if not user:
                flash('User does not exist.', category='error')
                
            elif not user.password == password:
                flash('Password is incorrect.', category='error')
                
            else:
                login_user(user, remember=True)
                return redirect(url_for('home'))

        return render_template("login.html", user=current_user)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("home"))
    
    return app
