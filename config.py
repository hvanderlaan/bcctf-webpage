class Config:
    SECRET_KEY: str = "0df015aeca59b5564429a676268f9fe047123c3f"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///ctf.db"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False