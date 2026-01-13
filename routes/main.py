from flask import Blueprint, render_template, session
from models import User, Challenge
from decorators import login_required

main = Blueprint("main", __name__)

@main.route("/")
def index() -> render_template:
    '''
    index route for flask (/index.html)
    
    :return: main page
    :rtype: render_template
    '''
    users = User.query.order_by(User.score.desc()).all()
    return render_template("index.html", users=users)

@main.route("/profile")
@login_required
def profile() -> render_template:
    '''
    profile route for flask (/profile)
    
    :return: Profile page
    :rtype: render_template
    '''
    user: User = User.query.get(session["user_id"])
    challenges: Challenge = Challenge.query.all()
    return render_template("profile.html", user=user, challenges=challenges)
