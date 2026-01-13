from flask import Blueprint, render_template, redirect, url_for
from models import Challenge
from extensions import db
from forms import AdminChallengeForm
from decorators import admin_required

admin: Blueprint = Blueprint("admin", __name__)

@admin.route("/admin", methods=["GET", "POST"])
@admin_required
def panel() -> render_template:
    '''
    panel route for flask (/admin)
    
    :return: Admin panel
    :rtype: render_template
    '''
    form: AdminChallengeForm = AdminChallengeForm()
    challenges: Challenge = Challenge.query.all()

    if form.validate_on_submit():
        chal: Challenge = Challenge(
            title=form.title.data,
            description=form.description.data,
            flag=form.flag.data,
            points=form.points.data
        )
        db.session.add(chal)
        db.session.commit()
        return redirect(url_for("admin.panel"))

    return render_template("admin.html", form=form, challenges=challenges)
