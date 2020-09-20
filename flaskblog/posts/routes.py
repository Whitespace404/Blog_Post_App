from flask import (redirect, render_template, Blueprint,
                   abort, flash, url_for, request)
from flaskblog.models import Post
from flaskblog import db
from flask_login import current_user, login_required
from flaskblog.posts.forms import PostForm, VerifyPostForm, ConfirmDeleteForm
from random import choice

posts = Blueprint("posts", __name__)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
            font=form.font.data,
            font_color=form.font_color.data,
        )
        db.session.add(post)
        db.session.commit()

        flash("Your post has been created successfully!", "success")
        return redirect(url_for("main.home"))
    return render_template("post_actions.html", form=form, legend="Create a Post")


@posts.route("/post/<int:post_id>/view", methods=["GET", "POST"])
@login_required
def post(post_id):
    validated = False

    if current_user.username == "__FLASKBLOG_ADMIN__":
        validated = True

    post = Post.query.get_or_404(post_id)

    # this is to prevent users from refreshing the page to gain more views
    choices = [1, 1, 0, 0, 0, 0]
    incrementing_number = choice(choices)
    post.views += incrementing_number
    db.session.commit()

    return render_template("post.html", post=post, validated=validated)


@login_required
@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)

    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.font = form.font.data
        post.font_color = form.font_color.data
        post.is_edited = True
        db.session.commit()
        flash("Your post has been updated successfully", "success")
        return redirect(url_for("posts.post", post_id=post.id))

    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content

    return render_template("post_actions.html", form=form, legend="Update Post")


@posts.route("/post/<int:post_id>/delete", methods=["GET", "POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash("Your post has been deleted successfully.", "success")
    return redirect(url_for("main.home"))


@login_required
@posts.route("/validate_post/<int:post_id>", methods=["GET", "POST"])
def validate_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user.username != "__FLASKBLOG_ADMIN__":
        abort(403)

    elif current_user.username == "__FLASKBLOG_ADMIN__":
        validated = True

    form = VerifyPostForm()

    if form.validate_on_submit():
        post.is_verified = form.verify.data
        db.session.commit()
        flash("That post has been verified.", "success")
        return redirect(url_for("main.home"))

    return render_template(
        "verify_post.html", form=form, post=post, legend="Verify this Post"
    )


@posts.route("/confirm_delete_post/<int:post_id>", methods=["GET", "POST"])
@login_required
def confirm_delete_post(post_id):
    form = ConfirmDeleteForm()
    post = Post.query.get_or_404(post_id)

    if form.validate_on_submit():
        return redirect(url_for("posts.delete_post", post_id=post.id))

    return render_template(
        "confirm_post_deletion.html",
        form=form,
        post=post,
        legend="Are you sure?",
    )


@posts.route("/post/forward/<int:post_id>", methods=["POST"])
@login_required
def forward_post(post_id):
    original_post = Post.query.get_or_404(post_id)
    new_post = Post(
        title=original_post.title,
        content=original_post.content,
        author=current_user,
        font=original_post.font,
        font_color=original_post.font_color,
        is_forwarded=True
    )
    db.session.add(new_post)
    db.session.commit()
    flash("You have forwarded that post successfully.", "success")
    return redirect(url_for("main.home"))
