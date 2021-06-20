from app import app
from models import db, User, Feedback

db.drop_all()
db.create_all()

u1 = User(
    username = "Millie",
    password = "millieisthebest",
    email = "millie@millie.com",
    first_name = "Millie",
    last_name = "Menes"
)

u2 = User(
    username = "Amelia",
    password = "creamsicle",
    email = "amelia@amelia.com",
    first_name = "Amelia",
    last_name = "Menes"
)

db.session.add_all([u1, u2])
db.session.commit()