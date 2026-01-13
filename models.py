from extensions import db

solved_challenges = db.Table('solved_challenges',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'))
)

class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    password: str = db.Column(db.String(200), nullable=False)
    score: int = db.Column(db.Integer, default=0)
    solved: int = db.Column(db.Integer, default=0)
    is_admin: bool = db.Column(db.Boolean, default=False)
    profile_pic: str = db.Column(db.String(200), default='default.png')
    solved_challenges = db.relationship('Challenge', secondary=solved_challenges, backref='solved_by')

class Challenge(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(120))
    description: str = db.Column(db.Text)
    flag: str = db.Column(db.String(120))
    points: int = db.Column(db.Integer)
