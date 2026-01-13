from flask import Blueprint, render_template, redirect, url_for, flash, session, current_app
from models import User
from extensions import db
from forms import ChangePasswordForm, ProfilePicForm
from decorators import login_required
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import os

user_bp: Blueprint = Blueprint("user", __name__)
UPLOAD_FOLDER: str = "static/uploads"

@user_bp.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password() -> render_template:
    '''
    change_password route for flask (/change-password)
    
    :return: Description
    :rtype: Any
    '''
    form: ChangePasswordForm= ChangePasswordForm()
    user: User = User.query.get(session["user_id"])

    if form.validate_on_submit():
        if check_password_hash(user.password, form.old_password.data):
            user.password = generate_password_hash(form.new_password.data)
            db.session.commit()
            flash("Wachtwoord succesvol gewijzigd!")
            return redirect(url_for("main.profile"))
        else:
            flash("Oud wachtwoord klopt niet!")

    return render_template("change_password.html", form=form)

@user_bp.route("/change-profile-pic", methods=["GET", "POST"])
@login_required
def change_profile_pic():
    form = ProfilePicForm()
    user = User.query.get(session["user_id"])

    if form.validate_on_submit() and form.picture.data:
        pic = form.picture.data
        filename = secure_filename(pic.filename)
        filepath = os.path.join(current_app.root_path, UPLOAD_FOLDER, filename)
        pic.save(filepath)
        user.profile_pic = filename
        db.session.commit()
        flash("Profielfoto gewijzigd!")
        return redirect(url_for("main.profile"))

    return render_template("change_profile_pic.html", form=form, user=user)