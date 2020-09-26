from flask import Blueprint, flash, redirect, url_for, render_template, request
from flask_login import current_user, login_user, logout_user, login_required
from flaskblog import bcrypt, db
from flaskblog.user.forms import (
    RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ChangePasswordForm)
from flaskblog.user.utils import save_picture, send_reset_confirmation, send_reset_email
from flaskblog.models import User, Post

user = Blueprint("user", __name__)


@user.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You already have an account.", "warning")
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", "success")
        return redirect(url_for("user.login"))
    return render_template("register.html", form=form, legend="Join Us")


@user.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "warning")
        return redirect(url_for("main.home"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            flash("Log in Successful.", "success")
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for("main.home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", form=form, legend="Login")


@user.route("/logout/")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully!", "success")
    return redirect(url_for("main.home"))


@user.route("/account/", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    user = User.query.filter_by(username=current_user.username).first()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()

        flash("Your account has been updated!", "success")
        return redirect(url_for("user.account"))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for(
        "static", filename=f"profile_pics/{current_user.image_file}")
    return render_template(
        "account.html", image_file=image_file, form=form, legend="Update your Account"
    )


@user.route("/user/<string:username>")
def user_post(username):
    page = request.args.get("page", 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = (
        Post.query.filter_by(author=user)
        .order_by(Post.date_posted.desc())
        .paginate(page=page, per_page=5)
    )
    return render_template("filter_post.html", posts=posts, user=user)


@user.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    user = User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token", "warning")
        return redirect(url_for("reset_request"))
    form = ChangePasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode(
            "utf-8"
        )
        user.password = hashed_password
        db.session.commit()
        flash("Your password has been updated! You are now able to log in", "success")
        send_reset_confirmation(user)

        return redirect(url_for("user.login"))
    return render_template(
        "reset_token.html",
        title="Reset Password",
        form=form,
        legend="Change your Password",
    )


@user.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        flash("You are already logged in.")
        return redirect(url_for("main.home"))
    form = RequestResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash(
            "An email has been sent with instructions to reset your password. \
                You can close this tab now.",
            "success",
        )
        return redirect(url_for("user.login"))

    return render_template(
        "reset_request.html",
        title="Reset Password",
        form=form,
        legend="Request a Password Reset",
    )
