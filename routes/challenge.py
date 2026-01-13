from flask import Blueprint, render_template, session, flash
from models import Challenge, User
from extensions import db
from forms import ChallengeForm
from decorators import login_required

challenge_bp: Blueprint = Blueprint("challenge", __name__)

@challenge_bp.route("/challenge/<int:id>", methods=["GET", "POST"])
@login_required
def challenge(id) -> render_template:
    '''
    challenge route for flask (/challenge/<ud>)
    
    :param id: challenge id
    :return: Challenge page
    :rtype: render template
    '''
    chal: Challenge = Challenge.query.get_or_404(id)
    user: User = User.query.get(session["user_id"])
    form: ChallengeForm = ChallengeForm()

    already_solved = chal in user.solved_challenges

    if form.validate_on_submit():
        if already_solved:
            flash("Je hebt deze challenge al opgelost!")
        elif form.flag.data == chal.flag:
            user.score += chal.points
            user.solved += 1
            user.solved_challenges.append(chal)  # Mark as solved
            db.session.commit()
            flash("Correct! 🎉")
        else:
            flash("Wrong flag")

    return render_template("challenge.html", chal=chal, form=form, already_solved=already_solved)

